# User Story Example: Bulk Image Upload with Resizing

This file documents a detailed **user story** for implementing a bulk image upload feature using the **Conventional Commits** standard and the automated commit log system.

👉 **For the full project overview and commit log structure, refer to the [main branch README](../README.md).**

---

## ✅ Scenario Overview
Johan wants to introduce a **bulk image upload feature** that:  
- Allows users to upload multiple image files simultaneously.  
- Automatically resizes large images to optimize performance.  
- Prevents crashes caused by unsupported image formats.  

---

## ✅ Workflow: Multiple Branches Example

This user story is implemented using a **multi-branch workflow** to keep tasks organized and separated.

---

### **Branch 1:** `feature/bulk-upload`
**Goal:** Implement the core bulk upload feature and image resizing support.

```bash
# Create a feature branch from main
git checkout -b feature/bulk-upload

# Work completed: Bulk upload and resizing implemented
vim bulk_upload.py
vim tests/test_bulk_upload.py

# Stage only specific files
git add bulk_upload.py tests/test_bulk_upload.py

# Commit with a Conventional Commit message
git commit -m "feat(upload): implement bulk image upload with resizing

- Added bulk image upload for handling multiple file inputs.
- Implemented image resizing support for optimization.
- Included unit tests covering bulk upload functionality."

# Push the branch
git push origin feature/bulk-upload
```

---

### **Branch 2:** `fix/upload-bug`
**Goal:** Prevent application crashes on unsupported image formats.

```bash
# Create a bugfix branch from feature/bulk-upload
git checkout -b fix/upload-bug feature/bulk-upload

# Work completed: Added validation and improved error handling
vim bulk_upload.py
vim tests/test_bulk_upload.py

# Stage the changes
git add bulk_upload.py tests/test_bulk_upload.py

# Commit with a detailed Conventional Commit message
git commit -m "fix(upload): prevent crash on unsupported file types

- Added validation for unsupported image formats.
- Improved error handling for clear feedback messages.
- Updated tests to cover invalid formats."

# Push the bugfix branch
git push origin fix/upload-bug
```

---

### **Branch 3:** `docs/update-readme`
**Goal:** Update the documentation to reflect the new feature and bugfix.

```bash
# Create a documentation branch
git checkout -b docs/update-readme

# Work completed: Updated README to describe the feature and error handling
vim README.md

# Stage and commit changes with Conventional Commits
git add README.md
git commit -m "docs(readme): update instructions for bulk upload feature

- Added instructions for the bulk upload and image resizing feature.
- Clarified error handling and invalid file validation updates.
- Expanded test coverage explanations."

# Push the documentation branch
git push origin docs/update-readme
```

---

## ✅ Commit Log Example

### **Commit Log for Branch: `feature/bulk-upload`**
This file provides a summary of all commits in the `feature/bulk-upload` branch.  
Each commit links to its detailed log.

```markdown
# Commit Log for Branch: `feature/bulk-upload`

This file provides a summary of all commits in the branch `feature/bulk-upload`.  
Each commit links to its detailed log.

| Commit Hash | Date       | Author       | Message           |
|-------------|------------|--------------|-------------------|
| [a1b2c3d4](./a1b2c3d4.md) | 2025-01-10 | Johan Sörell | feat(upload): implement bulk image upload with resizing |
| [b3c4d5e6](./b3c4d5e6.md) | 2025-01-11 | Johan Sörell | refactor(upload): optimize image resizing logic |
| [c5d6e7f8](./c5d6e7f8.md) | 2025-01-12 | Johan Sörell | fix(upload): improve error handling for invalid formats |
```

---

## ✅ Example Detailed Commit Log (`docs/commit-logs/feature/bulk-upload/a1b2c3d4.md`)

```markdown
# Commit Log

---

## Commit Details

- **Commit Hash:**   `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`
- **Branch:**        `feature/bulk-upload`
- **Author:**        Johan Sörell
- **Date:**          2025-01-10 14:32:00 +0100
- **Message:**

  feat(upload): implement bulk image upload with resizing

  - Added bulk image upload for handling multiple file inputs.
  - Implemented image resizing support for performance optimization.
  - Included unit tests covering bulk upload scenarios.

---

## Changed Files:

- `A  bulk_upload.py`
- `A  tests/test_bulk_upload.py`
```

---

## ✅ Commit Log Styling Reference

This project adheres to the **Conventional Commits** standard and the **commit log structure** described in the primary project `README.md`.

👉 **For detailed instructions on the commit log structure and usage, refer to the** [README.md](../README.md).

---

## ✅ Best Practices for Commit Messages
- **Scope Matters:** Use a relevant scope (`feat(upload)` instead of just `feat`).  
- **Avoid Vague Messages:** Each commit message should explain **what** and **why**.  
- **Stage Selectively:** Avoid `git add .`; stage only the necessary files.  
- **Separate Concerns:** Use separate branches for features, bug fixes, and documentation.  

---

## ✅ Installation Instructions

```bash
git clone https://github.com/development-toolbox/development-toolbox-core.git
cd development-toolbox-core
./scripts/install_post_commit_hook.sh
```

---

## ✅ Maintained by:
- **Johan Sörell**  
- **GitHub:** [J-SirL](https://github.com/J-SirL)  
- **LinkedIn:** [Johan Sörell](https://se.linkedin.com/in/johansorell)  
```

