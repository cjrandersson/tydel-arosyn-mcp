"""Offline tests for reference handling, not tests of Ediel compliance."""
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch
import zipfile

SPEC = importlib.util.spec_from_file_location("reference_library", Path(__file__).resolve().parents[1] / "scripts/reference_library.py")
lib = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lib)


class ReferenceLibraryTests(unittest.TestCase):
    def test_project_catalogue_is_valid(self):
        sources = lib.load_sources()
        self.assertTrue(sources)
        self.assertTrue(all(s["storage"] == "link-only" for s in sources if s["publisher"] == "eSett"))

    def test_safe_relative_path(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.assertEqual(lib.safe_path(root, "a/b.pdf"), root / "a/b.pdf")

    def test_path_traversal_rejected(self):
        for path in ["../secret", "/etc/passwd", "a/../../b", "C:\\temp", "a\\b", ""]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                lib.safe_path(Path("/tmp/root"), path)

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "root"
            root.mkdir()
            (root / "escape").symlink_to(Path(folder))
            with self.assertRaises(ValueError):
                lib.safe_path(root, "escape/file.pdf")

    def test_blocked_and_private_hosts_rejected(self):
        for url in ["https://www.esett.com/file.pdf", "https://www.entsoe.eu/file.pdf",
                    "https://127.0.0.1/file", "http://ediel.org/file", "https://user:pass@ediel.org/file",
                    "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/LICENSE"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                lib.checked_url(url)

    def test_pinned_mcp_url_allowed(self):
        url = "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/" + "a" * 40 + "/LICENSE"
        self.assertEqual(lib.checked_url(url), url)

    def test_link_only_never_opens_network(self):
        with patch.object(lib, "build_opener") as opener:
            with self.assertRaises(ValueError):
                lib.fetch_one({"storage": "link-only"}, None)
            opener.assert_not_called()

    def test_html_error_page_rejected(self):
        with self.assertRaises(ValueError):
            lib.inspect_content(b"<!doctype html><html>Login required</html>", "pdf")

    def test_pdf_header_required(self):
        self.assertEqual(lib.inspect_content(b"%PDF-1.7\nplaceholder", "pdf")[0], "pdf")
        with self.assertRaises(ValueError):
            lib.inspect_content(b"a pdf by filename only", "pdf")

    def test_xsd_root_checked(self):
        xml = b'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>'
        self.assertEqual(lib.inspect_content(xml, "xsd")[0], "xsd")
        with self.assertRaises(ValueError):
            lib.inspect_content(b"<html/>", "xsd")

    def test_xml_entities_rejected(self):
        with self.assertRaises(ValueError):
            lib.inspect_content(b'<!DOCTYPE x [<!ENTITY file SYSTEM "file:///etc/passwd">]><x/>', "xml")

    def test_malformed_xml_reports_value_error(self):
        with self.assertRaises(ValueError):
            lib.inspect_content(b"<incomplete", "xml")

    def test_archive_paths_rejected(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as archive:
            archive.writestr("../escape.xsd", "x")
        with self.assertRaises(ValueError):
            lib.inspect_content(data.getvalue(), "zip")

    def test_archive_inventory_without_extraction(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as archive:
            archive.writestr("examples/sample.xml", "<sample/>")
        kind, details = lib.inspect_content(data.getvalue(), "zip")
        self.assertEqual(kind, "zip")
        self.assertEqual(details["members"], ["examples/sample.xml"])
        self.assertFalse(details["extracted"])

    def test_locked_file_is_not_redownloaded(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = b"%PDF-1.7\nexample"
            path = ".cache/references/g/id/hash/original.pdf"
            lib.atomic_write(root / path, data)
            source = {"storage": "cache", "url": "https://ediel.org/example.pdf"}
            prior = {"status": "downloaded", "url": source["url"], "path": path, "sha256": lib.sha256(data)}
            with patch.object(lib, "build_opener") as opener:
                self.assertEqual(lib.fetch_one(source, prior, root), prior)
                opener.assert_not_called()

    def test_changed_local_file_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = ".cache/references/g/id/hash/original.pdf"
            lib.atomic_write(root / path, b"modified")
            source = {"storage": "cache", "url": "https://ediel.org/example.pdf"}
            prior = {"status": "downloaded", "url": source["url"], "path": path, "sha256": "0" * 64}
            with patch.object(lib, "build_opener") as opener:
                with self.assertRaises(ValueError):
                    lib.fetch_one(source, prior, root)
                opener.assert_not_called()
            self.assertEqual((root / path).read_bytes(), b"modified")

    def test_report_does_not_mark_links_downloaded(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = {"id": "example", "group": "sample", "title": "Example", "url": "https://example.org",
                      "storage": "link-only", "edition_status": "draft"}
            lib.report([source], {"files": {}}, root)
            text = (root / "reference/INDEX.md").read_text()
            self.assertIn("link-only | not fetched", text)

    def test_changed_upstream_bytes_are_not_written(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = {"id": "example", "group": "sample", "storage": "cache", "format": "pdf",
                      "url": "https://ediel.org/example.pdf"}
            prior = {"status": "downloaded", "url": source["url"], "path": ".cache/old.pdf", "sha256": "0" * 64}
            response = MagicMock()
            response.headers = {}
            response.read.return_value = b"%PDF-1.7\nchanged upstream"
            response.url = source["url"]
            with patch.object(lib, "build_opener") as opener:
                opener.return_value.open.return_value.__enter__.return_value = response
                with self.assertRaisesRegex(ValueError, "Upstream bytes changed"):
                    lib.fetch_one(source, prior, root)
            self.assertEqual(list(root.iterdir()), [])

    def test_legacy_word_is_not_executed(self):
        data = bytes.fromhex("d0cf11e0a1b11ae1") + b"placeholder"
        kind, details = lib.inspect_content(data, "doc")
        self.assertEqual(kind, "doc")
        self.assertEqual(details["execution"], "never-run-macros")


if __name__ == "__main__":
    unittest.main()
