##### Air - Le roi des tris #####
# Créez un programme qui trie une liste de nombres.
# Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
#
# Vous utiliserez une fonction de cette forme (selon votre langage) :
## def my_quick_sort(array):
##     # votre algorithme
##     return new_array
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.
# Wikipedia vous présentera une belle description de cet algorithme de tri.

import sys

### Functions ###
def my_quick_sort(array):
    new_array = []

    # algo

    return new_array

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("error: At least two arguments are required.")
        exit()

    for arg in sys.argv[1:]:
        if not arg.strip('-').isdigit():
            print("error: Your arguments must be integers.")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_array = sys.argv[1:]

### Problem Solving ###
my_quick_sort_result = my_quick_sort(input_array)

### Result ###
print(' '.join([str(i) for i in my_quick_sort_result]))
