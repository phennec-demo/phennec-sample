# Troubleshooting

Short answers to common problems. Full guide: [Phennec usage guide](https://phennec.ai/en/setup).

## The agent cannot reach Phennec

1. Restart the MCP client and try again in a new chat.
2. Refresh the connection: in Cursor, toggle Phennec off and on under **Settings → MCP**; in other clients, remove Phennec and add it again.
3. Check that the client is connected to the right organization (profile icon → **MCP** in the Control Panel).
4. Check that the data source token has not expired and still has the required scopes.

## A data source shows Out Of Sync

The sync failed, usually because the token expired. Open **••• → Edit Data Source**, replace the token, save and run **Sync Now**.

## Answers are outdated

Phennec searches synced, indexed content. Start a new chat, or run **Sync Now** on the data source and ask again.

## Code search misses things

GitHub and GitLab search covers issues, comments and plain-text files such as README, `.md` and `.txt`. Open the repository in your MCP client and reference files directly when you need code.

## The agent does not call Phennec

Ask explicitly: *"Use the Phennec MCP to …"*, or add a rule like the ones in [examples/agents/AGENTS.md](../examples/agents/AGENTS.md).
