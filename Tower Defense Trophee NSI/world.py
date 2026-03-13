import pygame as pg
import random
import constante as c
from ennemies_data import ENNEMIES_SPAWN_DATA

class World():
    def __init__(self, data, map_image):
        self.level = 1
        self.game_speed = 1
        self.niveau_vie = c.NIVEAU_VIE
        self.monnaie = c.MONNAIE
        self.tile_map = []
        self.waypoints = []
        self.level_data = data
        self.image = map_image
        self.ennemies_liste = []
        self.spawned_ennemies = 0
        self.ennemies_tues = 0
        self.ennemies_rates = 0

    def process_ennemies(self):
        ennemies = ENNEMIES_SPAWN_DATA[self.level - 1]
        for ennemies_type in ennemies:
            ennemies_to_spawn = ennemies[ennemies_type]
            for i in range(ennemies_to_spawn):
                self.ennemies_liste.append(ennemies_type)
        # Mélanger la liste des ennemis pour un ordre de spawn aléatoire
        random.shuffle(self.ennemies_liste)

    def verifie_niveau_fini(self):
        if self.ennemies_tues + self.ennemies_rates >= len(self.ennemies_liste):
            return True

    def reset_niveau(self):
        #reset les variables pour le niveau suivant
        self.ennemies_liste = []
        self.spawned_ennemies = 0
        self.ennemies_tues = 0
        self.ennemies_rates = 0        

    def draw(self, surface):
        surface.blit(self.image, (0, 0))