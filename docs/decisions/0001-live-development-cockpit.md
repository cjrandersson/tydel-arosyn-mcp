# Decision 0001 — Live Development Cockpit

**Status:** Replaced by [Decision 0005](0005-machine-readable-project-status.md)  
**Date:** 2026-09-25  
**Replaced:** 2026-09-28

## Historical decision

The repository README was originally designated as the team's live development cockpit and operational source of truth.

It was required to show:

- current milestone;
- current status;
- current objective;
- exact next task;
- explicit owner for the next task;
- blockers / pending decisions;
- explicit owner for every pending, blocked, waiting or next item;
- milestone checklist with completed work checked off;
- next milestone;
- last-updated date.

If Robin must act, the cockpit should still show this explicitly as:

`🚨 @cjrandersson — <required action>`

## Why this was replaced

Keeping operational state directly in README and separately in the visual cockpit created duplicate mutable state and allowed the two views to drift apart.

Decision 0005 keeps the Development Cockpit concept and visual design but moves the canonical status data to `project-status.yml`. README and the SVG cockpit are now human-facing mirrors of that source.
