import pygame as pg
from ennemis import Ennemis
from world import World
import constante as c
from bouton import Bouton
from tour import Tour


# Initialisation de Pygame
pg.init()   

clock = pg.time.Clock()

# Création de la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense - Sauver la Terre")

# Variables de jeu
placement_tour = False
selected_tour = None


# Chargement des images
#map
map_image = pg.image.load("actif/Map/grass_map_opacity_0.png").convert_alpha()
#ennemies
ennemmies_image = pg.image.load("actif/ennemis/Ennemis_1.png").convert_alpha()
#tours indivuelles pour curseur
tour_curseur = pg.image.load("actif/tours/plaine_tour_1.png").convert_alpha()
#bouton
acheter_tour_image = pg.image.load("actif/bouton/acheter_tour_bouton.png").convert_alpha()
annuler_image = pg.image.load("actif/bouton/annuler_bouton.png").convert_alpha()

def creer_tour(pos_souris):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    tour = Tour(tour_curseur, souris_grille_x, souris_grille_y)
    tour_groupe.add(tour)
    #print(tour_groupe)

def selectionner_tour(pos_souris):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    for tour in tour_groupe:
        if (souris_grille_x, souris_grille_y) == (tour.souris_grille_x, tour.souris_grille_y):
            return tour

#create world
world = World(map_image)


# Création de groupe
ennemies_groupe = pg.sprite.Group()
tour_groupe = pg.sprite.Group()

# Création du chemin

placement_interdit  = [
    (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0),
    (1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    ]






waypoints = [
    (0*c.GRILLE, 7.5*c.GRILLE), 
    (2.5*c.GRILLE, 7.5*c.GRILLE),
    (3*c.GRILLE, 7.7*c.GRILLE),
    (3.3*c.GRILLE, 8*c.GRILLE),
    (3.5*c.GRILLE, 8.5*c.GRILLE), 

    (3.5*c.GRILLE, 11*c.GRILLE),
    (3.7*c.GRILLE, 11.5*c.GRILLE), 
    (4*c.GRILLE, 12*c.GRILLE),
    (4.5*c.GRILLE, 12.3*c.GRILLE),
    (5*c.GRILLE, 12.4*c.GRILLE),
    (5.5*c.GRILLE, 12.3*c.GRILLE),
    (6*c.GRILLE, 12*c.GRILLE),
    (6.4*c.GRILLE, 11.5*c.GRILLE),
    (6.6*c.GRILLE, 11*c.GRILLE),

    (6.6*c.GRILLE, 6.7*c.GRILLE),
    (6.4*c.GRILLE, 6.2*c.GRILLE),
    (6*c.GRILLE, 5.8*c.GRILLE),
    (5.5*c.GRILLE, 5.6*c.GRILLE),

    (4*c.GRILLE, 5.6*c.GRILLE),
    (3.5*c.GRILLE, 5.4*c.GRILLE),
    (3.2*c.GRILLE, 5.1*c.GRILLE),
    (3*c.GRILLE, 4.5*c.GRILLE),
    (3.2*c.GRILLE, 3.9*c.GRILLE),
    (3.5*c.GRILLE, 3.6*c.GRILLE),
    (4*c.GRILLE, 3.5*c.GRILLE),
    
    (8.5*c.GRILLE, 3.5*c.GRILLE),
    (9*c.GRILLE, 3.7*c.GRILLE),
    (9.3*c.GRILLE, 4.0*c.GRILLE),
    (9.5*c.GRILLE, 4.5*c.GRILLE),

    (9.5*c.GRILLE, 13*c.GRILLE),
    (9.6*c.GRILLE, 13.3*c.GRILLE),
    (10*c.GRILLE, 13.8*c.GRILLE),
    (10.5*c.GRILLE, 14.1*c.GRILLE),
    (11*c.GRILLE, 14.15*c.GRILLE),
    (11.5*c.GRILLE, 14.1*c.GRILLE),
    (12*c.GRILLE, 13.8*c.GRILLE),
    (12.4*c.GRILLE, 13.4*c.GRILLE),
    (12.6*c.GRILLE, 13*c.GRILLE),

    (12.6*c.GRILLE, 7.5*c.GRILLE),
    (12.7*c.GRILLE, 7.1*c.GRILLE),
    (13*c.GRILLE, 6.7*c.GRILLE),
    (13.5*c.GRILLE, 6.4*c.GRILLE),
    (16*c.GRILLE, 6.4*c.GRILLE),
    ]

ennemis = Ennemis((waypoints), ennemmies_image)
ennemies_groupe.add(ennemis)


# Création des boutons
tour_bouton = Bouton(c.SCREEN_WIDTH + 50, 120, acheter_tour_image, True)
annuler_bouton = Bouton(c.SCREEN_WIDTH + 50, 220, annuler_image, True)

#-----------------------------------------------------------------------------------------------------------------------#

# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    #-----------------------------------------------------------#
    #-------------------------Update----------------------------#
    #-----------------------------------------------------------#

    #Mise à jour des ennemis
    ennemies_groupe.update()


    #Surligner la tour sélectionnée
    if selected_tour:
        selected_tour.select = True

    #-----------------------------------------------------------#
    #-------------------------Dessin----------------------------#
    #-----------------------------------------------------------#

    screen.fill("grey")

    # Dessiner le monde
    world.draw(screen)
    # Dessiner le chemin 
    #for i in range(len(waypoints)-1):
        #pg.draw.line(screen, "black", waypoints[i], waypoints[i+1], 5)

    # Dessiner les ennemis
    ennemies_groupe.draw(screen)
    for tour in tour_groupe:
        tour.draw(screen)

    # Dessiner les boutons
        #Bouton pour placer une tour
    if tour_bouton.draw(screen):
        placement_tour = True
    # Si le bouton de placement de tour est actif montre le bouton annuler 
    if placement_tour == True:
        #Affiche le curseur de la tour
        curseur_rect = tour_curseur.get_rect()
        curseur_pos = pg.mouse.get_pos()
        curseur_rect.center = curseur_pos
        if curseur_pos[0] < c.SCREEN_WIDTH and curseur_pos[1] < c.SCREEN_HEIGHT:
            screen.blit(tour_curseur, curseur_rect)
        if annuler_bouton.draw(screen):
            placement_tour = False
            
     




    # Gestion des événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # CLick de la souris
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            pos_souris = pg.mouse.get_pos()
            # Vérifier si la position de la souris est sur une case de la grille
            if pos_souris[0] < c.SCREEN_WIDTH and pos_souris[1] < c.SCREEN_HEIGHT:
                # Vérifier si la case est un emplacement interdit pour les tours
                if placement_interdit[pos_souris[1] // c.GRILLE][pos_souris[0] // c.GRILLE] == 1:
                    # Vérifier s'il n'y a pas déjà une tour à cet emplacement
                    emplacement_libre = True
                    for tour in tour_groupe:
                        if tour.rect.collidepoint(pos_souris):
                            emplacement_libre = False
                            break
                    # Si l'emplacement est libre, créer une tour
                    if emplacement_libre == True:
                        if placement_tour == True:
                            creer_tour(pos_souris)
                        else:
                            selected_tour = selectionner_tour(pos_souris)
                            if selected_tour:
                                selected_tour.select()

    #mise à jour des ennemis
    pg.display.flip()
pg.quit()









placement_interdit_3 = [
  (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
  (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
  (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1),
  (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
  (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
  (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
  (1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
  (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0),
  (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
  (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0),
  (1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0),
  (1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
  (1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
  (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
  (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
  ]


waypoints_3 = [
    (0*c.GRILLE, 7.5*c.GRILLE), 
    (2.5*c.GRILLE, 7.5*c.GRILLE),
    (3*c.GRILLE, 7.7*c.GRILLE),
    (3.3*c.GRILLE, 8*c.GRILLE),
    (3.5*c.GRILLE, 8.5*c.GRILLE), 

    (3.5*c.GRILLE, 11*c.GRILLE),
    (3.7*c.GRILLE, 11.5*c.GRILLE), 
    (4*c.GRILLE, 12*c.GRILLE),
    (4.5*c.GRILLE, 12.3*c.GRILLE),
    (5*c.GRILLE, 12.4*c.GRILLE),
    (5.5*c.GRILLE, 12.3*c.GRILLE),
    (6*c.GRILLE, 12*c.GRILLE),
    (6.4*c.GRILLE, 11.5*c.GRILLE),
    (6.6*c.GRILLE, 11*c.GRILLE),

    (6.6*c.GRILLE, 6.7*c.GRILLE),
    (6.4*c.GRILLE, 6.2*c.GRILLE),
    (6*c.GRILLE, 5.8*c.GRILLE),
    (5.5*c.GRILLE, 5.6*c.GRILLE),

    (4*c.GRILLE, 5.6*c.GRILLE),
    (3.5*c.GRILLE, 5.4*c.GRILLE),
    (3.2*c.GRILLE, 5.1*c.GRILLE),
    (3*c.GRILLE, 4.5*c.GRILLE),
    (3.2*c.GRILLE, 3.9*c.GRILLE),
    (3.5*c.GRILLE, 3.6*c.GRILLE),
    (4*c.GRILLE, 3.5*c.GRILLE),
    
    (8.5*c.GRILLE, 3.5*c.GRILLE),
    (9*c.GRILLE, 3.7*c.GRILLE),
    (9.3*c.GRILLE, 4.0*c.GRILLE),
    (9.5*c.GRILLE, 4.5*c.GRILLE),

    (9.5*c.GRILLE, 13*c.GRILLE),
    (9.6*c.GRILLE, 13.3*c.GRILLE),
    (10*c.GRILLE, 13.8*c.GRILLE),
    (10.5*c.GRILLE, 14.1*c.GRILLE),
    (11*c.GRILLE, 14.15*c.GRILLE),
    (11.5*c.GRILLE, 14.1*c.GRILLE),
    (12*c.GRILLE, 13.8*c.GRILLE),
    (12.4*c.GRILLE, 13.4*c.GRILLE),
    (12.6*c.GRILLE, 13*c.GRILLE),

    (12.6*c.GRILLE, 7.5*c.GRILLE),
    (12.7*c.GRILLE, 7.1*c.GRILLE),
    (13*c.GRILLE, 6.7*c.GRILLE),
    (13.5*c.GRILLE, 6.4*c.GRILLE),
    (16*c.GRILLE, 6.4*c.GRILLE),
    ]
