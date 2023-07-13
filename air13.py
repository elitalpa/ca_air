##### Air - Meta exercice #####
# Créez un programme qui vérifie si les exercices
# de votre épreuve de l’air sont présents dans le répertoire
# et qu’ils fonctionnent (sauf celui là).
# Créez au moins un test pour chaque exercice.
#
# Bonus : trouvez le moyen d’utiliser du vert et du rouge
# pour rendre réussites et échecs plus visibles.

import sys

### Functions ###
def test_exercises():
    test_result = ""
    # algo
    return test_result

def handle_argument_errors():
    if len(sys.argv) > 1:
        print("error: No arguments required.")
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###

### Problem Solving ###
test_exercises_result = test_exercises()

### Result ###
print(test_exercises_result)
