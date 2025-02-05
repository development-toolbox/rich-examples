# git-hooks-installer: Commit Log System

This project uses an **automated commit logging system** that **follows** the **Conventional Commits** standard. This ensures all changes are clearly recorded, easy to understand, and simple to track.  

---

## ✅ Overview

The commit log system automatically generates detailed commit logs after every commit, ensuring that all changes can be traced and reviewed with clarity. It uses **Conventional Commits** to standardize commit messages, making the history easier to navigate and automate.

### 📖 What Are Conventional Commits?

**Conventional Commits** is a standard that provides a simple way to write clear commit messages. It helps keep projects organized and makes it easier to automate things like changelogs, version updates, and release notes.

👉 **Learn more at:** [https://www.conventionalcommits.org](https://www.conventionalcommits.org)

---

## Commit Log Structure

After each commit, a detailed commit log is generated in the `docs/commit-logs` directory, sorted by branch. Each log file is named using the commit hash for traceability.

### Example Structure
```plaintext
docs/
└── commit-logs
    ├── main
    │   ├── 305f3093.md
    │   ├── 8d917eb1.md
    │   └── README.md
    └── commit-log-system-readme.md
```

---

## ✅ Conventional Commits Guide

This project follows the **Conventional Commits** standard for clarity and automation in version control.

### Commit Message Format
```plaintext
<type>(optional scope): <description>

[optional body]

[optional footer(s)]
```

### Commit Types with Examples
- **`feat(scope)`** – Adding a new feature.  
   *Example:* `feat(upload): add bulk image upload feature with drag-and-drop support`

- **`fix(scope)`** – Fixing a bug.  
   *Example:* `fix(storage): correct file reference bug in image processing`

- **`docs(scope)`** – Updating documentation.  
   *Example:* `docs(readme): add example usage for commit process`

- **`refactor(scope)`** – Code changes without functional impact.  
   *Example:* `refactor(core): simplify data validation logic`

- **`style(scope)`** – Code style changes (e.g., formatting).  
   *Example:* `style(css): standardize indentation in style.css`

- **`chore(scope)`** – Maintenance tasks like dependency updates.  
   *Example:* `chore(deps): upgrade pytest to version 7.2.0`

- **`test(scope)`** – Adding or updating tests.  
   *Example:* `test(image-processing): add unit tests for resize feature`

---

## ✅ Usage

This commit log system automates the process of recording all commit activity. Below is a **step-by-step** guide for making a professional commit using **Conventional Commits**.

### Example Workflow:
1. **Stage Your Changes**  
   Add your modified files to the staging area:
   ```bash
   git add <file-name>
   ```

2. **Check the Changes (Optional)**  
   Verify the staged files before committing:
   ```bash
   git status
   git diff --staged
   ```

3. **Commit the Changes (Using Conventional Commits)**  
   Use a properly formatted commit message:
   ```bash
   git commit -m "feat(upload): add bulk image upload with drag-and-drop support"
   ```

4. **Verify the Commit Log (Optional)**  
   Check the auto-generated commit log located under `docs/commit-logs`:
   ```bash
   ls docs/commit-logs/main
   ```

5. **Push the Changes**  
   Push the commit to your remote repository:
   ```bash
   git push origin <branch> 
   # or just do git push if you like 
   ```

### Example with Auto-Push Enabled (`GIT_AUTO_PUSH`)
```bash
GIT_AUTO_PUSH=true git commit -m "chore(hooks): enable auto-push for commit logging"
```

---

## ✅ Parameters

The commit log system uses the following parameter for additional customization:

- **`GIT_AUTO_PUSH`** – Controls whether commit logs are automatically pushed after each commit.

### Default Behavior:
- If **`GIT_AUTO_PUSH`** is **not set**, it defaults to `false` (no auto-push).
- To enable automatic pushing, set `GIT_AUTO_PUSH=true` before committing.

### Example Usage:
```bash
# Enable auto-push for a single commit
GIT_AUTO_PUSH=true git commit -m "chore(hooks): enable auto-push for commit logging"

# Disable auto-push (default behavior)
git commit -m "docs: update README with clearer parameter explanation"
```
---

## ✅ Installation

Ensure you have the following dependencies installed:

- `git`

### Steps to Install:

```bash
# Clone the repository
git clone https://github.com/development-toolbox/development-toolbox-core.git
cd development-toolbox-core

# Install the commit log system (automatically adds the post-commit hook)
./scripts/install_post_commit_hook.sh
```

---

## ✅ Changed Files Explained

The **Changed Files** section in the commit log uses standard Git status codes:

- **R** – Renamed file
- **096** – Similarity index (96% similarity with the original file)
- **A** – Added file
- **D** – Deleted file
- **M** – Modified file

---

## ✅ How the Commit Log System Works

The commit log system is managed by a `post-commit` hook located in `.git/hooks/post-commit`. The process works as follows:

1. **Marker File Check:** Prevents recursive execution using a marker file.
2. **Commit Information Collection:** Gathers commit hash, message, author, date, and branch details.
3. **Changed Files Detection:** Captures a list of modified files and their statuses using `git diff`.
4. **Log Generation:** Writes a structured commit log to `docs/commit-logs`.
5. **Automatic Push (Optional):** If the `GIT_AUTO_PUSH` variable is enabled, the log will be committed and pushed automatically.

---

## ✅ Contributing

Contributions are welcome! Please ensure all commit messages follow the **Conventional Commits** standard described above. For larger changes, consider opening a discussion issue first.

---

## ✅ Maintained by

- **Johan Sörell**  
- **GitHub:** [J-SirL](https://github.com/J-SirL)  
- **LinkedIn:** [Johan Sörell](https://se.linkedin.com/in/johansorell)  

The original `git-hooks-installer` files used in this system are located in the [development-toolbox-core](https://github.com/development-toolbox/development-toolbox-core) repository.
