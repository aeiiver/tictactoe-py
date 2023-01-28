def creer_une_grille():
    """
    Créer une grille de jeu de morpion 3x3

    Paramètres : aucun

    Retour : aucun
    """
    return [[0,0,0] for _ in range(3)]

def verifie_victoire(grille):
    """
    Vérifie s'il y a un alignement horizontal, vertical ou 
    diagonal de 3 jetons, et donc s'il y a un vainqueur.

    Paramètres : 
        - [list of list] grille : la grille de jeu dans 
        lequel on souhaite vérifier s'il y a un vainqueur

    Retour :
        - [int] le numéro du vainqueur (1 ou 2) s'il y a un vainqueur
        - [int] 0                               s'il n'y a pas de vainqueur
    """

    # alignement horizontal
    for num_ligne in range(3):
        if (not grille[num_ligne][0] == 0) and (grille[num_ligne][0] == grille[num_ligne][1] == grille[num_ligne][2]):
            return grille[num_ligne][0]

    # alignement vertical
    for num_colonne in range(3):
        if (not grille[0][num_colonne] == 0) and (grille[0][num_colonne] == grille[1][num_colonne] == grille[2][num_colonne]):
            return grille[0][num_colonne]

    # alignement diagonal
    if (not grille[0][0] == 0) and ((grille[0][0] == grille[1][1] == grille[2][2]) or (grille[0][2] == grille[1][1] == grille[2][0])):
        return grille[0][0]

    return 0

def verifie_match_nul(grille):
    """
    Vérifie si toutes les cases de la grille 
    sont occupées par un joueur.

    Paramètres : 
        - [list of list] grille : la grille de jeu que l'on vérifie

    Retour :
        - [bool] True  si toute la grille est pleine
        - [bool] False si la grille n'est pas pleine
    """
    for row_no in range(3):
        for column_no in range(3):
            if grille[row_no][column_no] == 0:
                return False
    return True

def placer_jeton(grille, position_ligne, position_colonne, num_joueur):
    """
    Place un jeton sur la grille spécifiée en paramètre.

    Paramètres : 
        - [list of list] grille : la grille de jeu dans lequel on place un jeton
        - [int] position_ligne : index de la ligne on l'on place le jeton
        - [int] position_colonne : index de la colonne on l'on place le jeton
        - [int] num_joueur : le numéro du joueur

    Retour :
        - [bool] True  si le jeton a été placé avec succès
        - [bool] False si le jeton n'a pu être placé
    """
    if grille[position_ligne][position_colonne] == 0:
        grille[position_ligne][position_colonne] = num_joueur
        return True
    return False
    
if __name__ == "__main__":
    grille = [[2,5,2],
              [0,5,0],
              [2,5,3]]

    print(verifie_victoire(grille))
    
    placer_jeton(grille, 1, 1, 9)
    print(grille)