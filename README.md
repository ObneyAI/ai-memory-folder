# AI Memory Folder

A starter kit for a personal AI assistant with memory you own. Your notes live in one folder on your computer. Any AI tool that can open the folder can read them.

Made by [obney.ai](https://obney.ai) for the Personal AI Assistant workshop.

## What's in the kit

| Path | What it is |
|---|---|
| `AI Memory/` | The folder you keep. Copy this one. |
| `AI Memory/Start Here.md` | Plain-language guide for the owner |
| `AI Memory/AGENTS.md` | The one instructions file for any assistant |
| `AI Memory/CLAUDE.md` | Points to AGENTS.md. Nothing else. |
| `AI Memory/Workflows/` | Interview Me, Morning Check, Save Meeting Notes, Reflect, plus two copy-and-paste prompts |
| `AI Memory/Templates/` | Daily Note, Meeting Note, Person, Organization, About Me, Area, Workflow |
| `Setup/` | Text to paste into Claude's settings, and a note about sync for later |
| `Skills/` | Optional. Two small skills that give you `/reflect` and `/interview-me` |

## Set it up (about 15 minutes)

1. **Get the kit.** On GitHub, press the green **Code** button, then **Download ZIP**. Open the ZIP.
2. **Move the folder.** Drag `AI Memory` into your Documents folder. If your Documents folder already syncs to iCloud or OneDrive, that is your one sync tool. Don't add another. See `Setup/Later - Sync.md`.
3. **Make a Cowork project.** Open the Claude desktop app. In Cowork, open **Projects**, press **+**, and choose **Use an existing folder**. Pick your `AI Memory` folder.
4. **Point the project at the instructions.** Paste the line from `Setup/Cowork Project Instruction.txt` into the project's Instructions.
5. **Tell Claude chat about the folder.** Paste the text from `Setup/Claude Custom Instruction.txt` into **Settings**, under **Instructions for Claude**.
6. **Optional: add the skills.** In the Claude app, open **Customize**, then **Skills**, and upload `Skills/reflect.zip` and `Skills/interview-me.zip`. You can skip this. The same phrases work without them.
7. **Start.** In your AI Memory project, say **"interview me"**.

## How it works

- **The folder owns the facts.** Claude's built-in memory is a helper. The weekly Reflect moves what's worth keeping into the folder and prunes the rest.
- **One instructions file.** AGENTS.md holds the rules. CLAUDE.md and the Cowork project instruction only point to it. Two full copies drift apart.
- **Workflows are notes.** Each one is a plain-language note in `Workflows/`. The skills only point to those notes, so there's one version of each.
- **Nothing goes out without a yes.** The assistant drafts. The owner approves.

## For whoever maintains this kit

- Keep the kit free of anyone's real content. Client copies are made from it, never the other way around.
- People copy the folder once. Their copy is not connected to this repo, and shouldn't be.
- After editing a skill, rebuild its ZIP: `cd Skills && zip -r reflect.zip reflect`.
- Write for a non-technical owner: short sentences, plain words, no em dashes.
