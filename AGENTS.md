# AGENTS.md

Instructions for AI coding agents (OpenCode, Freebuff/Codebuff, Hermes workers, and others). Humans: see [CONTRIBUTING.md](CONTRIBUTING.md).

## Project

- **What it is:** replace with one sentence.
- **Stack:** replace (language, framework, runtime).
- **Run locally:** open `index.html` in a browser, or `npx serve .` for a static server (this is a static Pages portal — no container).
- **Health check:** `GET /healthz` must return 200.

## Commands

| Task | Command |
| --- | --- |
| Build image | `docker build .` |

| Lint markdown | `markdownlint-cli2 "**/*.md"` |
| Scan for secrets | `gitleaks detect --redact --no-banner` |


## Rules

1. Work on a branch named `agent/<task>`. Never push to `main`. Open a pull request.
2. Commit messages use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
3. Never read, print, or commit secrets. Do not open `.env` files. Use `.env.example` for documentation.
4. This is a static portal: no runtime server, no container binding.
5. Screenshots use demo data only. No real hostnames, IPs, usernames, emails, school or client names.
6. Do not invent facts. If a command, flag, or API is unverified, check the official docs or ask.
7. Verify before reporting done: run the build, run the tests, open the page. Paste real output.
8. Ask before: creating releases or tags, changing repo visibility, deleting files outside your task, or adding dependencies with a network-heavy footprint.

## Style

- Match the existing code style. `.editorconfig` is authoritative.
- README voice: calm, direct, specific. No hype, no filler.
- Design language for any UI: background `#0a0a09`, accent `#FFB300`, font JetBrains Mono.

## Skills

Reusable procedures live in `.agents/skills/`: `repo-polish`, `readme-writer`, `dockerize`, `screenshot-capture`, `security-scrub`, `pr-workflow`, `release-checklist`. Load the one that matches your task.
