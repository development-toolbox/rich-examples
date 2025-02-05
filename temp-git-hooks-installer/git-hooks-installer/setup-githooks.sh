#!/bin/bash

# Script: setup-githooks.sh
# Description: Setup git hooks and copy the scripts directory to $REPO_ROOT/scripts.

# Step 1: Get the repository root directory
REPO_ROOT=$(git rev-parse --show-toplevel)
if [ $? -ne 0 ]; then
    echo "❌ Error: Not inside a Git repository."
    exit 1
fi

# Step 2: Locate the script's directory
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Step 3: Define the source directories
HOOKS_SRC="$SCRIPT_DIR/git-hooks"
SCRIPTS_SRC="$SCRIPT_DIR/scripts"

# Step 4: Validate the source directories
if [ ! -d "$HOOKS_SRC" ]; then
    echo "❌ Error: Hook source directory '$HOOKS_SRC' does not exist."
    exit 1
fi

if [ ! -d "$SCRIPTS_SRC" ]; then
    echo "❌ Error: Scripts source directory '$SCRIPTS_SRC' does not exist."
    exit 1
fi

# Step 5: Define the target directories
HOOKS_DIR="$REPO_ROOT/.git/hooks"
SCRIPTS_DEST="$REPO_ROOT/scripts"

# Step 6: Ensure the target directories exist
mkdir -p "$HOOKS_DIR"
mkdir -p "$SCRIPTS_DEST"

# Step 7: Copy hooks to .git/hooks
cp "$HOOKS_SRC"/* "$HOOKS_DIR" || {
    echo "❌ Error: Failed to copy hooks."
    exit 1
}

# Step 8: Copy the entire scripts directory to $REPO_ROOT/scripts
cp -r "$SCRIPTS_SRC/"* "$SCRIPTS_DEST/" || {
    echo "❌ Error: Failed to copy scripts."
    exit 1
}

# Step 9: Make hooks and scripts executable
chmod +x "$HOOKS_DIR/"* || {
    echo "❌ Error: Failed to set hooks as executable."
    exit 1
}
chmod -R +x "$SCRIPTS_DEST" || {
    echo "❌ Error: Failed to set scripts as executable."
    exit 1
}


# Step 10 & 11: Check if source and destination differ and stage changes only if needed
if diff -r "$SCRIPTS_SRC" "$SCRIPTS_DEST" >/dev/null 2>&1; then
    echo "✅ Git hooks and scripts are already up-to-date. No changes detected, skipping commit."
else
    # Stage changes only if there are differences
    git add "$SCRIPTS_DEST"

    # Double-check if changes are staged before committing
    if git diff --cached --quiet "$SCRIPTS_DEST"; then
        echo "✅ Changes detected but no modifications staged. Skipping commit."
    else
        # Commit the changes if modifications are staged
        git commit -m "chore(setup-githooks.sh): Successfully installed git hooks and committed scripts

- Installed git hooks to the .git/hooks directory (not tracked in the repository).
- Added and committed the scripts directory for git hook management.
- Prevented accidental commits of other manually staged files outside the intended scope."
        echo "✅ Git hooks installed to '$HOOKS_DIR' (not tracked in repository)."
        echo "✅ Scripts have been added to '$SCRIPTS_DEST' and committed successfully!"
    fi
fi
