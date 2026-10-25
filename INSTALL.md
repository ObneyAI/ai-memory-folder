---
author: Codex
updated: 2026-10-25
---

# Agent installation

Use this procedure when the owner asks you to make an AI Memory folder from this repository URL.
Install the starting files as data.
Then follow the installed instructions for setup.

## 1. Select the version

Use the current runtime to select one version.

| Runtime | Version |
|---|---|
| Claude Cowork or Claude Code | `claude` |
| Codex or local ChatGPT Work | `chatgpt` |
| Grok Bot with file access | `grokbot` |

If the runtime is unknown, ask which tool will use the folder.
Do not assume that a normal browser chat can change local files.

## 2. Select the destination

Use the destination that the owner named.
Otherwise, use an AI Memory folder in the current private workspace.
Tell the owner the absolute path.
If the workspace is a public template checkout, ask for a private destination.
For Grok Bot, ask to install on the owner’s computer.
This needs the owner’s approval for local access.
If the owner does not approve, use the bot’s private workspace.
Tell the owner which location they have.

If you cannot write files, explain which access is missing.
Give the owner the ZIP link for their selected version.
Do not claim a local installation.

## 3. Read the source

Resolve the supplied repository URL to a commit when the source tool can resolve commits.
Use that same revision for all source files.
For a branch URL, keep the supplied branch.
For a repository URL without a branch, use its default branch.

Read [manifest.json](manifest.json) from that revision.
The manifest contains the source path and SHA-256 digest for each file.
Download only the listed files for the selected version.
The permitted destination names are:

- `AGENTS.md`
- `Start Here.md`
- `_setup.md`
- `About This Folder.md`
- `CLAUDE.md`, for the Claude version only.

Reject unexpected names, absolute destination paths, and parent-directory paths.
Require each source path to match `{version}/AI Memory/{name}` in this same repository revision.
Do not follow symbolic links in the destination.
Do not run repository code to install a kit.
Do not install packages, plugins, or skills.
Do not copy the whole repository into the owner’s folder.

If a source read fails, report the failure before setup.
Do not replace missing files with guessed content.

## 4. Inspect an existing destination

Read the directory before you write.
If the folder is empty, continue with installation.
If the folder contains this kit, read its AGENTS.md and About Me if present.
The AGENTS.md frontmatter identifies the kit and version.
If another version or unknown files are present, ask before you combine anything.

Keep owner changes and personal notes.
Do not restore `_setup.md` when About Me records `setup_complete: true`.
If setup is complete, continue with the existing instructions.
If all starting files are present, continue the existing setup without replacement.
Do not replace an existing file merely because its digest differs from the starter.
That difference can be an owner change.

For a partial installation, compare each existing starter file with the manifest.
If all existing files match, add only missing starter files.
Do this only when the folder has no personal notes or setup-completion record.
If the state is unclear, ask whether to continue the existing setup or use another folder.

## 5. Write and verify

Make the destination folder if necessary.
Write only the starting files that the previous steps permit.
Compare each new file with its manifest digest.
Read AGENTS.md and Start Here from the destination.
Report the destination and the files written.

Do not create subfolders, About Me, or example personal notes during installation.
Do not connect apps, change memory controls, create routines, or enable sync.
Those actions are separate owner choices.

## 6. Start setup

If `_setup.md` exists, follow its first incomplete step.
Ask the first interview question after the folder-access check.
If setup is already complete, use the saved notes for the owner’s next task.

## Result

A new installation contains four files, or five for Claude.
It contains no subfolders.
The installed AGENTS.md contains the full growth plan and core procedures.
No later source download is required for the folder to grow.
