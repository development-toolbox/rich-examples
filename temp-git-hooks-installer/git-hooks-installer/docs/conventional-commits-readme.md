# Conventional Commits Guide

This project uses the **Conventional Commits** standard to ensure clarity, consistency, and better automation in version control. The goal is to create a structured commit history that improves collaboration and makes the project easier to maintain.

## Why Use Conventional Commits?
- **Consistency:** Makes commit messages easier to read and understand.
- **Automation:** Allows tools to generate changelogs and automate versioning.
- **Clarity:** Helps contributors quickly understand the purpose of each commit.

## Commit Message Format
A commit message should follow this structure:

```plaintext
<type>(optional scope): <description>

[optional body]

[optional footer(s)]
```

## Commit Types and Usage

### ✅ `feat:` (Feature)
- **Description:** Introduces a new feature.
- **Example:** `feat: add bulk image upload option`

### ✅ `fix:` (Bug Fix)
- **Description:** Fixes a bug.
- **Example:** `fix: correct image upload path error`

### ✅ `refactor:` (Code Refactoring)
- **Description:** Code changes that do not affect functionality but improve structure or readability.
- **Example:** `refactor: rename 'github-hooks' to 'git-hooks-installer'`

### ✅ `chore:` (Maintenance Tasks)
- **Description:** Changes related to build tools, dependencies, or project settings.
- **Example:** `chore: update project dependencies`

### ✅ `docs:` (Documentation)
- **Description:** Documentation changes only.
- **Example:** `docs: add README section for CI setup`

### ✅ `style:` (Code Style)
- **Description:** Formatting and style updates without functional impact.
- **Example:** `style: fix indentation issues in script`

### ✅ `test:` (Testing)
- **Description:** Adding or updating tests.
- **Example:** `test: add tests for image resizing`

### ✅ `perf:` (Performance Improvements)
- **Description:** Performance-related improvements.
- **Example:** `perf: optimize image compression speed`

### ✅ `ci:` (Continuous Integration)
- **Description:** CI/CD configurations and changes.
- **Example:** `ci: update GitHub Actions to run tests`

### ✅ `build:` (Build System)
- **Description:** Changes affecting the build system.
- **Example:** `build: migrate from npm to yarn`

### ✅ `revert:` (Reverting Changes)
- **Description:** Revert a previous commit.
- **Example:** `revert: undo commit abc123`

### ✅ `security:` (Security Fixes)
- **Description:** Security patches.
- **Example:** `security: fix XSS vulnerability in login form`

## Enforcing Conventional Commits
To enforce this standard, you can use tools like `commitlint` and `husky` for automated validation.

## Read more on Conventional commits
[Conventional Commits][conventional-commits-main-site] 

[The power of conventional commits][the-powewr-of-conv-commits]

[git gist cheat][cheat-cheat]




[cheat-cheat]: https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13
[conventional-commits-main-site]: https://www.conventionalcommits.org/
[the-powewr-of-conv-commits]: https://julien.ponge.org/blog/the-power-of-conventional-commits/
 