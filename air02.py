##### Air - Concat #####
# Créez un programme qui transforme un tableau de chaînes de caractères
# en une seule chaîne de caractères.
# Espacés d’un séparateur donné en dernier argument au programme.
#
# Utilisez une fonction de ce genre (selon votre langage) :
## ma_fonction(array_de_strings, separateur):
##     # votre algorithme
##     return string
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def my_concat(strings_array, separator):
    string = ""

    for element in strings_array:
        string += element + str(separator[0])

    return string[:-len(separator[0])]

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.")
        exit()

    for arg in sys.argv[1:-1]:
        if arg.strip('-').isdigit():
            print("error: Your arguments must be strings.")
            exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
array_input = sys.argv[1:-1]
separator_input = sys.argv[-1::]

### Problem Solving ###
concat_result = my_concat(array_input, separator_input)

### Result ###
print(concat_result)
