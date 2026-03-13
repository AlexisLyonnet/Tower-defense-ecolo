import pygame as pg
from pygame.math import Vector2
import math
from ennemies_data import ENNEMIES_DATA
import constante as c

class Ennemis(pg.sprite.Sprite):
    def __init__(self, ennemies_type, waypoints, images):
        pg.sprite.Sprite.__init__(self)
        self.ennemies_type = ennemies_type
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = ENNEMIES_DATA[self.ennemies_type].get("health")
        self.speed = ENNEMIES_DATA[self.ennemies_type].get("speed")
        self.angle = 0
        self.original_image = images.get(ennemies_type)
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self, world):
        self.move(world)
        self.rotate()
        self.verifie_mort(world)

    def move(self, world):
        if self.target_waypoint < len(self.waypoints):
        # Définition de la direction vers le prochain waypoint
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # Ennemis a atteint le dernier waypoint
            self.kill()
            world.niveau_vie -= 5
            world.ennemies_rates += 1

        # Calcul de la distance au prochain waypoint
        dist = self.movement.length()

        # Vérifier si la distance est inférieure à la vitesse pour éviter de dépasser le waypoint
        if dist >= (self.speed * world.game_speed):
            self.pos += self.movement.normalize() * (self.speed * world.game_speed)
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1

    def rotate(self):
        # Calculer la distance au prochain waypoint
        dist = self.target - self.pos
        # Utilise la distance pour calculer l'angle de rotation
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        # Rotater l'image de l'ennemi en fonction de l'angle calculé
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def verifie_mort(self, world):
        if self.health <= 0:
            world.ennemies_tues += 1
            world.monnaie += c.RECOMPENSE_TUE
            self.kill()