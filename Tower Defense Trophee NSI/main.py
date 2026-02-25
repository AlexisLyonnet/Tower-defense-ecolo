import pygame as pg
from ennemis import Ennemis
from world import World
import constante as c


# Initialisation de Pygame
pg.init()   

clock = pg.time.Clock()

# Création de la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense - Sauver la Terre")

# Chargement des images
#map
map_image = pg.image.load("actif/Map/grass_map_opacity_100.png").convert_alpha()
#ennemies
ennemmies_image = pg.image.load("actif/ennemis/Ennemis_1.png").convert_alpha()

#create world
world = World(map_image)


# Création de groupe

ennemies_groupe = pg.sprite.Group()

# Création du chemin

waypoints = [
    (0*c.GRILLE, 7.5*c.GRILLE), 
    (2.5*c.GRILLE, 7.5*c.GRILLE),
    (3.5*c.GRILLE, 8.5*c.GRILLE), 
    (3.5*c.GRILLE, 11.5*c.GRILLE), 
    (5*c.GRILLE, 12.5*c.GRILLE), 
    (6.7*c.GRILLE, 11.5*c.GRILLE),
    (6.7*c.GRILLE, 6.7*c.GRILLE),
    (5.5*c.GRILLE, 5.5*c.GRILLE),
    (3.5*c.GRILLE, 5.5*c.GRILLE),
    (3*c.GRILLE, 4.5*c.GRILLE),
    (3.5*c.GRILLE, 3.5*c.GRILLE),
    (8.5*c.GRILLE, 3.5*c.GRILLE),
    (9.5*c.GRILLE, 4.5*c.GRILLE),
    (9.5*c.GRILLE, 13.25*c.GRILLE),
    (11*c.GRILLE, 14.25*c.GRILLE),
    (12.7*c.GRILLE, 13.25*c.GRILLE),
    (12.7*c.GRILLE, 7.5*c.GRILLE),
    (13.5*c.GRILLE, 6.5*c.GRILLE),
    (16*c.GRILLE, 6.5*c.GRILLE),
    ]

ennemis = Ennemis((waypoints), ennemmies_image)
ennemies_groupe.add(ennemis)

# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    screen.fill("grey")

    # Dessiner le monde
    world.draw(screen)

    # Dessiner le chemin 
    pg.draw.lines(screen, "black", False, waypoints)


    #Mise à jour des ennemis
    ennemies_groupe.update()

    # Dessiner les ennemis
    ennemies_groupe.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #mise à jour des ennemis
    pg.display.flip()
pg.quit()
