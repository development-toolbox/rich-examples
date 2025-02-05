#!/usr/bin/env python3
# Last changes by Johan Sörell
import subprocess
import os
import sys
from datetime import datetime


def get_repo_url():
    """Automatically detect the GitHub repository URL."""
    remote_url = run_git_command(["git", "remote", "get-url", "origin"])[0]
    # Convert SSH to HTTPS if needed
    if remote_url.startswith("git@"):
        repo_url = remote_url.replace(":", "/").replace("git@", "https://").replace(".git", "")
    else:
        repo_url = remote_url.replace(".git", "")
    return repo_url

def run_git_command(command):
    """Run a git command and return the output."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip().splitlines()

def get_repo_root():
    """Get the root of the current git repository."""
    return subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()

def get_branches():
    """Fetch all branches with latest commit."""
    return run_git_command(["git", "branch", "--all", "--format=%(refname:short) | %(objectname:short) | %(authorname)"])

def get_tags():
    """Fetch all tags with commit hash and messages."""
    return run_git_command(["git", "tag", "--sort=-taggerdate", "--format=%(refname:short) | %(objectname:short) | %(taggerdate)"])

def get_pull_requests():
    """Simulating PR fetching. Real PRs require GitHub API integration."""
    return run_git_command(["git", "log", "--grep=Merge pull request", "--pretty=format:%h | %s | %ad", "--date=iso"])

def get_commits():
    """Fetch the latest commits with exact date and time."""
    return run_git_command(["git", "log", "--all", "--pretty=format:%h | %s | %an | %ad", "--date=iso"])

def generate_git_timeline():
    branch_name = os.getenv("BRANCH_NAME")
    
    if not branch_name:
        print("❌ ERROR: Branch name not set. Exiting.")
        sys.exit(1)

    print(f"🌿 Active Branch: {branch_name}")    
    
    repo_root = get_repo_root()
    log_dir = os.path.join(repo_root, "docs", "commit-logs", branch_name)
    os.makedirs(log_dir, exist_ok=True)

    timeline_file_path = os.path.join(log_dir, "git_timeline_report.md")

    # Start generating the Markdown content
    with open(timeline_file_path, "w") as md_file:
        md_file.write("# 📊 Git Commit Timeline\n\n")
        md_file.write(f"> **Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        md_file.write(f"> **Branch:** `{branch_name}`\n\n")

        # Branches Section
        md_file.write("## 📦 Branches\n| **Branch Name** | **Last Commit** | **Author** |\n|----------------|--------------|------------|\n")
        for branch in get_branches():
            md_file.write(f"| {branch} |\n")

        # Tags Section
        md_file.write("\n## 🏷️ Tags\n| **Tag** | **Commit Hash** | **Tagged On** |\n|--------|----------------|--------------|\n")
        for tag in get_tags():
            md_file.write(f"| {tag} |\n")

        # PR Section (Simulated using commit messages)
        md_file.write("\n## 🔀 Pull Requests (PRs)\n| **Commit** | **Message** | **Date** |\n|------------|-------------|---------|\n")
        for pr in get_pull_requests():
            md_file.write(f"| {pr} |\n")

        # Commits Section
        md_file.write("\n## 📑 Commit Log\n")
        for commit in get_commits():
            hash, message, author, date = commit.split(" | ")
            repo_url = get_repo_url()
            md_file.write(f"### ✅ Commit: [{hash}]({repo_url}/commit/{hash})\n")
            md_file.write(f"- **Date:** {date}\n- **Author:** {author}\n- **Message:** {message}\n\n")

        md_file.write("\n## ✅ Summary\n- **Here you can put a summary if you like.**\n- **PR and MR inclusion (simulated).**\n")

    # ✅ Stage and Commit the Timeline File
    subprocess.run(["git", "add", timeline_file_path], check=True)
    commit_hash = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    commit_message = f"Update commit timeline: {commit_hash}"

    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"📈 Git Timeline Updated for branch: {branch_name}")
        print(f"✅ Timeline report generated: {timeline_file_path}")
    except subprocess.CalledProcessError:
        print("⚠️ No changes detected. Skipping commit.")

if __name__ == "__main__":
    generate_git_timeline()
