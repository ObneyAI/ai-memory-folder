---
author: Codex
updated: 2026-10-25
---

# Verification

This record separates file checks from live product behavior.

## Build checks

Run `python3 build.py` after source changes.

| Check | Required result |
|---|---|
| ChatGPT and Grok Bot starting files | Four files each |
| Claude starting files | Five files, including CLAUDE.md |
| Starting subfolders | Zero in every version |
| Manifest | Exact source paths and SHA-256 digests |
| ZIP files | Starting files only, inside one AI Memory folder |
| ZIP extraction | Content matches every source file |
| Relative Markdown links | Every link target exists |
| Writing checks | All prose sentences within 20 words; no em dashes or contractions |
| Nested Git repositories | None inside platform folders |

Build checks passed on October 14, 2026.
The build verified all three ZIPs and 31 relative links.
Each extracted file matched its source.
Common agent instructions and setup checklists matched across all three versions.
The manifest identities matched the instructions.
Two builds produced identical manifest and ZIP bytes.

The prose check applied the 20-word sentence limit throughout the repository.
The manual writing pass used the official dictionary for uncertain verbs and other terms.
Full dictionary and grammar compliance remains a separate editorial check.

## Design checks

These checks inspect the instructions. They do not establish model behavior.

- The starter contains the full growth plan and core procedures.
- Generated paths appear as possible paths, not links to missing files.
- The setup checklist can continue across sessions.
- A later message alone does not prove a new session.
- A completed setup leaves its state in About Me.
- Lasting instructions remain after setup removal.
- Repeat installation preserves personal notes and owner changes.
- Grok Bot routines require a selected schedule and owner approval.
- Memory procedures report unavailable access.
- No setup procedure depends on a plugin, skill upload, or new app connection.

## Product sources

| Topic | Source and use |
|---|---|
| Codex instructions | [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): native instruction discovery |
| Local folder access | [Projects](https://learn.chatgpt.com/docs/projects?surface=app): local folder access differs from uploaded sources |
| Work | [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt): local and cloud source access differ |
| Voice | [Voice](https://learn.chatgpt.com/docs/features/voice): task permissions and feature availability apply |
| OpenAI memory | [Memories](https://learn.chatgpt.com/docs/customization/memories): separate stores and supported controls |
| Cowork setup | [Get started](https://support.claude.com/en/articles/13345190-get-started-with-cowork): explicit project instructions |
| Claude voice | [Voice](https://support.claude.com/en/articles/11101966-use-voice-mode): keep a written-summary path when files are unavailable |
| Grok Bot | Earlier draft from a working bot; fresh-bot memory and voice behavior remain unverified |
| Writing | [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf): rules, dictionary, and technical-term categories |

OpenAI sources were read on October 14, 2026.
Claude findings retain the earlier Claude Code source review.
The official ASD-STE100 PDF was read for this revision.
The automated writing check is not a complete grammar or dictionary check.

## Live pilot tasks

These tasks have not been run with the revised kit.

| Task | Expected result |
|---|---|
| Repository URL install | Agent selects a version and installs only its starting files |
| Repeat install | Personal notes and changed instructions remain intact |
| Partial install | Agent adds only safe missing starting files |
| Interview | One question at a time; owner accepts About Me |
| New session | Agent uses saved context without another interview |
| New responsibility | One real note causes the first Area folder |
| Setup completion | Agent moves lasting information before removal of `_setup.md` |
| Morning check twice | One daily note retains other work |
| Reflection without reply | Draft stays marked `not yet reviewed` |
| Voice | Text reaches the correct folder, or the agent explains missing access |
| Memory unavailable | Agent states the limit without a false change claim |
| Grok Bot routine | Agent creates only the approved schedule and prompt |

## Publication state

The preview branch is `codex/progressive-memory-kits`.
Use its page URL for the revised installer.
The root URL serves the new installer only after this change reaches the default branch.
