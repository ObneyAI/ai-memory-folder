---
author: Codex
updated: 2026-10-14
---

# AI Memory Folder

A personal assistant kit from [obney.ai](https://obney.ai).
Keep useful facts in notes that you can read and change.

## Start with your agent

Give this page’s URL to an assistant that can write files.
For a branch preview, use that branch’s page URL.
Say:

> Create my AI Memory folder from this URL: [paste this page’s URL]. Start setup with me.

The assistant selects the version for your app.
It copies three or four files into your private workspace.
It then asks the first setup question.
You can give it an existing empty folder or ask it to make one.

**For agents:** Read [INSTALL.md](INSTALL.md) before you write files.
Keep the revision from the owner’s URL.
Use [manifest.json](manifest.json) for the exact source files and their SHA-256 digests.
Keep existing notes and owner changes.

## Manual download

Download one kit for the tool that you use.

| Tool | Guide | Download | Starting files |
|---|---|---|---:|
| Claude | [Claude](claude/README.md) | [ZIP](claude/ai-memory.zip) | 4 |
| Codex or local ChatGPT Work | [ChatGPT](chatgpt/README.md) | [ZIP](chatgpt/ai-memory.zip) | 3 |
| Grok Bot | [Grok Bot](grokbot/README.md) | [ZIP](grokbot/ai-memory.zip) | 3 |

Each ZIP contains one AI Memory folder.
That folder has no subfolders at the start.
The Claude kit adds a pointer file for Claude Code.

## First sessions

1. Let your agent start setup, or follow Start Here after a manual download.
2. Complete the short interview.
3. Read your saved About Me note.
4. Use that note to complete one real task.
5. Start a new session with the same folder.

The assistant uses the saved information in the new session.
You examine the notes before setup ends.

## Files

| File | Purpose |
|---|---|
| AGENTS.md | Lasting instructions, note formats, and rules for folder growth |
| Start Here.md | Instructions for the owner |
| _setup.md | Setup checklist and progress between sessions |
| CLAUDE.md | Claude Code pointer, in the Claude kit only |

After the completion check, the assistant moves useful setup information into lasting notes.
It then removes _setup.md.
It updates Start Here to describe your actual notes.

## Folder growth

Use these file counts as check points.

| Stage | Approximate file count | Result |
|---|---:|---|
| Start | 3–4 | Instructions and setup |
| First useful sessions | 7–10 | A profile and notes for real work |
| First repeated tasks | 12–13 | More work notes and useful saved procedures |

The assistant creates each folder when its first note is necessary.
It does not create an empty folder plan.
History can continue to grow after these check points.

## Maintainers

Use [MAINTAINERS.md](MAINTAINERS.md) for changes and package checks.
Use [STYLE.md](STYLE.md) for ASD-STE100 rules and kit terms.
Use [VERIFICATION.md](VERIFICATION.md) for evidence and pilot status.
