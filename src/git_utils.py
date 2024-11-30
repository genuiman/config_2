import subprocess
from datetime import datetime

def get_commits_after_date(repo_path, commit_date):
    result = subprocess.run(
        ['git', 'log', '--since', commit_date.strftime('%Y-%m-%d'), '--pretty=format:%H'],
        cwd=repo_path, capture_output=True, text=True
    )
    return result.stdout.splitlines()

def get_commit_messages(repo_path, commits):
    messages = {}
    for commit in commits:
        result = subprocess.run(
            ['git', 'log', '-n', '1', '--pretty=format:%s', commit],
            cwd=repo_path, capture_output=True, text=True
        )
        messages[commit] = result.stdout.strip()
    return messages

def get_linear_dependencies(repo_path, commits):
    dependencies = {}
    previous_commit = None
    for commit in commits:
        if previous_commit:
            dependencies[commit] = [previous_commit]
        previous_commit = commit
    return dependencies
