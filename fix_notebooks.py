import json

def update_notebook(filepath):
    with open(filepath, 'r') as f:
        nb = json.load(f)

    modified = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])

            if 'def simple_prompt(animal_statement):' in source or 'def basic_prompt(complaint):' in source:
                pass

    return modified
