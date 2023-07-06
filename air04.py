##### Air - Un seul à la fois #####
# Créez un programme qui affiche une chaîne de caractères
# en évitant les caractères identiques adjacents.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def remove_adjacent_duplicates(char_string):
    filtered_string = char_string[0]

    for i in range(1, len(char_string) - 1):
        if char_string[i] != char_string[i - 1]:
            filtered_string += char_string[i]

    return filtered_string

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("error: Only one argument is required.")
        exit()
    if sys.argv[1].strip('-').isdigit():
        print("error: Your argument must be a string.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_string = sys.argv[1]

### Problem Solving ###
removed_adjacent_duplicates_result = remove_adjacent_duplicates(input_string)

### Result ###
print(removed_adjacent_duplicates_result)
