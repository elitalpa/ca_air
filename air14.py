##### Air - Air : ok #####
# Créez un programme qui célèbre votre victoire.
#
# Note : [] est à remplacer par un adjectif de votre choix (facile ?)

import random

### Function ###
def get_victory_message():
    adjective_of_victory = ["[]"] # to be filled with adjectives
    victory_index = random.randint(0, len(adjective_of_victory) - 1)
    return f"J’ai terminé l’Épreuve de l’Eau et c’était {adjective_of_victory[victory_index]}."

### Error ###

### Parsing ###

### Problem Solving ###
victory_message = get_victory_message()

### Result ###
print(victory_message)
