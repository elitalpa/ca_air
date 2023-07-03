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
def my_function(string_to_cut, string_separator):
    array = string_to_cut
    # algo
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
string_separator = [chr(32), chr(10), chr(9)]

### Problem Solving ###
function_result = my_function(string_input, string_separator)

### Result ###
print(function_result)
