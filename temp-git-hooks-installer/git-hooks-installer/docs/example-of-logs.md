# git-hooks-installer: Branch README.md examples

## ✅ `main` Branch README.md

```markdown
# Commit Log for Branch: `main`

This file provides a summary of all commits in the `main` branch.  
Each commit links to its detailed log.  
It also summarizes and links to all other branches.

---

## ✅ Commit Summary Table (Main Branch Only)

| Commit Hash | Date       | Author       | Message           |
|-------------|------------|--------------|-------------------|
| [a1b2c3d4](./a1b2c3d4.md) | 2025-01-10 | Johan Sörell | chore(main): initial commit log structure added |
| [b3c4d5e6](./b3c4d5e6.md) | 2025-01-11 | Johan Sörell | chore(main): added post-commit hook configuration |

---

## ✅ Branches Summary

- [Feature: Bulk Upload](../feature/bulk-upload/README.md)  
- [Bug Fix: Upload Bug](../fix/upload-bug/README.md)  
- [Documentation Update](../docs/update-readme/README.md)  

👉 **For the complete commit details, refer to each branch-specific README.**
```

---

## ✅ `feature/bulk-upload` Branch README.md

```markdown
# Commit Log for Branch: `feature/bulk-upload`

This file provides a summary of all commits made in the `feature/bulk-upload` branch only.  
For the complete project details, refer to the [main branch README](../README.md).

---

## ✅ Commit Summary Table (Feature Branch Only)

| Commit Hash | Date       | Author       | Message           |
|-------------|------------|--------------|-------------------|
| [a1b2c3d4](./a1b2c3d4.md) | 2025-01-10 | Johan Sörell | feat(upload): implement bulk image upload with resizing |
| [b3c4d5e6](./b3c4d5e6.md) | 2025-01-11 | Johan Sörell | refactor(upload): optimize image resizing logic |

---

## ✅ Commit Log Example (`docs/commit-logs/feature/bulk-upload/a1b2c3d4.md`)

```markdown
# Commit Log

---

## Commit Details

- **Commit Hash:**   `a1b2c3d4`
- **Branch:**        `feature/bulk-upload`
- **Author:**        Johan Sörell
- **Date:**          2025-01-10
- **Message:**

  feat(upload): implement bulk image upload with resizing

  - Implemented bulk image upload for handling multiple file inputs.
  - Added image resizing for performance optimization.
  - Created unit tests covering bulk upload scenarios.

---

## Changed Files:
- `A  bulk_upload.py`
- `A  tests/test_bulk_upload.py`
```

---

## ✅ `fix/upload-bug` Branch README.md

```markdown
# Commit Log for Branch: `fix/upload-bug`

This file provides a summary of all commits made in the `fix/upload-bug` branch only.  
For the complete project details, refer to the [main branch README](../README.md).

---

## ✅ Commit Summary Table (Bug Fix Branch Only)

| Commit Hash | Date       | Author       | Message           |
|-------------|------------|--------------|-------------------|
| [e4f5g6h7](./e4f5g6h7.md) | 2025-01-12 | Johan Sörell | fix(upload): prevent crash on unsupported file types |

---

## ✅ Commit Log Example (`docs/commit-logs/fix/upload-bug/e4f5g6h7.md`)

```markdown
# Commit Log

---

## Commit Details

- **Commit Hash:**   `e4f5g6h7`
- **Branch:**        `fix/upload-bug`
- **Author:**        Johan Sörell
- **Date:**          2025-01-12
- **Message:**

  fix(upload): prevent crash on unsupported file types

  - Added validation to reject unsupported image formats.
  - Improved error handling to return meaningful feedback.
  - Updated tests to ensure invalid formats are covered.

---

## Changed Files:
- `M  bulk_upload.py`
- `M  tests/test_bulk_upload.py`
```

---

## ✅ `docs/update-readme` Branch README.md

```markdown
# Commit Log for Branch: `docs/update-readme`

This file provides a summary of all commits made in the `docs/update-readme` branch only.  
For the complete project details, refer to the [main branch README](../README.md).

---

## ✅ Commit Summary Table (Documentation Branch Only)

| Commit Hash | Date       | Author       | Message           |
|-------------|------------|--------------|-------------------|
| [i8j9k0l1](./i8j9k0l1.md) | 2025-01-14 | Johan Sörell | docs(readme): update instructions for bulk upload feature |

---

## ✅ Commit Log Example (`docs/commit-logs/docs/update-readme/i8j9k0l1.md`)

```markdown
# Commit Log

---

## Commit Details

- **Commit Hash:**   `i8j9k0l1`
- **Branch:**        `docs/update-readme`
- **Author:**        Johan Sörell
- **Date:**          2025-01-14
- **Message:**

  docs(readme): update instructions for bulk upload feature

  - Added step-by-step instructions for the bulk upload feature.
  - Clarified error handling and invalid file validation updates.
  - Expanded test coverage details and examples.

---

## Changed Files:
- `M  README.md`
```
