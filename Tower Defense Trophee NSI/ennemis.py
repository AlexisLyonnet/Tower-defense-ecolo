import pygame as pg
from pygame.math import Vector2
import math

class Ennemis(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.angle = 0
        self.orinial_image = image
        self.image = pg.transform.rotate(self.orinial_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()
        self.rotate()

    def move(self):
        if self.target_waypoint < len(self.waypoints):
        # Définition de la direction vers le prochain waypoint
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # Ennemis a atteint le dernier waypoint
            self.kill()

        # Calcul de la distance au prochain waypoint
        dist = self.movement.length()
        print(dist)

        # Vérifier si la distance est inférieure à la vitesse pour éviter de dépasser le waypoint
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
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
        self.image = pg.transform.rotate(self.orinial_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
