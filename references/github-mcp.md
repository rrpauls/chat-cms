# GitHub MCP Reference

Load only for repository write operations.

Chat CMS uses the environment's GitHub MCP/connector/integration as the repository control surface. Exact tool names vary.

## Required capabilities

A normal write transaction needs equivalent operations for:

- read repository/default branch/files;
- create task branch;
- create/update files on that branch;
- inspect diff;
- create PR;
- inspect CI/checks;
- merge PR;
- inspect deployment/workflow state.

If a required capability is unavailable, stop and report it. Do not fall back to direct `main` edits.

## Minimal flow

1. Resolve configured repository and current default-branch head.
2. Create a concise task branch from that head.
3. Fetch every existing text/data file before changing it.
4. Apply only profile-authorized writes.
5. Upload binary media only to profile-authorized directories.
6. Compare branch against default branch.
7. Validate changed files and, where applicable, exact writable regions/semantic keys.
8. Open a PR with a short factual title/body.
9. Confirm required checks pass.
10. Merge using the repository's normal mechanism.
11. Confirm configured deployment starts and completes.
12. Verify the target site when web access exists.

## Never

- request/store GitHub passwords, PATs, SSH keys, or secrets in chat;
- force-push;
- bypass required checks;
- broaden the whitelist because a tool is inconvenient;
- repair unrelated CI/workflow/server code under a content-only profile;
- claim deployment success from a commit/merge alone.
