# CLAUDE.md

This file provides guidance to AI assistants (Claude Code and others) when working in this repository. Keep this document updated as the project evolves.

---

## Repository Overview

**Remote:** `gsaenzmartinez-design/TESTING`
**Primary development branch:** `claude/add-claude-documentation-Ywu48`

This repository is currently in its initial state. Update this section with a description of the project's purpose, tech stack, and high-level architecture once the codebase is established.

---

## Development Branch Requirements

- All development work goes on the designated feature branch. **Never push directly to `main` or `master`** without explicit permission.
- Create the branch locally if it does not yet exist:
  ```bash
  git checkout -b <branch-name>
  ```
- Push with tracking:
  ```bash
  git push -u origin <branch-name>
  ```

---

## Git Workflow

### Commits
- Write clear, descriptive commit messages in the imperative mood (e.g., "Add user authentication module").
- Keep commits focused — one logical change per commit.
- Never skip pre-commit hooks (`--no-verify`) unless explicitly instructed.
- Never amend published commits. Create a new commit instead.
- Do not commit secrets, credentials, or large binary files.

### Pull Requests
- Do **not** open a pull request unless the user explicitly requests one.
- PR titles must be under 70 characters.
- PR body must include a summary and a test plan.

---

## Project Structure

> **Note:** This repository is currently empty. Populate this section as source files are added.

```
TESTING/
├── CLAUDE.md                      # This file
├── .claude/
│   └── agents/
│       └── asesor-fiscal.md       # Subagente "asesor fiscal" (fiscalidad española)
└── .git/
```

Update this tree whenever significant new directories or files are introduced.

---

## Tech Stack

> To be documented as the project is built out.

List the primary language(s), frameworks, package manager, test runner, linter, and formatter here.

---

## Setup & Installation

> To be documented once dependencies are introduced.

Typical setup commands to include here:
```bash
# Install dependencies
# e.g., npm install / pip install -r requirements.txt / cargo build

# Copy and configure environment variables
# cp .env.example .env

# Run the development server
# e.g., npm run dev
```

---

## Environment Variables

> To be documented as `.env` / config files are added.

Never commit real secrets. Use `.env.example` to document required variables with placeholder values.

---

## Running Tests

> To be documented once a test framework is chosen.

```bash
# Run all tests
# e.g., npm test / pytest / cargo test

# Run a single test file
# e.g., npm test -- path/to/file.test.ts
```

Always run tests before pushing. Do not mark a task complete if tests are failing.

---

## Linting & Formatting

> To be documented once linting tools are configured.

```bash
# Lint
# e.g., npm run lint

# Format
# e.g., npm run format
```

Fix all linting errors before committing. Do not disable linting rules without a documented reason.

---

## Code Conventions

The following conventions apply regardless of language. Update with language-specific rules as the stack is defined.

- **Clarity over cleverness:** Write code that is easy to read and reason about.
- **No speculative abstractions:** Only abstract when there are at least three concrete use cases.
- **No unused code:** Remove dead code rather than commenting it out.
- **No backwards-compatibility hacks:** If something is unused, delete it completely.
- **Minimal error handling:** Only validate at system boundaries (user input, external APIs). Trust internal code and framework guarantees.
- **No extra features:** Implement exactly what is asked for. Do not add configurability, logging, or comments beyond what the task requires.
- **Security first:** Never introduce command injection, XSS, SQL injection, or other OWASP Top 10 vulnerabilities.

---

## AI Assistant Guidelines

When working in this repository:

1. **Read before editing.** Always read a file before modifying it.
2. **Use dedicated tools.** Prefer `Read`, `Edit`, `Write`, `Grep`, and `Glob` over raw shell commands.
3. **Parallel tool calls.** Make independent tool calls in parallel to maximize efficiency.
4. **Confirm before destructive actions.** Ask before deleting files/branches, force-pushing, or resetting hard.
5. **Keep context updated.** If the project structure or conventions change significantly, update this file.
6. **Short responses.** Be concise. Use markdown formatting with file path references (`path/to/file:line_number`) when referencing code.
7. **Do not push to remote** unless the user explicitly asks.

---

## Updating This File

This document should be updated whenever:
- A new language, framework, or major dependency is introduced.
- The directory structure changes significantly.
- New test, lint, or build commands are added.
- Team conventions are established or changed.

Last updated: 2026-04-12
