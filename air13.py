##### Air - Meta exercice #####
# Créez un programme qui vérifie si les exercices
# de votre épreuve de l’air sont présents dans le répertoire
# et qu’ils fonctionnent (sauf celui là).
# Créez au moins un test pour chaque exercice.
#
# Bonus : trouvez le moyen d’utiliser du vert et du rouge
# pour rendre réussites et échecs plus visibles.

import sys, subprocess

### Functions ###
def test_exercises():
    exercise_checks = [
        {
            "name": "air00",
            "tests": [
                {
                    "input": ["Bonjour les gars"],
                    "output": "Bonjour\nles\ngars\n"
                },
                {
                    "input": ["Ceci est un test"],
                    "output": "Ceci\nest\nun\ntest\n"
                },
                {
                    "input": ["Bonjour", "les", "gars"],
                    "output": ""
                },
                {
                    "input": [200],
                    "output": ""
                }
            ],
            "error_handling": ["test"]
        },
        {
            "name": "air01",
            "tests": [
                {
                    "input": ["Crevette magique dans la mer des étoiles", "la"],
                    "output": "Crevette magique dans \n mer des étoiles\n"
                },
                {
                    "input": ["Ceci est un test"],
                    "output": ""
                },
                {
                    "input": ["Bonjour", "les", "gars"],
                    "output": ""
                },
                {
                    "input": [200],
                    "output": ""
                }
            ]
        },
        {
            "name": "air02",
            "tests": [
                {
                    "input": ["je", "teste", "des", "trucs", " "],
                    "output": "je teste des trucs\n"
                }
            ]
        },
        {
            "name": "air03",
            "tests": [
                {
                    "input": [1, 2, 3, 4, 5, 4, 3, 2, 1],
                    "output": "5\n"
                },
                {
                    "input": ["bonjour", "monsieur", "bonjour"],
                    "output": "monsieur\n"
                }
            ]
        },
        {
            "name": "air04",
            "tests": [
                {
                    "input": ["Hello milady,    bien ou quoi ??"],
                    "output": "Helo milady, bien ou quoi ?\n"
                }
            ]
        },
        {
            "name": "air05",
            "tests": [
                {
                    "input": [1, 2, 3, 4, 5, "+2"],
                    "output": "3 4 5 6 7\n"
                },
                {
                    "input": [10, 11, 12, 20, "-5"],
                    "output": "5 6 7 15\n"
                }
            ]
        },
        {
            "name": "air06",
            "tests": [
                {
                    "input": ["Michel", "Albert", "Thérèse", "Benoit", "t"],
                    "output": "Michel\n"
                },
                {
                    "input": ["Michel", "Albert", "Thérèse", "Benoit", "a"],
                    "output": "Michel, Thérèse, Benoit\n"
                }
            ]
        },
        {
            "name": "air07",
            "tests": [
                {
                    "input": [1, 3, 4, 2],
                    "output": "1 2 3 4\n"
                },
                {
                    "input": [10, 20, 30, 40, 50, 60, 70, 90, 33],
                    "output": "10 20 30 33 40 50 60 70 90\n"
                }
            ]
        },
        {
            "name": "air08",
            "tests": [
                {
                    "input": [10, 20, 30, "fusion", 15, 25, 35],
                    "output": "10 15 20 25 30 35\n"
                }
            ]
        },
        {
            "name": "air09",
            "tests": [
                {
                    "input": ["Michel", "Albert", "Thérèse", "Benoit"],
                    "output": "Albert, Thérèse, Benoit, Michel\n"
                }
            ]
        },
        {
            "name": "air10",
            "tests": [
                {
                    "input": ["a.txt"],
                    "output": f"{subprocess.getoutput('cat a.txt')}"
                }
            ]
        },
        {
            "name": "air11",
            "tests": [
                {
                    "input": ["O", 5],
                    "output": "    O    \n   OOO   \n  OOOOO  \n OOOOOOO \nOOOOOOOOO\n"
                }
            ]
        },
        {
            "name": "air12",
            "tests": [
                {
                    "input": [6, 5, 4, 3, 2, 1],
                    "output": "1 2 3 4 5 6\n"
                }
            ]
        }
    ]

    test_result = ""
    is_success = False
    ascii_d_quotes = 34
    total_test_count = 0
    total_passed = 0

    for i in range(len(exercise_checks)):
        test_count = len(exercise_checks[i]["tests"])
        total_test_count += test_count
        passed = 0
        for j in exercise_checks[i]["tests"]:
            expected = f"{j['output']}"
            command = f"python {exercise_checks[i]['name']}.py {' '.join(str(f'{chr(ascii_d_quotes)}{item}{chr(ascii_d_quotes)}') for item in j['input'])}"
            
            completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if expected == completed_process.stdout:
                passed += 1
                total_passed += 1
            else:
                break

        if passed == test_count:
            is_success = True
        else:
            is_success = False

        test_result += f"{exercise_checks[i]['name']} ({passed}/{test_count}) : {'success' if is_success else 'failure'}\n"

    test_result += f"Total success: ({total_passed}/{total_test_count})"

    return test_result

def handle_argument_errors():
    if len(sys.argv) > 1:
        print("error: No arguments required.", file=sys.stderr)
        exit()

### Error Handling ###
handle_argument_errors()

### Parsing ###

### Problem Solving ###
test_exercises_result = test_exercises()

### Result ###
print(test_exercises_result)
