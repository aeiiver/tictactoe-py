import pygame
from morpion import *

pygame.init()
#########################################################################################################
# variables
grille = creer_une_grille()
fenetre_affichage = pygame.display.set_mode((600,600))
pygame.display.set_caption('Morpion')

# images
GRILLE = pygame.image.load("images/grille.png")
JETON_O = pygame.image.load("images/o.png")
JETON_X = pygame.image.load("images/x.png")
#########################################################################################################
# functions
def translate_pixels_into_indexes(position_souris):
    """
    Interprète la position de la souris en numéro 
    de ligne et colonne de la grille de jeu.

    Paramètres : 
        - [tuple of int] position_souris : contient les coordonnées de la souris

    Retour : [list] l'index de la ligne et l'index de la colonne, respectivement
    """
    indexes_grille = [0,0]
    positions = [200*i for i in range(4)]

    for index in range(3):
        if position_souris[0] in range(positions[index], positions[index+1]+1):
            indexes_grille[0] = index
    
        if position_souris[1] in range(positions[index], positions[index+1]+1):
            indexes_grille[1] = index

    return indexes_grille

def translate_indexes_into_pixels(row_no, column_no):
    """
    Interprète les indexes de la grille en pixels de l'affichage.

    Paramètres : 
        - [int] row_no : l'index de la ligne
        - [int] column_no : l'index de la colonne

    Retour : [tuple of ints] les postions en pixels de la ligne et de la colonne, respectivement
    """
    return (row_no*200, column_no*200)

def update_display(display, grille):
    """
    Actualise l'affichage de la grille.

    Paramètres : 
        - [pygame.display] display : la fenetre du jeu
        - [list of list] grille : la grille à actualiser

    Retour : aucun
    """
    display.blit(GRILLE, (0,0))

    for row_no in range(3):
        for column_no in range(3):
            if grille[row_no][column_no] == 1:
                display.blit(JETON_O, translate_indexes_into_pixels(row_no, column_no) )
            elif grille[row_no][column_no] == 2:
                display.blit(JETON_X, translate_indexes_into_pixels(row_no, column_no) )

def update_cursor_position(display, x, y, joueur):
    """
    Actualise la position du jeton qui suit le curseur du joueur.

    Paramètres : 
        - [pygame.display] display : la fenetre du jeu
        - [tuple] (x,y) : la nouvelle position du curseur du joueur
        - [int] joueur : le numéro du joueur

    Retour : aucun
    """
    display.blit(JETON_O if joueur == 1 else JETON_X, (x-100,y-100))

def change_player(Player_no):
    """
    Bascule le numéro entre les deux joueurs.

    Paramètres : 
        - [int] Player_no : le numéro du joueur actuel

    Retour : aucun
    """
    if Player_no == 1:
        return 2
    else:
        return 1
#########################################################################################################
# game loop
joueur = 1
_quit = False
while not _quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"Fin de la partie. Le joueur {joueur} a quitté la fenêtre.")
            _quit = True

        if event.type == pygame.MOUSEMOTION:
            (cursor_x,cursor_y) = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            indexes = translate_pixels_into_indexes((x,y))

            if placer_jeton(grille, indexes[0], indexes[1], joueur):
                joueur = change_player(joueur)

        if verifie_match_nul(grille):
            print("Match nul !")
            _quit = True

        if not verifie_victoire(grille) == 0:
            print(f"Joueur {verifie_victoire(grille)} a gagné !")
            _quit = True

    update_display(fenetre_affichage, grille)
    update_cursor_position(fenetre_affichage, cursor_x, cursor_y, joueur)
    pygame.display.update()
    
quit()