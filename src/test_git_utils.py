import unittest
from unittest.mock import patch, MagicMock
from git_utils import get_commits_after_date, get_commit_messages, get_linear_dependencies
from datetime import datetime

class TestGitUtils(unittest.TestCase):

    @patch('subprocess.run')
    def test_get_commits_after_date(self, mock_run):
        mock_run.return_value = MagicMock(stdout="abc123\ndef456\nghi789")
        repo_path = "/path/to/repo"
        commit_date = datetime(2023, 1, 1)

        commits = get_commits_after_date(repo_path, commit_date)
        self.assertEqual(commits, ["abc123", "def456", "ghi789"])
        mock_run.assert_called_once_with(
            ['git', 'log', '--since', '2023-01-01', '--pretty=format:%H'],
            cwd=repo_path, capture_output=True, text=True
        )

    @patch('subprocess.run')
    def test_get_commit_messages(self, mock_run):
        mock_run.side_effect = [
            MagicMock(stdout="Initial commit"),
            MagicMock(stdout="Fix bug in API"),
            MagicMock(stdout="Update docs")
        ]
        repo_path = "/path/to/repo"
        commits = ["abc123", "def456", "ghi789"]

        messages = get_commit_messages(repo_path, commits)
        expected_messages = {
            "abc123": "Initial commit",
            "def456": "Fix bug in API",
            "ghi789": "Update docs"
        }
        self.assertEqual(messages, expected_messages)
        self.assertEqual(mock_run.call_count, 3)

    def test_get_linear_dependencies(self):
        commits = ["abc123", "def456", "ghi789"]
        dependencies = get_linear_dependencies("/path/to/repo", commits)
        expected_dependencies = {
            "def456": ["abc123"],
            "ghi789": ["def456"]
        }
        self.assertEqual(dependencies, expected_dependencies)

if __name__ == '__main__':
    unittest.main()
