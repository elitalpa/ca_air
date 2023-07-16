##### Air - Afficher une pyramide #####
# Afficher un escalier constitué d’un caractère
# et d’un nombre d’étages donné en paramètre.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def generate_pyramid(char, number_of_floors):
    number_of_floors_int = int(number_of_floors)
    pyramid = []

    for floor in range(1, number_of_floors_int + 1):
        spaces = ' ' * (number_of_floors_int - floor)
        line = spaces + char * (2 * floor - 1) + spaces

        pyramid.append(line + '\n')

    return pyramid

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("error: Two arguments are required: the charachter and the number of floors for your pyramid.", file=sys.stderr)
        exit()

    if len(sys.argv[1]) != 1:
        print("error: Your first argument can only be one charachter.", file=sys.stderr)
        exit()

    if not sys.argv[2].isdigit() or int(sys.argv[2]) <= 0:
        print("error: Your second argument needs to be a positive integer above 0.", file=sys.stderr)
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_char = sys.argv[1]
input_floors = sys.argv[2]

### Problem Solving ###
generated_pyramid_result = generate_pyramid(input_char, input_floors)

### Result ###
print(''.join(generated_pyramid_result), end="")
