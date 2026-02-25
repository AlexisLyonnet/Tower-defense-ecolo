import pygame as pg
from ennemis import Ennemis
import constante as c


# Initialisation de Pygame
pg.init()   

clock = pg.time.Clock()

# Création de la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense - Sauver la Terre")

# Chargement des images
ennemmies_image = pg.image.load("actif/ennemis/Ennemis_1.png").convert_alpha()

# Création de groupe

ennemies_groupe = pg.sprite.Group()

# Création du chemin

waypoints = [
    (0, 300), 
    (100, 400), 
    (200, 400), 
    (300, 300), 
    (400, 400), 
    (500, 400)
    ]

ennemis = Ennemis((waypoints), ennemmies_image)
ennemies_groupe.add(ennemis)

# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    screen.fill("grey")

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
