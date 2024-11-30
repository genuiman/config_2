def generate_plantuml(dependencies, messages):
    plantuml_code = "@startuml\n"
    plantuml_code += "skinparam linetype ortho\n"

    for commit, message in messages.items():
        plantuml_code += f'node "{commit}\\n{message}" as "{commit}"\n'

    for commit, parents in dependencies.items():
        for parent in parents:
            plantuml_code += f'"{parent}" --> "{commit}"\n'

    plantuml_code += "@enduml\n"
    return plantuml_code
