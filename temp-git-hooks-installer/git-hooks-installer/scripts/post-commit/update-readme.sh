#!/bin/bash
# Update branch-specific README.md with commit logs

set -e  # Exit immediately if any command fails

# ✅ Kontrollera att branch-namnet är definierat
if [ -z "$BRANCH_NAME" ]; then
  echo "ERROR: Branch name not set. Exiting."
  exit 1
fi

# ✅ Kontrollera att repo root är satt
if [ -z "$REPO_ROOT" ]; then
  REPO_ROOT=$(git rev-parse --show-toplevel)
fi

# ✅ Navigera till repo root
cd "$REPO_ROOT" || { echo "ERROR: Could not navigate to repository root"; exit 1; }

# ✅ Definiera kataloger
LOG_DIR="$REPO_ROOT/docs/commit-logs/$BRANCH_NAME"
README_FILE="$LOG_DIR/README.md"

# ✅ Kontrollera om loggmappen finns
if [ ! -d "$LOG_DIR" ]; then
  echo "ERROR: Log directory $LOG_DIR does not exist. Skipping README update."
  exit 1
fi

# ✅ Aktivera nullglob för att hantera tomma kataloger
shopt -s nullglob

# ✅ Rensa tidigare README.md
> "$README_FILE"

# ✅ Generera README-header
{
    echo "# Commit Log for Branch: \`$BRANCH_NAME\`"
    echo
    echo "This file provides a summary of all commits in the branch \`$BRANCH_NAME\`."
    echo "Each commit links to its detailed log."
    echo
    echo "### 📈 [View Full Git Timeline](./git_timeline_report.md)"
    echo
    echo "| Commit Hash | Date & Time       | Author       | Message           |"
    echo "|-------------|------------------|--------------|-------------------|"
} >> "$README_FILE"

# ✅ Samla in commit-detaljer
commit_entries=()

for log_file in "$LOG_DIR"/*.md; do
    # Exkludera README och git_timeline_report.md
    if [[ "$log_file" == *"README.md" || "$log_file" == *"git_timeline_report.md" ]]; then
        continue
    fi

    # Hämta commit-detaljer direkt från Git
    COMMIT_HASH=$(basename "$log_file" .md)
    COMMIT_DATE=$(git show -s --format="%ad" --date=format:'%Y-%m-%d %H:%M' "$COMMIT_HASH")
    COMMIT_AUTHOR=$(git show -s --format="%an" "$COMMIT_HASH")
    COMMIT_MESSAGE=$(git show -s --format="%s" "$COMMIT_HASH")

    # Lägg till i listan
    commit_entries+=("$COMMIT_DATE|$COMMIT_HASH|$COMMIT_AUTHOR|$COMMIT_MESSAGE")
done

# ✅ Sortera commits efter datum (senaste först)
IFS=$'\n' sorted_commits=($(sort -r <<<"${commit_entries[*]}"))
unset IFS

# ✅ Skriv tabellen i README.md
for entry in "${sorted_commits[@]}"; do
    IFS='|' read -r COMMIT_DATE COMMIT_HASH COMMIT_AUTHOR COMMIT_MESSAGE <<< "$entry"
    echo "| [$COMMIT_HASH](./$COMMIT_HASH.md) | $COMMIT_DATE | $COMMIT_AUTHOR | $COMMIT_MESSAGE |" >> "$README_FILE"
done

# ✅ Bekräftelse
echo "✅ README.md has been generated and updated: $README_FILE"

# ✅ Stage README.md för commit
if ! git add "$README_FILE"; then
  echo "ERROR: Failed to stage $README_FILE"
  exit 1
fi

echo "✅ README.md successfully added for commit."
