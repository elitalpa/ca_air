##### Air - Split en fonction #####
# Créez un programme qui découpe une chaîne de caractères en tableau en
# fonction du séparateur donné en 2e argument.
#
# Votre programme devra intégrer une fonction prototypée comme ceci :
## def ma_fonction(string_à_couper, string_séparateur): # syntaxe selon votre langage
##     # votre algorithme
##     return tableau
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def my_split_by(string_to_cut, string_separator):
    array = []
    i = 0
    j = 0

    while i < len(string_to_cut):
        if string_to_cut[i:i + len(string_separator)] != string_separator:
            if len(array) <= j:
                array.append(string_to_cut[i])
                i += 1
            else:
                array[j] += string_to_cut[i]
                i += 1
        else:
            array.append("")
            j += 1
            i += len(string_separator)

    return array

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("error: Two arguments are needed.")
        exit()
    if sys.argv[1].strip('-').isdigit() or sys.argv[2].strip('-').isdigit():
        print("error: Your arguments must be strings.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]
string_separator = sys.argv[2]

### Problem Solving ###
split_by_result = my_split_by(string_input, string_separator)

### Result ###
print("\n".join(split_by_result))
