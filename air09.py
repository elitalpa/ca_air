##### Air - Rotation vers la gauche #####
# Créez un programme qui décale tous les éléments d’un tableau vers la gauche.
# Le premier élément devient le dernier à chaque rotation.
#
# Utilisez une fonction de ce genre (selon votre langage) :
## def ma_rotation(array):
##     # votre algorithme
##     return new_array
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def my_rotation(array):
    new_array = []

    # algo

    return new_array

def handle_argument_errors():
    if len(sys.argv) < 3:
        print("error: At least 2 arguments are required.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_array = sys.argv[1:]

### Problem Solving ###
my_rotation_result = my_rotation(input_array)

### Result ###
print(" ".join(my_rotation_result))