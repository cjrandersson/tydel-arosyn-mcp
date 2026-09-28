# Decision 0005 — Machine-readable project status

**Status:** Accepted  
**Date:** 2026-09-28

## Problem

Tydel's project state has been represented in several places: the README cockpit, the visual SVG cockpit and conversational project updates. This creates a risk that a decision is described as complete while one or more repository views still show an older state.

## Decision

`project-status.yml` is the operational source of truth for mutable project status.

It owns at least:

- product strategy / north star;
- current milestone and state;
- current objective;
- exact next task and owner;
- blocked state;
- per-owner task state;
- milestone progress;
- configurable cockpit display labels.

`README.md` and `assets/graphics/development-cockpit.svg` remain the human-facing Development Cockpit. They must reflect the same status model and must not introduce independent pending, blocker, owner or milestone state.

Until an automatic renderer exists, any meaningful status change must update `project-status.yml` first and synchronize the README/SVG mirrors in the same repository change.

## Consequences

- Agents and collaborators read `project-status.yml` before taking ownership of work.
- A status claim is not considered complete merely because it was stated in chat.
- `pending`, `blocked`, `waiting` and `next` require explicit ownership.
- Display labels may change without changing the semantic status model.
- Future work may generate the README/SVG cockpit from `project-status.yml`; that automation is not required for M0.

## Replaces

This decision replaces Decision 0001 only with respect to the source-of-truth mechanism. The Development Cockpit concept, explicit ownership rules and visual presentation remain valid.
