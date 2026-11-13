# Agent rules for Phennec

Example rules to add to `AGENTS.md` (or your client's rules) so the agent uses Phennec reliably.

- When a prompt mentions "phennec", use the Phennec MCP tools instead of searching the local workspace.
- If you work with several Phennec projects, include the project name in the first prompt and use a separate chat per project.
- For code, read files from the opened repository; use Phennec for issues, comments and documentation.
- If an answer looks outdated, start a new chat before asking again.
