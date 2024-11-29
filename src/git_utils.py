import subprocess
from datetime import datetime

def get_commits_after_date(repo_path, commit_date):
    result = subprocess.run(
        ['git', 'log', '--since', commit_date.strftime('%Y-%m-%d'), '--pretty=format:%H'],
        cwd=repo_path, capture_output=True, text=True
    )
    return result.stdout.splitlines()

def get_commit_dependencies(repo_path, commits):
    dependencies = {}
    for commit in commits:
        result = subprocess.run(
            ['git', 'rev-list', '--parents', commit],
            cwd=repo_path, capture_output=True, text=True
        )
        parents = result.stdout.split()
        dependencies[commit] = parents[1:]
    return dependencies
