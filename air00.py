##### Air - Split #####
# Créez un programme qui découpe une chaîne de caractères en tableau
# (séparateurs : espaces, tabulations, retours à la ligne).
#
# Votre programme devra utiliser une fonction prototypée comme ceci :
## def ma_fonction(string_à_couper, string_séparateur): # syntaxe selon votre langage
##     # votre algorithme
##     return tableau
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def my_split(string_to_cut, string_separator):
    array = []
    i = 0

    for char in string_to_cut:
        if char not in string_separator:
            if len(array) <= i:
                array.append(char)
            else:
                array[i] += char
        else:
            i += 1

    return array

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: Only one argument is allowed.")
        exit()
    if sys.argv[1].strip('-').isdigit():
        print("error: Please provide a string argument.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

ascii_space = 32
ascii_new_line = 10
ascii_tab = 9
string_separator = [chr(ascii_space), chr(ascii_new_line), chr(ascii_tab)]

### Problem Solving ###
split_result = my_split(string_input, string_separator)

### Result ###
print(chr(ascii_new_line).join(split_result))
