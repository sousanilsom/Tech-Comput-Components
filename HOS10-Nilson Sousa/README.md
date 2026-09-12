# HOS10A: MongoDB Atlas

## How to finish this

1. Take a screenshot.
2. Save it into `screenshots/` using the filename from the list below.
3. Run:

```
python3 rebuild_doc.py
```

The document is rebuilt with every screenshot it can find placed in the right
spot with a caption underneath. Anything still missing stays an orange
placeholder box, and the script prints exactly what it is still waiting for.
Run it as many times as you like.

On a Mac, `Cmd+Shift+4` then space captures a single window.

## Filenames

| File | What it should show |
|---|---|
| `s01-codespace.png` | The running GitHub Codespace with the course repo |
| `s02-atlas-signup.png` | The Atlas sign up page |
| `s03-atlas-welcome.png` | Verified account and welcome questionnaire |
| `s04-create-deployment.png` | Deploy screen, Free tier, AWS, Oregon |
| `s05-database-user.png` | Database Access, showing `nilsonalvessousa_db_user` |
| `s06-ip-access-list.png` | IP Access List with both entries Active |
| `s07-vscode-extension.png` | MongoDB for VS Code installed in the codespace |
| `s08-connect-string.png` | Atlas Connect dialog with the VS Code string |
| `s09-paste-string.png` | Connection string pasted into the codespace prompt |
| `s10-connected.png` | Successful connection to the cluster |
| `s11-playground-saved.png` | `hos10.mongodb.js` under PLAYGROUNDS |
| `step01.png` … `step23.png` | Playground Result pane for each of the 23 steps |
| `s12-source-control.png` | Source Control panel with the commit message |
| `s13-pushed-commit.png` | The pushed commit on GitHub |

`.jpg` works too, the script accepts either.

## What is already done

**Atlas**, cluster `CS11A`, Free tier, AWS Oregon (us-west-2), MongoDB 8.0.32.
Database user `nilsonalvessousa_db_user` with `atlasAdmin@admin`. IP access list
has the Auto Setup entry plus `0.0.0.0/0` so a codespace can connect.

**The document** has all eight sections written, with every Section 7 command
explained and its real output already included. The outputs are genuine: every
command in `dbserver/hos10.mongodb.js` was executed against a MongoDB 7 server
and the results captured in `mongodb-results.txt`.

## What is left

In the codespace: install the MongoDB for VS Code extension, add the connection
using the Atlas string with the real password, create a playground saved as
`HOS10/dbserver/hos10.mongodb.js`, paste in the file from `dbserver/`, and run
the 23 steps one at a time.

## Security note

`0.0.0.0/0` opens the cluster to every address on the internet. Delete that
entry when the course is over.

## Other files

| File | What it is |
|---|---|
| `dbserver/hos10.mongodb.js` | The playground file, 23 steps |
| `mongodb-results.txt` | Raw verified output, the source for the document |
| `rebuild_doc.py` | Regenerates the document |
