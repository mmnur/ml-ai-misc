
# Declutter Your Slack Sidebar With a Single Prompt

If your Slack sidebar has turned into an endless scroll of unsorted channels, you can fix it in one shot. Paste the prompt below into Slackbot, and save it as a reusable skill so you never have to think about it again.

## The Prompt

> "Help me organize my Slack channels into sidebar sections. Don't ask me for section names or categories first — analyze my channels and propose/build the structure automatically, end-to-end.
>
> Start by checking whether I already have sections set up. If I do, work with what exists rather than starting from scratch — don't duplicate a section that already covers a topic (e.g. don't create a new "Team" section if one already exists, just add channels to it).
>
> Check my starred channels as well as my regular unsectioned "Channels" list — starred channels don't automatically show up in the standard unsectioned sweep, so call them out separately.
>
> For every unsectioned or uncategorized channel, move it into the most logical existing section — whether that section was already there or one you created earlier in this process. If a channel's name or topic doesn't clearly tell you where it belongs, check its last 5 messages to figure out its real theme before deciding — don't just guess from the name.
>
> If a channel or cluster of channels doesn't logically fit any existing section, create a new section for it yourself (with a clear name and matching emoji) rather than forcing a bad fit or asking me what to call it.
>
> If I ask you to merge two sections, combine their channels into one and delete the redundant section.
>
> After you're done, run one more check to confirm nothing is still unsectioned (channels can slip through, especially newly-joined ones) — and give me a final list of anything left uncategorized, so I can decide if it's still relevant or safe to leave as-is.
>
> At the end, give me a clear summary: which channels moved, to which section (noting whether that section was pre-existing or newly created), and flag anything placed with low confidence or left unclear/skipped."

## Why This Works

Instead of manually dragging channels around or deciding on categories yourself, the agent does the heavy lifting — it **analyzes your channels**, **respects your existing structure**, and **builds out the rest automatically**. It even peeks at recent messages when a channel name is ambiguous, so nothing gets misplaced on a guess.

Save it as a skill and re-run it whenever your sidebar starts getting messy again.

