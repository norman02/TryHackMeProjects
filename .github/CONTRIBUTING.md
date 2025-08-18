# Contributing – TryHackMeProjects

Default branches (`main`, legacy `master`) are protected by a GitHub Ruleset. All changes land via PR with passing checks and linear history.

## Workflow
1. `git checkout -b feature/<scope>-<desc>`
2. Commit in small chunks (Conventional Commits: feat/fix/docs/chore)
3. Push and open a PR (one topic per PR)
4. Wait for CI to pass; address review
5. Squash & merge

## Required Checks (Ruleset)
- CI / ShellCheck
- CI / Python Lint
- (Add CodeQL if enabled)

## Run CI Manually
Workflows support `workflow_dispatch`:
```bash
gh workflow run "CI"
