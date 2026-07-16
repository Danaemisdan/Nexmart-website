import os
import glob
from pathlib import Path

target_dir = r'c:\Users\91844\Downloads\Nexmart Website'

def get_tree(directory, prefix=''):
    lines = []
    items = sorted(os.listdir(directory))
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = (i == len(items) - 1)
        connector = '└── ' if is_last else '├── '
        lines.append(prefix + connector + item)
        if os.path.isdir(path):
            new_prefix = prefix + ('    ' if is_last else '│   ')
            lines.extend(get_tree(path, new_prefix))
    return lines

tree = get_tree(target_dir)

html_files = [Path(f).name for f in glob.glob(os.path.join(target_dir, '*.html'))]

with open('architecture_scan.txt', 'w', encoding='utf-8') as f:
    f.write('--- Folder Structure ---\n')
    f.write('\n'.join(tree))
    f.write('\n\n--- HTML Files ---\n')
    f.write('\n'.join(html_files))
