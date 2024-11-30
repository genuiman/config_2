import unittest
from plantuml_utils import generate_plantuml

class TestPlantUMLUtils(unittest.TestCase):

    def test_generate_plantuml(self):
        dependencies = {
            "def456": ["abc123"],
            "ghi789": ["def456"]
        }
        messages = {
            "abc123": "Initial commit",
            "def456": "Fix bug in API",
            "ghi789": "Update docs"
        }
        plantuml_code = generate_plantuml(dependencies, messages)
        expected_code = """@startuml
skinparam linetype ortho
node "abc123\\nInitial commit" as "abc123"
node "def456\\nFix bug in API" as "def456"
node "ghi789\\nUpdate docs" as "ghi789"
"abc123" --> "def456"
"def456" --> "ghi789"
@enduml
"""
        self.assertEqual(plantuml_code.strip(), expected_code.strip())

if __name__ == '__main__':
    unittest.main()
