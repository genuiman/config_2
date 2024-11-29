import os
import subprocess
import yaml
from datetime import datetime
from git_utils import get_commits_after_date, get_commit_dependencies
from plantuml_utils import generate_plantuml

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config('../config.yaml')

    repo_path = config['repository_path']
    visualization_program = config['visualization_program']
    output_image_path = config['output_image_path']
    commit_date = datetime.strptime(config['commit_date'], "%Y-%m-%d")

    commits = get_commits_after_date(repo_path, commit_date)
    dependencies = get_commit_dependencies(repo_path, commits)

    plantuml_code = generate_plantuml(dependencies)

    with open('graph.puml', 'w') as f:
        f.write(plantuml_code)

    subprocess.run(['java', '-jar', visualization_program, 'graph.puml'])

    os.rename('graph.png', output_image_path)

    print(f"Граф успешно сгенерирован и сохранен в {output_image_path}")


if __name__ == '__main__':
    main()
