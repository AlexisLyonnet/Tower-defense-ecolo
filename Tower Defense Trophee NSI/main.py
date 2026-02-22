import pygame as pg
import constante as c
from ennemis import Ennemis

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

Ennemis = Ennemis((200, 300), ennemmies_image)
ennemies_groupe.add(Ennemis)


# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()