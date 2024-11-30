import unittest
from unittest.mock import patch, mock_open

from main import main

class TestMain(unittest.TestCase):
    @patch('main.load_config', return_value={
        'repository_path': '/mock/repo/path',
        'visualization_program': '/mock/visualization_program.jar',
        'output_image_path': '/mock/output/graph.png',
        'commit_date': '2023-01-01'
    })
    @patch('main.subprocess.run')
    @patch('main.os.rename')
    @patch('builtins.open', new_callable=mock_open)
    def test_main(self, mock_open_file, mock_rename, mock_subprocess, mock_load_config):
        # Запуск тестируемой функции
        main()

        # Проверяем, что были вызваны subprocess.run и os.rename
        mock_subprocess.assert_called()
        mock_rename.assert_called()

        # Проверяем, что файл graph.puml был создан
        mock_open_file.assert_called_with('graph.puml', 'w')

if __name__ == '__main__':
    unittest.main()
