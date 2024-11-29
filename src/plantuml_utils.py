def generate_plantuml(dependencies):
    plantuml_code = "@startuml\n"
    for commit, parents in dependencies.items():
        for parent in parents:
            plantuml_code += f'"{parent}" --> "{commit}"\n'
    plantuml_code += "@enduml\n"
    return plantuml_code
