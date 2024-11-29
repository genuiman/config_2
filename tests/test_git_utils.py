import unittest
from unittest.mock import patch
from git_utils import get_commits_after_date

class TestGitUtils(unittest.TestCase):
    @patch('subprocess.run')
    def test_get_commits_after_date(self, mock_run):
        mock_run.return_value.stdout = "abc123\ndef456\n"
        commits = get_commits_after_date('/path/to/repo', '2023-01-01')
        self.assertEqual(commits, ['abc123', 'def456'])

if __name__ == '__main__':
    unittest.main()
