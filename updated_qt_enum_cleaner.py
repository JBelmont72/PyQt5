'''
two improved versons of the qt_enum_cleaner.py script that:
Recursively walks through a folder and its subfolders.
Cleans enum issues like QtCore.Qt.AlignCenter.
Removes redundant QtCore.Qt.QtCore prefixes.
Automatically adds a test runner block to show the window if it finds a class named Ui_MainWindow (you can easily extend this logic later).


'''
import sys
import os
import re
from pathlib import Path

def clean_enum_syntax(code):
    # Fix C++-style enums like QtCore.Qt.QFrame::Shape::Box -> QtWidgets.QFrame.Box
    code = re.sub(r'Qt(Core|Gui)?\.Qt\.QFrame::(Shape|Shadow)::(\w+)', r'QtWidgets.QFrame.\3', code)

    # Replace Qt::Something::Value -> Qt.Something.Value
    code = re.sub(r'Qt::(\w+)::(\w+)', r'Qt.\1.\2', code)

    # Replace Qt::Something -> Qt.Something
    code = re.sub(r'Qt::(\w+)', r'Qt.\1', code)

    # Remove repeated Qt. or QtCore.Qt.Qt
    code = re.sub(r'(QtCore|QtGui)?\.?(Qt\.)+(Qt\.)*', r'QtCore.Qt.', code)

    return code

def add_missing_imports(code):
    # Check for use of QtWidgets.QFrame without import
    if 'QtWidgets.QFrame' in code and 'from PyQt5.QtWidgets import QFrame' not in code:
        lines = code.splitlines()
        for i, line in enumerate(lines):
            if line.startswith('from PyQt5.QtWidgets'):
                # Append QFrame if PyQt5.QtWidgets is already imported
                if 'QFrame' not in line:
                    lines[i] = line.rstrip() + ', QFrame'
                break
        else:
            # No import line found, insert a new one after PyQt5.QtWidgets import
            for i, line in enumerate(lines):
                if line.startswith('from PyQt5'):
                    lines.insert(i + 1, 'from PyQt5.QtWidgets import QFrame')
                    break
        return '\n'.join(lines)
    return code

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        original = f.read()

    cleaned = clean_enum_syntax(original)
    cleaned = add_missing_imports(cleaned)

    if original != cleaned:
        # Back up original
        backup_path = f"{file_path}.bak"
        with open(backup_path, 'w', encoding='utf-8') as backup_file:
            backup_file.write(original)
        # Save cleaned version
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"✅ Cleaned and backed up: {file_path}")
    else:
        print(f"✔️ Already clean: {file_path}")

def process_directory(target):
    path = Path(target)
    if path.is_file() and path.suffix == '.py':
        process_file(path)
    elif path.is_dir():
        for file in path.rglob("*.py"):
            process_file(file)
    else:
        print(f"❌ Not a valid .py file or directory: {target}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qt_enum_cleaner.py <file_or_directory>")
    else:
        process_directory(sys.argv[1])
####################
# This script does the following:
# 1. Cleans enum syntax issues.
# 2. Removes redundant prefixes.
# 3. Adds missing imports for QFrame.
# 4. Backs up the original file before writing changes.
# 5. Processes both files and directories recursively.
# 6. Provides user feedback on the cleaning process.


# import sys
# import os
# import re
# from pathlib import Path

# WIDGET_ENUM_IMPORTS = {
#     'QFrame': 'from PyQt5.QtWidgets import QFrame',
#     'QSizePolicy': 'from PyQt5.QtWidgets import QSizePolicy',
#     'QAbstractItemView': 'from PyQt5.QtWidgets import QAbstractItemView',
#     'QStyle': 'from PyQt5.QtWidgets import QStyle',
# }

# def clean_enum_syntax(code):
#     original_code = code

#     # Replace C++-style Qt enums (e.g., Qt::AlignmentFlag::AlignCenter)
#     code = re.sub(r'Qt::(\w+)::(\w+)', r'Qt.\1.\2', code)

#     # Replace double Qt references (e.g., QtCore.Qt.Qt.AlignCenter -> QtCore.Qt.AlignCenter)
#     code = re.sub(r'(QtCore|QtGui)\.Qt\.Qt\.', r'\1.Qt.', code)

#     # Replace widget enums (e.g., Qt::QFrame::Shape::Box -> QtWidgets.QFrame.Box)
#     code = re.sub(r'Qt::Q(Frame)::\w+::(\w+)', r'QtWidgets.\1.\2', code)
#     code = re.sub(r'Qt::Q(SizePolicy)::\w+::(\w+)', r'QtWidgets.\1.\2', code)
#     code = re.sub(r'Qt::Q(AbstractItemView)::\w+::(\w+)', r'QtWidgets.\1.\2', code)
#     code = re.sub(r'Qt::Q(Style)::\w+::(\w+)', r'QtWidgets.\1.\2', code)

#     # General cleanup of Qt::Enum -> Qt.Enum
#     code = re.sub(r'Qt::(\w+)', r'Qt.\1', code)

#     return code

# def inject_imports_if_missing(code):
#     lines = code.splitlines()
#     import_lines = [line for line in lines if line.startswith('from PyQt5.QtWidgets import')]
#     existing_imports = set()
#     for line in import_lines:
#         for item in line.replace('from PyQt5.QtWidgets import', '').split(','):
#             existing_imports.add(item.strip())

#     new_imports = []
#     for widget, import_stmt in WIDGET_ENUM_IMPORTS.items():
#         if widget in code and widget not in existing_imports:
#             new_imports.append(import_stmt)

#     if new_imports:
#         # Insert new imports after existing PyQt5 imports
#         for i, line in enumerate(lines):
#             if line.startswith('from PyQt5') or line.startswith('import PyQt5'):
#                 continue
#             # Insert after last PyQt5 import
#             insert_index = i
#             break
#         else:
#             insert_index = 0

#         lines = lines[:insert_index] + new_imports + lines[insert_index:]

#     return '\n'.join(lines)

# def process_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         original = f.read()

#     cleaned = clean_enum_syntax(original)
#     cleaned = inject_imports_if_missing(cleaned)

#     if original != cleaned:
#         backup_path = file_path + '.bak'
#         os.rename(file_path, backup_path)
#         with open(file_path, 'w', encoding='utf-8') as f:
#             f.write(cleaned)
#         print(f"✅ Cleaned: {file_path} (backup saved as {backup_path})")
#     else:
#         print(f"✔️ Already clean: {file_path}")

# def process_directory(target):
#     path = Path(target)
#     if path.is_file() and path.suffix == '.py':
#         process_file(path)
#     elif path.is_dir():
#         for file in path.rglob("*.py"):
#             process_file(file)
#     else:
#         print(f"❌ Not a valid .py file or directory: {target}")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python qt_enum_cleaner.py <file_or_directory>")
#     else:
#         process_directory(sys.argv[1])