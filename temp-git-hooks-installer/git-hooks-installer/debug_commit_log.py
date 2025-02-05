#!/usr/bin/env python3
"""
Debugging Script for Commit Logs
This script reads a commit log directory and extracts commit details for validation.
"""

import os
import sys
import subprocess

# Set the commit log directory
BRANCH_NAME = os.getenv("BRANCH_NAME", "main")
REPO_ROOT = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
).stdout.strip()
LOG_DIR = os.path.join(REPO_ROOT, "docs", "commit-logs", BRANCH_NAME)


def get_commit_data(commit_hash):
    """Fetch commit details using git show."""
    try:
        commit_date = subprocess.run(
            ["git", "show", "-s", "--format=%ad", "--date=format:%Y-%m-%d %H:%M", commit_hash],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        commit_author = subprocess.run(
            ["git", "show", "-s", "--format=%an", commit_hash],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        commit_message = subprocess.run(
            ["git", "show", "-s", "--format=%s", commit_hash],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        return commit_date, commit_author, commit_message
    except subprocess.CalledProcessError:
        return "N/A", "N/A", "N/A"


def debug_commit_logs():
    """Debug and print commit details from log files."""
    if not os.path.exists(LOG_DIR):
        print(f"ERROR: Log directory '{LOG_DIR}' does not exist.")
        sys.exit(1)

    print(f"\n🔎 Debugging commit logs in: {LOG_DIR}\n")

    for log_file in sorted(os.listdir(LOG_DIR)):
        # Skip non-commit files
        if log_file in ["README.md", "git_timeline_report.md"]:
            continue

        log_file_path = os.path.join(LOG_DIR, log_file)

        # Try to extract the commit hash from the file content
        try:
            with open(log_file_path, "r") as file:
                for line in file:
                    if "Commit Hash:" in line:
                        commit_hash = line.split("`")[1]
                        break
                else:
                    commit_hash = log_file.split(".")[0]  # Fallback to filename
        except Exception as e:
            print(f"Error reading file {log_file}: {e}")
            continue

        # Fetch commit details
        commit_date, commit_author, commit_message = get_commit_data(commit_hash)

        # Print results
        print(f"📌 Commit File: {log_file}")
        print(f"   - Commit Hash: {commit_hash}")
        print(f"   - Date: {commit_date}")
        print(f"   - Author: {commit_author}")
        print(f"   - Message: {commit_message}\n")


if __name__ == "__main__":
    debug_commit_logs()

