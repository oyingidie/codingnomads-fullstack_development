# 0. Write a script that walks through a nested folder structure
#    and prints out all the Python files it can find.
# 1. Run it in your labs folder and add formatting for nicer viewing.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pathlib

directory = pathlib.Path.cwd()

for file in directory.rglob('*.py'):
    relative_path_parts = file.relative_to(directory).parts
    indentation_level = len(relative_path_parts) - 1
    indent = '  ' * indentation_level
    print(f"{indent}{file.name}")
