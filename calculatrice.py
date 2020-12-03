from operation.addition import additioner
from operation.soustraction import soustraire
from operation.multiplication import multiplier
from operation.division import diviser


# Définir une fonction nommée "demander_nombre" qui demande à l'utilisateur un nombre
# et le retourne (pour la mettre dans une variable)
def demander_nombre():
    return float(input('Saisir un nombre: '))

# Déclarer une variable nommée memoire pour stocker une valeur en mémoire
memoire = 0.0

# Mémoriser la saisie de l'utilisateur
# Au début, la saisie est vide car l'utilisateur n'a rien saisie
saisie_utilisateur = '' # texte vide

# Condition à remplir pour que la calculatrice reste allumé (fonctionne)
while saisie_utilisateur.lower() != 'x':  # ! -> négatif
    # Afficher la valeur de ce qui est en mémoire
    print('MEM: ' + str(memoire))
    
    # Afficher la saisie de l'utilisateur
    # print(saisie_utilisateur)

    # Demander à l'utilisateur de saisir un nombre
    if saisie_utilisateur == 'mr':
        nombre1 = memoire
    else:
        nombre1 = demander_nombre()

    # Demander à l'utilisateur de saisir l'opération à réaliser
    operation_saisie = input('Saisir une opération (+, -, *, /): ')

    # Vérifier que l'information saisie par l'utilisateur est valide
    liste_operation_valide = ['+', '-', '*', '/']
    if operation_saisie not in liste_operation_valide:
        exit()  # Quitte l'application

    # Demander à l'utilisateur de saisir un nombre
    nombre2 = demander_nombre()

    # Détecter la saisie (de la touche) "="
    saisie_utilisateur = input('(x pour quitter, = pour calculer, m+ pour ajouter en mémoire, m- pour retirer de la en mémoire, mr pour retrouver la valeur en mémoire): ')
    
    resultat = 0.0
    if saisie_utilisateur in ['=', 'm+', 'm-', 'mr']:
        # Afficher le résultat de l'opération
        if operation_saisie == '+':
            resultat = additioner(nombre1, nombre2)
        elif operation_saisie == '-':  # elif = else if = sinon si
            resultat = soustraire(nombre1, nombre2)
        elif operation_saisie == '*':
            resultat = multiplier(nombre1, nombre2)
        elif operation_saisie == '/':
            resultat = diviser(nombre1, nombre2)

        if saisie_utilisateur == '=':
            print(resultat)
        elif saisie_utilisateur == 'm+':
            # memoire = memoire+resultat # 1 + 3 -> 1 = memoire, 3 = resultat -> memoire+resultat
            memoire += resultat
        elif saisie_utilisateur == 'm-':
            memoire -= resultat
print('Au revoir.')
