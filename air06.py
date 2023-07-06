##### Air - Contrôle de pass sanitaire #####
# Créez un programme qui supprime d’un tableau tous les éléments
# qui ne contiennent pas une autre chaîne de caractères.
#
# Utilisez une fonction de ce genre (selon votre langage) :
## def ma_fonction(array_de_strings, string):
##     # votre algorithme
##     return nouvel_array_de_strings
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def my_pass_controller(strings_array, string):
    new_strings_array = strings_array[:]
    # algo
    return new_strings_array

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.")
        exit()

    for arg in sys.argv[1:-1]:
        if arg.strip('-').isdigit():
            print("error: Your arguments must be strings.")
            exit()

    if sys.argv[-1::][0][0].strip('-').isdigit():
        print("error: Your last argument must be a string.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_strings_array = sys.argv[1:-1]
input_string = sys.argv[-1::][0][0]

### Problem Solving ###
my_pass_controller_result = my_pass_controller(input_strings_array, input_string)

### Result ###
print(my_pass_controller_result)
