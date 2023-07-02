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
def my_function(string_to_cut, string_separator):
    array = string_to_cut
    # algo
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
string_separator = [" "]

### Problem Solving ###
function_result = my_function(string_input, string_separator)

### Result ###
print(function_result)
