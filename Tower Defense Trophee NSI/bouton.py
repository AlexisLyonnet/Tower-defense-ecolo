import pygame as pg

class Bouton(pg.sprite.Sprite):
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click  = single_click

    def draw(self, surface):
        action = False
        # Prend la position de la souris
        pos = pg.mouse.get_pos()

        # Souris au dessus et clique
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:  # Clic gauche
                action = True
                # Si le bouton est en mode single click, on le désactive après un clic
                if self.single_click:
                    self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Dessine le bouton
        surface.blit(self.image, self.rect)

        return action
