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
        mouse_down = pg.mouse.get_pressed()[0] == 1

        # Souris au dessus et clique
        if self.rect.collidepoint(pos):
            if mouse_down and self.clicked == False:  # Clic gauche
                action = True
                # Si le bouton est en mode single click, on le désactive après un clic
                if self.single_click:
                    self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Dessine le bouton (agrandi de 3 px quand pressé ou actif)
        expand = (self.rect.collidepoint(pos) and mouse_down) or self.clicked
        if expand:
            w, h = self.image.get_size()
            disp = pg.transform.scale(self.image, (w + 3, h + 3))
            disp_rect = disp.get_rect(center=self.rect.center)
            surface.blit(disp, disp_rect)
        else:
            surface.blit(self.image, self.rect)

        return action