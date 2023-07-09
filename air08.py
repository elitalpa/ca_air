##### Air - Mélanger deux tableaux triés #####
# Créez un programme qui fusionne deux listes d’entiers triées
# en les gardant triées, les deux listes seront séparées par un “fusion”.
#
# Utilisez une fonction de ce genre (selon votre langage) :
## def sorted_fusion(array1, array2):
##     # your algo
##     return new_array
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def sorted_fusion(array1, array2):
    new_array = array1, array2

    # algo

    return new_array

def handle_argument_errors():
    contains_fusion_string = False

    if len(sys.argv) < 6:
        print("error: At least 5 arguments are required.")
        exit()

    for arg in sys.argv[1:]:
        if arg == "fusion":
            contains_fusion_string = True

        if not arg.strip('-').isdigit() and not arg == "fusion":
            print('error: All of your arguments must be integers except the "fusion" string which separates the lists of integers.')
            exit()

    if not contains_fusion_string:
        print('error: The "fusion" string is missing.')
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
# Finding the index of the "fusion" string in command-line arguments (excluding the filename).
fusion_index = sys.argv[1:].index("fusion") + 1

input_array1 = sys.argv[1:fusion_index]
input_array2 = sys.argv[fusion_index + 1:]

### Problem Solving ###
sorted_fusion_result = sorted_fusion(input_array1, input_array2)

### Result ###
print(" ".join([str(item) for item in sorted_fusion_result]))
