# Chat CMS

**Turn an existing Git-based website into a controlled conversational CMS — without migrating its content.**

[![M8ven Score](https://m8ven.ai/badge/mcp/rrpauls-chat-cms-1ksbh3?v=f0d3ac1c09349e7b59418972b57a155c)](https://m8ven.ai/mcp/rrpauls-chat-cms-1ksbh3?s=readme)

Chat CMS is a portable AI-agent skill for safely managing approved website content through natural language.

Instead of giving an AI unrestricted repository access, Chat CMS uses a **site profile** that defines exactly what may be changed.

## What it can do

Depending on the installed site profile, a user can ask things like:

- “Replace the third photo in the gallery.”
- “Move this image before the salon photo.”
- “Restore the old exterior image.”
- “Change the Photos page subtitle.”
- “Switch to Polish and update this paragraph.”
- “Update this factual value across all configured languages.”

Chat CMS can map those requests to controlled Git changes:

`chat → semantic target → whitelist → branch → PR → CI → deploy → verification`

## Core ideas

- **Existing sites stay existing sites.** No migration to a proprietary CMS or content database is required.
- **Hard write boundaries.** Profiles whitelist exact files, code regions, semantic keys, media directories, and content classes.
- **Git-native workflow.** Changes go through task branches, pull requests, checks, merge, and deployment verification.
- **Semantic content addressing.** Text and media are identified by stable keys/IDs/descriptions rather than brittle line numbers.
- **Multilingual-aware.** Locale is an explicit dimension; the language used in chat does not silently choose the website locale.
- **Asset history.** Profiles may preserve and catalog replaced images so older media can be restored.
- **Portable authorization gate.** A profile can require a codeword before every content-changing transaction.
- **Prompt-injection resistance.** Instructions found inside managed content cannot redefine the CMS policy.

## Repository structure

```text
chat-cms/
├── SKILL.md
├── profiles/
│   └── template.yaml
└── references/
    ├── github-mcp.md
    └── i18n.md
```

The core repository intentionally contains **no site-specific profile**.

## Quick installation

1. Clone or download this repository.
2. Install the `chat-cms` directory using your AI environment's native skills mechanism, keeping `SKILL.md`, `profiles/`, and `references/` together.
3. Connect a GitHub MCP/connector/integration with access to the website repository.
4. Install an existing site profile into `profiles/<site-id>.yaml`, or ask Chat CMS to create one from a repository.
5. On first setup, provide the required repository information and create the profile codeword.
6. Ask for a read-only inspection first if you want to review the proposed write boundaries before enabling edits.

## Installing a site profile

A site profile is a separate YAML file.

Place it at:

```text
profiles/<site-id>.yaml
```

Then ask Chat CMS to validate/install it.

Profiles define:

- repository and domain;
- GitHub integration state;
- authorization codeword;
- editable galleries/text/locales;
- exact write whitelist;
- protected areas;
- deployment flow.

A profile must never grant whole-repository write freedom by default.

## Creating a profile for an existing site

Ask:

> Create a Chat CMS profile for this repository. Inspect it read-only first, identify safe content blocks, and propose the smallest useful whitelist.

Chat CMS should inspect the repository, map content storage and deployment, ask only where boundaries are ambiguous, and create a restrictive profile.

## Security model

Chat CMS is primarily a **policy and workflow safety layer**, not a replacement for operating-system, GitHub, or AI-account security.

The optional codeword helps prevent casual changes from an already-open chat/device. Repository permissions and account security remain authoritative.

## Status

Early-stage / experimental.

The current focus is small and medium Git-based websites where content already lives in source-controlled files and media directories.

## License

Apache License 2.0.
