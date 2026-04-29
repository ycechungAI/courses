import json

files_to_check = [
    'prompt_evaluations/05_prompt_foo_code_graded_animals/lesson.ipynb',
    'prompt_evaluations/06_prompt_foo_code_graded_classification/lesson.ipynb'
]

for file in files_to_check:
    with open(file, 'r') as f:
        nb = json.load(f)
    print(f"\n--- {file} ---")
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            source = "".join(cell['source'])
            if 'def ' in source and 'prompt' in source:
                print(f"Markdown Cell {idx} contains prompt functions.")
                print(source)
