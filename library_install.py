import os
import subprocess

def get_imported_libraries(file_path):
    imported_libraries = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.lstrip().startswith('import') or line.lstrip().startswith('from'):
                words = line.split()
                for word in words:
                    if word != 'import' and word != 'from':
                        library = word.replace('\n', '').replace(',', '')
                        if '.' not in library:
                            imported_libraries.append(library)
    return imported_libraries

def install_libraries(libraries):
    for library in libraries:
        subprocess.run(['pip', 'install', library])

def main():
    directory_path = input(r'chemin du dossier : ')  # Remplacez par le chemin du dossier à scanner
    libraries_to_install = set()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                libraries_to_install.update(get_imported_libraries(file_path))

    install_libraries(libraries_to_install)

if __name__ == "__main__":
    main()