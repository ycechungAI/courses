import json

def update_notebook(filepath):
    with open(filepath, 'r') as f:
        nb = json.load(f)

    modified = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source_list = cell['source']
            for i, line in enumerate(source_list):
                if '<animal_statement>{animal_statement}</animal_statement>' in line:
                    source_list[i] = line.replace('<animal_statement>{animal_statement}</animal_statement>', '<animal_statement>{html.escape(str(animal_statement))}</animal_statement>')
                    modified = True
                if '<complaint>{complaint}</complaint>' in line:
                    source_list[i] = line.replace('<complaint>{complaint}</complaint>', '<complaint>{html.escape(str(complaint))}</complaint>')
                    modified = True

            if modified and 'def simple_prompt(animal_statement):' in "".join(source_list) and 'import html' not in "".join(source_list):
                source_list.insert(0, "import html\n\n")
            if modified and 'def basic_prompt(complaint):' in "".join(source_list) and 'import html' not in "".join(source_list):
                source_list.insert(0, "import html\n\n")

    if modified:
        with open(filepath, 'w') as f:
            json.dump(nb, f, indent=1)
            f.write('\n')
        print(f"Updated {filepath}")

update_notebook('prompt_evaluations/05_prompt_foo_code_graded_animals/lesson.ipynb')
update_notebook('prompt_evaluations/06_prompt_foo_code_graded_classification/lesson.ipynb')
