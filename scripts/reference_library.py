#!/usr/bin/env python3
"""Fetch an explicit source catalogue. No crawling, model uploads or archive execution.

Python 3.10+; standard library only. Run from any working directory.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import build_opener, HTTPRedirectHandler, Request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LOCK = Path("reference/download-lock.json")
MAX_BYTES = 30 * 1024 * 1024
MAX_ARCHIVE_BYTES = 150 * 1024 * 1024
ALLOWED_HOSTS = {"www.ediel.se", "ediel.se", "ediel.org",
                 "www.elmarknadshandboken.se", "raw.githubusercontent.com"}
STORAGE = {"vendored", "cache", "link-only"}


def safe_path(root: Path, relative: str) -> Path:
    path = PurePosixPath(relative)
    if not relative or path.is_absolute() or ".." in path.parts or "\\" in relative or ":" in relative:
        raise ValueError(f"Unsafe path: {relative}")
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes project: {relative}")
    return result


def checked_url(url: str) -> str:
    parsed = urlparse(url)
    if (parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError(f"URL is not approved for download: {url}")
    if parsed.hostname == "raw.githubusercontent.com" and not re.match(
            r"^/modelcontextprotocol/modelcontextprotocol/[a-f0-9]{40}/", parsed.path):
        raise ValueError("MCP downloads must use a pinned upstream commit")
    return url


class CheckedRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        checked_url(newurl)
        # Do not follow a source to another publisher, even another allowed host.
        old = urlparse(req.full_url).hostname.removeprefix("www.")
        new = urlparse(newurl).hostname.removeprefix("www.")
        if old != new:
            raise ValueError("Cross-publisher redirect requires review")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def load_sources(root: Path = ROOT) -> list[dict]:
    sources = []
    for path in sorted((root / "reference/catalogs").glob("*.json")):
        catalog = json.loads(path.read_text(encoding="utf-8"))
        if catalog.get("schema_version") != 1:
            raise ValueError(f"Unsupported catalogue: {path.name}")
        sources.extend(catalog["sources"])
    seen = set()
    destinations = set()
    for source in sources:
        sid = source["id"]
        if not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", sid) or sid in seen:
            raise ValueError(f"Invalid/duplicate source ID: {sid}")
        seen.add(sid)
        if source["storage"] not in STORAGE:
            raise ValueError(f"Invalid storage policy: {sid}")
        if source["storage"] != "link-only":
            checked_url(source["url"])
        if source["storage"] == "vendored":
            path = source["path"]
            safe_path(root, path)
            if not path.startswith("reference/vendor/mcp/") or path in destinations:
                raise ValueError(f"Invalid/duplicate vendor path: {sid}")
            destinations.add(path)
            if source["rights"] != "upstream-license":
                raise ValueError(f"Vendored source needs a reviewed license: {sid}")
        if not re.fullmatch(r"[a-z0-9.-]+", source["group"]):
            raise ValueError(f"Unsafe group: {sid}")
    return sources


def read_lock(root: Path = ROOT) -> dict:
    path = root / LOCK
    if not path.exists():
        return {"schema_version": 1, "files": {}}
    lock = json.loads(path.read_text(encoding="utf-8"))
    if lock.get("schema_version") != 1:
        raise ValueError("Unsupported lock version")
    return lock


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".partial-", delete=False) as temp:
        temp_path = Path(temp.name)
        try:
            temp.write(data)
            temp.flush()
        except BaseException:
            temp_path.unlink(missing_ok=True)
            raise
    try:
        temp_path.replace(path)
    finally:
        temp_path.unlink(missing_ok=True)


def inspect_content(data: bytes, expected: str) -> tuple[str, dict]:
    """Check container signatures, NOT Ediel/schema/business-rule validity."""
    if not data or len(data) > MAX_BYTES:
        raise ValueError("Empty or oversized file")
    head = data[:1024].lstrip().lower()
    if expected != "html" and (head.startswith(b"<!doctype html") or head.startswith(b"<html")):
        raise ValueError("Received HTML instead of the requested document")
    if expected == "pdf":
        if not data.startswith(b"%PDF-"):
            raise ValueError("Invalid PDF signature")
        return "pdf", {}
    if expected == "doc":
        if not data.startswith(bytes.fromhex("d0cf11e0a1b11ae1")):
            raise ValueError("Not a legacy Office container")
        return "doc", {"execution": "never-run-macros"}
    if expected in {"xsd", "xml"}:
        if b"<!doctype" in data.lower() or b"<!entity" in data.lower():
            raise ValueError("XML declarations need separate security review")
        import xml.etree.ElementTree as ET
        try:
            node = ET.fromstring(data)
        except ET.ParseError as error:
            raise ValueError(f"Malformed XML: {error}") from error
        if expected == "xsd" and node.tag != "{http://www.w3.org/2001/XMLSchema}schema":
            raise ValueError("Not an XML Schema document")
        return expected, {"root_element": node.tag}
    if expected in {"zip", "xlsx", "pptx", "docx", "spreadsheet", "xls"}:
        if expected in {"xls", "spreadsheet"} and data.startswith(bytes.fromhex("d0cf11e0a1b11ae1")):
            return "xls", {"execution": "never-run-macros"}
        if not zipfile.is_zipfile(io.BytesIO(data)):
            raise ValueError("Not a recognized Office/ZIP container")
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            members = archive.infolist()
            if len(members) > 5000 or sum(m.file_size for m in members) > MAX_ARCHIVE_BYTES:
                raise ValueError("Archive exceeds inspection limits")
            for member in members:
                name = PurePosixPath(member.filename)
                if (name.is_absolute() or ".." in name.parts or "\\" in member.filename
                        or ":" in member.filename or stat.S_ISLNK(member.external_attr >> 16)):
                    raise ValueError("Unsafe archive member")
                if member.file_size > 1024 * 1024 and member.file_size / max(1, member.compress_size) > 300:
                    raise ValueError("Excessive archive compression ratio")
            names = [member.filename for member in members]
            actual = "zip"
            for prefix, kind in [("xl/", "xlsx"), ("ppt/", "pptx"), ("word/", "docx")]:
                if any(name.startswith(prefix) for name in names):
                    actual = kind
                    break
            if expected not in {"zip", "spreadsheet"} and actual != expected:
                raise ValueError(f"Expected {expected}; received {actual}")
            if expected == "spreadsheet" and actual != "xlsx":
                raise ValueError("Not a spreadsheet")
            return actual, {"members": names, "extracted": False, "execution": "never-run"}
    if expected == "json":
        json.loads(data)
    elif expected in {"mdx", "ts", "text"}:
        data.decode("utf-8")
    elif expected == "html":
        if b"<html" not in head and b"<!doctype html" not in head:
            raise ValueError("Not an HTML document")
    else:
        raise ValueError(f"Unsupported file type: {expected}")
    return expected, {}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_one(source: dict, prior: dict | None, root: Path = ROOT) -> dict:
    if source["storage"] == "link-only":
        raise ValueError("Link-only sources must never be downloaded")
    checked_url(source["url"])
    if prior and prior.get("status") == "downloaded":
        if prior["url"] != source["url"]:
            raise ValueError("Source URL changed; create a new source edition")
        path = safe_path(root, prior["path"])
        if path.exists():
            if path.is_symlink() or sha256(path.read_bytes()) != prior["sha256"]:
                raise ValueError("Existing file differs from the lock; refusing replacement")
            return prior
    opener = build_opener(CheckedRedirects())
    request = Request(source["url"], headers={"User-Agent": "TydelReferenceFetcher/1.0 (bounded research download)"})
    with opener.open(request, timeout=35) as response:
        if response.headers.get("Content-Length") and int(response.headers["Content-Length"]) > MAX_BYTES:
            raise ValueError("Download exceeds size limit")
        data = response.read(MAX_BYTES + 1)
        content_type = response.headers.get("Content-Type", "")
        final_url = response.url
    kind, details = inspect_content(data, source["format"])
    digest = sha256(data)
    if prior and prior.get("sha256") and prior["sha256"] != digest:
        raise ValueError("Upstream bytes changed; review as a new edition, not an automatic update")
    if source.get("upstream_blob_sha"):
        git_sha = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if git_sha != source["upstream_blob_sha"]:
            raise ValueError("Upstream Git blob checksum mismatch")
    relative = source.get("path") if source["storage"] == "vendored" else (
        f".cache/references/{source['group']}/{source['id']}/{digest}/original.{kind}")
    path = safe_path(root, relative)
    if path.exists() and sha256(path.read_bytes()) != digest:
        raise ValueError("Refusing to overwrite a different local file")
    atomic_write(path, data)
    # Archive inventories stay private, next to the original. Nothing is extracted.
    if details and source["storage"] == "cache":
        atomic_write(path.with_name("inspection.json"), (json.dumps(details, indent=2) + "\n").encode())
    return {"status": "downloaded", "url": source["url"], "resolved_url": final_url,
            "path": relative, "sha256": digest, "bytes": len(data), "format": kind,
            "content_type": content_type, "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "checks": "checksum-and-container-only",
            **({"archive_members": len(details["members"])} if "members" in details else {})}


def verify(sources: list[dict], lock: dict, include_cache: bool, root: Path = ROOT) -> tuple[int, int]:
    passed = failed = 0
    for source in sources:
        if source["storage"] == "link-only" or (source["storage"] == "cache" and not include_cache):
            continue
        record = lock["files"].get(source["id"], {})
        try:
            if record.get("status") != "downloaded":
                raise ValueError("No successful download recorded")
            if record["url"] != source["url"]:
                raise ValueError("Catalogue and lock URLs differ")
            path = safe_path(root, record["path"])
            expected_prefix = "reference/vendor/mcp/" if source["storage"] == "vendored" else ".cache/references/"
            if not record["path"].startswith(expected_prefix):
                raise ValueError("File does not match its storage policy")
            if source["storage"] == "vendored" and record["path"] != source["path"]:
                raise ValueError("Vendor path differs from the catalogue")
            data = path.read_bytes()
            if sha256(data) != record["sha256"] or len(data) != record["bytes"]:
                raise ValueError("Checksum or size differs")
            inspect_content(data, source["format"])
            passed += 1
        except (ValueError, OSError, KeyError) as error:
            print(f"FAIL {source['id']}: {error}", file=sys.stderr)
            failed += 1
    return passed, failed


def report(sources: list[dict], lock: dict, root: Path = ROOT) -> None:
    """Generate a small overview and a full human-readable link index."""
    groups = sorted({s["group"] for s in sources})
    lines = ["# Source index", "", "Generated from `catalogs/*.json` and `download-lock.json`.", "",
             "A listed source is not necessarily downloaded, current or approved for production.", "",
             "`cache` means local-only; `vendored` means included in Git; `link-only` means not fetched.", ""]
    summary = ["# Download inventory", "", "This records the collection run, not files present on every clone.", "",
               "Only vendored files travel with Git. Recreate the local cache with the fetch command.", "",
               "| Collection | Listed | Vendored | Cached | Links only | Fetch errors |",
               "| --- | ---: | ---: | ---: | ---: | ---: |"]
    totals = [0] * 5
    for group in groups:
        subset = [s for s in sources if s["group"] == group]
        counts = [len(subset), 0, 0, 0, 0]
        lines += [f"## {group}", "", "| Source | Edition status | Storage | Download |", "| --- | --- | --- | --- |"]
        for source in subset:
            record = lock["files"].get(source["id"], {})
            status = record.get("status", "not fetched")
            if source["storage"] == "link-only":
                counts[3] += 1
                status = "not fetched"
            elif status == "downloaded":
                counts[1 if source["storage"] == "vendored" else 2] += 1
            elif status == "error":
                counts[4] += 1
            title = source["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
            lines.append(f"| [{title}]({source['url']}) | {source['edition_status']} | {source['storage']} | {status} |")
        lines += [""]
        totals = [a + b for a, b in zip(totals, counts)]
        summary.append(f"| {group} | " + " | ".join(map(str, counts)) + " |")
    summary += ["| **Total** | " + " | ".join(map(str, totals)) + " |", "",
                "Counts are source files, not distinct standards or unique editions. Archives may contain multiple files.", "",
                "Checks cover checksums, basic file signatures and selected container structure only.",
                "They do not establish market validity, complete schema dependency closure or reuse permission.", ""]
    errors = [(s, lock["files"].get(s["id"], {})) for s in sources
              if lock["files"].get(s["id"], {}).get("status") == "error"]
    if errors:
        summary += ["## Downloads to resolve", ""]
        for source, record in errors:
            summary.append(f"- `{source['id']}`: {record['error']}")
        summary += [""]
    atomic_write(root / "reference/INDEX.md", ("\n".join(lines).rstrip() + "\n").encode())
    atomic_write(root / "reference/INVENTORY.md", ("\n".join(summary).rstrip() + "\n").encode())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["list", "fetch", "verify", "report"])
    parser.add_argument("--group")
    parser.add_argument("--id")
    parser.add_argument("--include-cache", action="store_true", help="Also fetch/verify local-only reference files")
    parser.add_argument("--include-archive", action="store_true", help="Include historical and natural-gas material")
    parser.add_argument("--jobs", type=int, choices=range(1, 5), default=2)
    args = parser.parse_args()
    sources = load_sources()
    if args.command == "report":
        if args.group or args.id:
            parser.error("Report always covers the whole catalogue")
        report(sources, read_lock())
        print("Updated reference/INDEX.md and reference/INVENTORY.md")
        return 0
    if args.group:
        sources = [s for s in sources if s["group"] == args.group]
    if args.id:
        sources = [s for s in sources if s["id"] == args.id]
    if not sources:
        parser.error("No sources match the selection")
    if args.command == "list":
        for source in sources:
            print(f"{source['id']}\t{source['storage']}\t{source['edition_status']}\t{source['title']}")
        return 0
    sources = [s for s in sources if args.include_archive or s["edition_status"] not in {"archive", "natural-gas"}]
    lock = read_lock()
    if args.command == "verify":
        passed, failed = verify(sources, lock, args.include_cache)
        print(f"Verified {passed}; failed {failed}. No market-compliance claim.")
        return 1 if failed else 0
    selected = []
    for source in sources:
        if source["storage"] == "link-only":
            print(f"SKIP {source['id']}: {source['rights']}", flush=True)
        elif source["storage"] == "vendored" or args.include_cache:
            selected.append(source)
    errors = 0

    def run(source):
        try:
            return source, fetch_one(source, lock["files"].get(source["id"])), None
        except (HTTPError, OSError, ValueError, zipfile.BadZipFile) as error:
            return source, None, str(error)

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for source, record, error in pool.map(run, selected):
            if error:
                errors += 1
                print(f"FAIL {source['id']}: {error}", flush=True)
                # Do not discard a previous verified edition on a failed fetch.
                if lock["files"].get(source["id"], {}).get("status") != "downloaded":
                    lock["files"][source["id"]] = {"status": "error", "url": source["url"], "error": error}
            else:
                lock["files"][source["id"]] = record
                print(f"OK {source['id']} ({record['bytes']} bytes)", flush=True)
            atomic_write(ROOT / LOCK, (json.dumps(lock, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode())
    print(f"Selected {len(selected)} sources; {errors} errors. Link-only sources were not fetched.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
