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
def sorted_insert(array, new_element):
    new_array = array[:]
    # algo
    return new_array

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.")
        exit()

    for arg in sys.argv[1:-1]:
        if not arg.strip('-').isdigit():
            print("error: Your arguments must be integers.")
            exit()

    if not sys.argv[-1::][0][0].strip('-').isdigit():
        print("error: Your last argument must be an integer.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
array = sys.argv[1:-1]
new_element = sys.argv[-1::][0][0]

### Problem Solving ###
sorted_insert_result = sorted_insert(array, new_element)

### Result ###
print(sorted_insert_result)
