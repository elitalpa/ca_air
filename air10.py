##### Air - Afficher le contenu #####
# Créez un programme qui affiche le contenu d’un fichier donné en argument.
#
# Afficher error et quitter le programme
# en cas de problèmes d’arguments ou de fichier inaccessible.

import sys

### Functions ###
def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return content

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: One argument (the filename) is required.", file=sys.stderr)
        exit()

    try:
        with open(sys.argv[1], 'r'):
            pass
    except FileNotFoundError:
        print("error: File not found.", file=sys.stderr)
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_filename = sys.argv[1]

### Problem Solving ###
read_file_result = read_file(input_filename)

### Result ###
print(read_file_result, end="")
