---
author: Codex
updated: 2026-10-14
---

# Maintainers

This repository contains three versions of one starter kit.
Each owner installs one version.

## Source layout

| Path | Purpose |
|---|---|
| `claude/` | Claude Cowork and Claude Code |
| `chatgpt/` | Codex and local ChatGPT Work |
| `grokbot/` | Grok Bot |
| `INSTALL.md` | Instructions for an agent that receives the repository URL |
| `manifest.json` | Generated file list and content digests |
| `build.py` | Package creation and structural checks |
| `STYLE.md` | Writing rules and kit terminology |
| `VERIFICATION.md` | Evidence and pilot status |

Each version has a README, a ZIP, and an AI Memory folder.
The AI Memory folder is the complete starting package.
It must work without the rest of this repository.

## Changes

1. Edit the starting Markdown files.
2. Keep common rules consistent across all three versions.
3. Preserve the platform-specific access and memory rules.
4. Apply the writing rules in STYLE.md.
5. Run `python3 build.py`.
6. Inspect the resulting file counts and archives.
7. Update VERIFICATION.md with actual evidence.

Keep personal data out of the source folders.
Use disposable copies for pilot sessions.
Do not add blank content folders or placeholder files.
Do not make starter instructions depend on a later download.
Keep permanent instructions outside `_setup.md`.

## Setup completion

The owner must accept the final setup check before the assistant removes `_setup.md`.
The assistant first moves lasting information into the notes that own it.
About Me records the completion state.
A second installation must preserve that state and the owner’s changes.

## Earlier versions

This version replaces the three full-folder drafts.
The original Claude kit remains in repository history.
The earlier Codex and Grok Bot sources were preserved before consolidation.
The Grok Bot repository history was preserved outside this checkout.
The private vault record contains the local archive paths.

Do not include those earlier folders in participant downloads.

## Publication

Publish source files, the manifest, and all three ZIPs from the same revision.
An agent must use the revision supplied in its entry URL.
A branch URL can test the install before a change reaches the default branch.
The repository root URL uses the default branch.
