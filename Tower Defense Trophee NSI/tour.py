import pygame as pg
import math
import constante as c
from tour_data import TOUR_DATA


class Tour(pg.sprite.Sprite):
    def __init__(self, images, souris_grille_x, souris_grille_y):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        # list of surfaces for each level of the tower
        self.images = images
        # start with the first frame
        self.image = self.images[self.upgrade_level - 1]
        self.range = TOUR_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TOUR_DATA[self.upgrade_level - 1].get("cooldown")
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None


        self.souris_grille_x = souris_grille_x
        self.souris_grille_y = souris_grille_y
        #Calculer le centre de la grille
        self.x = (self.souris_grille_x + 0.5)* c.GRILLE
        self.y = (self.souris_grille_y + 0.5)* c.GRILLE
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        

        # creer un cercle transparent pour la portée de la tour
        size = max(1, int(math.ceil(self.range * 2)))
        radius = max(1, int(round(self.range)))
        self.range_image = pg.Surface((size, size))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (size // 2, size // 2), radius)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def update(self, ennemis_groupe, world):
        # Si la cible est choisie, joue l'animation
        #if self.target:
            #self.play_animation()
            
        #else:
        if pg.time.get_ticks() - self.last_shot > (self.cooldown / world.game_speed):
            self.choisi_cible(ennemis_groupe)

    def choisi_cible(self, ennemis_groupe):
        #trouver l'ennemi le plus proche dans la portée de la tour
        x_dist = 0
        y_dist = 0
        # calcule la distance a chaque ennemi
        for ennemi in ennemis_groupe:
            if ennemi.health > 0:    
                x_dist = ennemi.pos[0] - self.x
                y_dist = ennemi.pos[1] - self.y
                dist = math.sqrt(x_dist**2 + y_dist**2)
                if dist <= self.range:
                    self.target = ennemi
                    print("cible trouvé")
                    # Degat sur l'ennemi
                    self.target.health -= c.DEGATS
                    # register the shot time so cooldown is applied
                    self.last_shot = pg.time.get_ticks()
                    break

    def upgrade(self):
        # only upgrade if not already at maximum defined level
        if self.upgrade_level < len(self.images):
            self.upgrade_level += 1
            self.range = TOUR_DATA[self.upgrade_level - 1].get("range")
            self.cooldown = TOUR_DATA[self.upgrade_level - 1].get("cooldown")
            self.image = self.images[self.upgrade_level - 1]
        else:
            # already at max level, nothing to do
            return

        # améliorer la portée de la tour
        size = max(1, int(math.ceil(self.range * 2)))
        radius = max(1, int(round(self.range)))
        self.range_image = pg.Surface((size, size))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (size // 2, size // 2), radius)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
         

   