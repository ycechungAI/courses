import os
import re

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Regex to find f-strings with XML tags containing variables
    # e.g., <tag>{var}</tag>
    matches = re.finditer(r'<[a-zA-Z0-9_-]+>.*?\{.+?\}.*?</[a-zA-Z0-9_-]+>', content, re.DOTALL)
    for match in matches:
        text = match.group()
        if 'html.escape' not in text and 'escape' not in text:
            print(f"Found potential unescaped XML tag injection in {filepath}:")
            print(text.strip())
            print("---")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') or file.endswith('.ipynb'):
            check_file(os.path.join(root, file))
