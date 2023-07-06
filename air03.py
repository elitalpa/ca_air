##### Air - Chercher l’intrus #####
# Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.
#
# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

### Functions ###
def find_intruder(values_list):
    intruder = ""
    occ_dict = {}
    
    for element in values_list:
        if element in occ_dict:
            occ_dict[element] += 1
        else:
            occ_dict[element] = 1

    for key, value in occ_dict.items():
        if value == 1:
            intruder += key + " "
    
    return intruder[:-1]

def handle_argument_errors():
    if len(sys.argv) < 4:
        print("error: At least three arguments are needed.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###
input_list = sys.argv[1:]

### Problem Solving ###
intruder_result = find_intruder(input_list)

### Result ###
print(intruder_result)
