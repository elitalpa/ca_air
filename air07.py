##### Air - Insertion dans un tableau trié #####
# Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier
# tout en gardant la liste triée dans l’ordre croissant.
# Le dernier argument est l’élément à ajouter.
#
# Utilisez une fonction de ce genre (selon votre langage) :
## def sorted_insert(array, new_element):
##     # your algo
##     return new_array
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def sorted_insert(input_array, input_new_element):
    array = [int(item) for item in input_array]
    new_element = int(input_new_element)

    new_array = []
    inserted = False
    
    for item in array:
        if not inserted and item > new_element:
            new_array.append(new_element)
            inserted = True

        new_array.append(item)

    if not inserted:
        new_array.append(new_element)

    return new_array

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.", file=sys.stderr)
        exit()

    for arg in sys.argv[1:-1]:
        if not arg.strip('-').isdigit():
            print("error: Your arguments must be integers.", file=sys.stderr)
            exit()

    if not sys.argv[-1::][0].strip('-').isdigit():
        print("error: Your last argument must be an integer.", file=sys.stderr)
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_array = sys.argv[1:-1]
input_new_element = sys.argv[-1::][0]

### Problem Solving ###
sorted_insert_result = sorted_insert(input_array, input_new_element)

### Result ###
print(" ".join([str(item) for item in sorted_insert_result]))
