from operation.addition import additioner
from operation.soustraction import soustraire
from operation.multiplication import multiplier
from operation.division import diviser


# Demander à l'utilisateur de saisir un nombre
nombre1 = float(input('Saisir un nombre: '))

# Demander à l'utilisateur de saisir l'opération à réaliser
operation_saisie = input('Saisir une opération (+, -, *, /): ')

# Vérifier que l'information saisie par l'utilisateur est valide
liste_operation_valide = ['+', '-', '*', '/']
if operation_saisie not in liste_operation_valide:
    exit()  # Quitte l'application

# Demander à l'utilisateur de saisir un nombre
nombre2 = float(input('Saisir un nombre: '))

# Détecter la saisie (de la touche) "="
touche_saisie = input()
if touche_saisie == '=':
    # Afficher le résultat de l'opération
    if operation_saisie == '+':
        additioner(nombre1, nombre2)
    if operation_saisie == '-':
        soustraire(nombre1, nombre2)
    if operation_saisie == '*':
        multiplier(nombre1, nombre2)
    if operation_saisie == '/':
        diviser(nombre1, nombre2)   
