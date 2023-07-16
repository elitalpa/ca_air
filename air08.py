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
    array1 = [int(n) for n in array1]
    array2 = [int(n) for n in array2]

    new_array = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1

    new_array += array1[i:]
    new_array += array2[j:]

    return new_array

def handle_argument_errors():
    contains_fusion_string = False

    if len(sys.argv) < 6:
        print("error: At least 5 arguments are required.", file=sys.stderr)
        exit()

    for arg in sys.argv[1:]:
        if arg == "fusion":
            contains_fusion_string = True

        if not arg.strip('-').isdigit() and not arg == "fusion":
            print('error: All of your arguments must be integers except the "fusion" string which separates the two sorted lists of integers.', file=sys.stderr)
            exit()

    if not contains_fusion_string:
        print('error: The "fusion" string is missing.', file=sys.stderr)
        exit()
    
    fusion_index = sys.argv[1:].index("fusion") + 1

    input_array1 = sys.argv[1:fusion_index]
    input_array2 = sys.argv[fusion_index + 1:]

    if len(input_array1) < 2 or len(input_array2) < 2:
        print('error: There must be at least two numbers before and after the "fusion" string.', file=sys.stderr)
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
