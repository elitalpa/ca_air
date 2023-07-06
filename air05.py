##### Air - Sur chacun d’entre eux #####
# Créez un programme qui est capable de reconnaître
# et de faire une opération (addition ou soustraction)
# sur chaque entier d’une liste.
#
# L’opération à appliquer sera toujours le dernier élément.
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def perform_operation_on_each_integer(integers_list, operation):
    operation_results = []

    if operation[0] == '-':
        for n in integers_list:
            operation_results.append(int(n) - int(operation[1:]))
    else:
        for n in integers_list:
            operation_results.append(int(n) + int(operation[1:]))

    return operation_results

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.")
        exit()

    for arg in sys.argv[1:-1]:
        if not arg.strip('-').isdigit():
            print("error: Your arguments must be integers.")
            exit()

    if sys.argv[-1::][0][0] != '+' and sys.argv[-1::][0][0] != '-':
        print("error: Your last argument must begin with the operator + or - .")
        exit()
    if not sys.argv[-1::][0][1:].isdigit():
        print("error: Your last argument must contain only integers after the + or - operator.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_list = sys.argv[1:-1]
input_operation = sys.argv[-1::][0]

### Problem Solving ###
operation_on_each_integer_result = perform_operation_on_each_integer(input_list, input_operation)

### Result ###
print(" ".join([str(item) for item in operation_on_each_integer_result]))
