# Reflect

**When:** once a week, you say "reflect". Friday works well.
**Who approves:** you
**Status:** ready to try

Your assistant looks back over the week, writes a short week note, updates your notes, and tidies up. It shows you every change before making it. About 20 minutes.

## Steps (for the assistant)

1. **Read the week, newest first.** This week's notes in Log/Daily, starting with today and going back to Monday. Then this week's notes in Log/Meetings. Then anything in Inbox. Then the "Next week" list in last week's note in Log/Weekly.
2. **Draft the week note.** Make "Log/Weekly/Week of [Monday's date].md", like "Week of 2026-10-12.md". Use these headings:
   - **What the week was about**: two or three lines.
   - **What changed**: decisions, news and finished work. Name the note each one affects.
   - **People**: who came up, anyone new, anyone you owe a reply or a follow-up.
   - **What I learned**: leave empty until step 3.
   - **Next week**: what carries over.
   - **Cleanup**: filled in at step 5.
3. **Ask a few questions, one at a time.** What's missing? What surprised you? Is anything on the list done, or no longer worth doing? Put the answers in the week note.
4. **Update the notes that own the facts.** List the exact changes you'd make to About Me, the Areas notes ("Open right now" and "Last reviewed") and the People notes ("Last talked" and notes). Ask once for the whole list. Make the changes they approve. Add a line to today's note under "Done".
5. **Clean up memory.** Do each part. If a part has nothing, say so in one line and move on.
   1. **Inbox.** For each item, suggest where it belongs: added to a note, made into a new note, or removed. Ask before removing anything.
   2. **This week's files.** Look at the files that changed this week. Point out files with " 2" at the end of the name, the same fact written in two places, notes in the wrong folder, and links that go nowhere. Suggest one fix for each.
   3. **Your assistant's own memory.** Read whatever memory you can see. In a Cowork project, that is the project's memory. Compare it with this folder:
      - True and missing from the folder: suggest adding it to the note that owns it.
      - Different from the folder: ask which is right. Fix the folder.
      - Out of date or wrong: list it so it can be removed from memory.
   4. **Claude's chat memory.** You may not be able to see it from here. Ask whether they want to check it this week. If yes, they paste Workflows/Memory Export Prompt.txt into a Claude chat and paste the answer here. Save it to Inbox, then compare it the same way as part 3. To remove something from chat memory, they can tell Claude in a chat what to forget, or edit memory in Claude's settings.
6. **The folder owns the facts.** Built-in memory is a helper. Move what's worth keeping into the folder, and prune what's stale or wrong. Ask before writing to the folder or changing any memory.
7. **First reflect of the month:** read About Me back to them and ask "Is this still you?" Update what changed.
8. **Close.** Say in two or three lines what changed this week and what's on next week's list.

## What it must not do
- Delete a file or a memory without asking.
- Send anything to anyone.
- Rewrite a note from scratch when a small change will do.
