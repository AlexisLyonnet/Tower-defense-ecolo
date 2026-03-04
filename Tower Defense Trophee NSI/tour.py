import pygame as pg
import constante as c

class Tour(pg.sprite.Sprite):
    def __init__(self, image, souris_grille_x, souris_grille_y):
        super().__init__()
        self.range = 2.5 * c.GRILLE
        self.selected = False
        self.souris_grille_x = souris_grille_x
        self.souris_grille_y = souris_grille_y
        #Calculer le centre de la grille
        self.x = (self.souris_grille_x + 0.5)* c.GRILLE
        self.y = (self.souris_grille_y + 0.5)* c.GRILLE
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


        #creer un cercle transparrent pour la portée de la tour
        self.range_image = pg.Surface((self.range*2, self.range*2)) 
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
         

   
