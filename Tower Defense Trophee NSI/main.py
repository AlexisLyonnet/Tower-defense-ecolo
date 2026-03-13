import pygame as pg
from ennemis import Ennemis
from world import World
import constante as c
from bouton import Bouton
from tour import Tour
from ennemies_data import ENNEMIES_SPAWN_DATA

# Initialisation de Pygame
pg.init()   

clock = pg.time.Clock()

# Création de la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense - Sauver la Terre")

# Variables de jeu
game_over = False
game_outcome = 0 # -1 est perdu, 0 est en cours, 1 est gagné
dernier_ennemies_spawn = pg.time.get_ticks()
placement_tour = False
selected_tour = None
niveau_commence = False


# Chargement des images
#map
# Chargement des images
# map (two versions: with grid and without)
map_image_grille_0 = pg.image.load("actif/Map/grass_map_opacity_0.png").convert_alpha()
map_image_grille_100 = pg.image.load("actif/Map/grass_map_opacity_100.png").convert_alpha()
#ennemies
ennemies_images = {
    "faible" : pg.image.load("actif/ennemis/Ennemis_1.png").convert_alpha(),
    "moyen" : pg.image.load("actif/ennemis/Ennemis_2.png").convert_alpha(),
    "fort" : pg.image.load("actif/ennemis/Ennemis_3.png").convert_alpha(),
    "boss" : pg.image.load("actif/ennemis/Ennemis_4.png").convert_alpha()
}
#tours indivuelles pour curseur
tour_plaines = []
for x in range(1, c.NIVEAU_MAX + 1):
    img = pg.image.load(f"actif/tours/plaine_tour_{x}.png").convert_alpha()
    tour_plaines.append(img)

if tour_plaines:
    tour_curseur = tour_plaines[0]
else:
    tour_curseur = pg.Surface((c.GRILLE, c.GRILLE))
    tour_curseur.fill((255,0,255))  
#bouton
acheter_tour_image = pg.image.load("actif/bouton/acheter_tour_bouton.png").convert_alpha()
annuler_image = pg.image.load("actif/bouton/annuler_bouton.png").convert_alpha()
ameliorer_image = pg.image.load("actif/bouton/amelioration_bouton.png").convert_alpha()
commencer_image = pg.image.load("actif/bouton/commencer_bouton.png").convert_alpha()
recommencer_image = pg.image.load("actif/bouton/recommencer_bouton.png").convert_alpha()
accelerer_1x_image = pg.image.load("actif/bouton/vitesse_x1_bouton.png").convert_alpha()
accelerer_2x_image = pg.image.load("actif/bouton/vitesse_x2_bouton.png").convert_alpha()
# Affiche les polices pour les textes 
police_texte = pg.font.SysFont("Arial", 24, bold=True)
police_large = pg.font.SysFont("Arial", 36)

# Load optional right-panel background image (fallback to a solid surface)
try:
    panel_bg = pg.image.load("Actif/Gui/interface.png").convert_alpha()
    panel_bg = pg.transform.scale(panel_bg, (c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
except Exception:
    panel_bg = pg.Surface((c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
    panel_bg.fill((200, 200, 200))

# Fonction pour montrer le texte à l'écran
def draw_texte(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def display_data(): 
    #Dessine l'interface d'utilisation
    pg.draw.rect(screen)



def creer_tour(pos_souris):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    tour = Tour(tour_plaines, souris_grille_x, souris_grille_y)
    tour_groupe.add(tour)
    #print(tour_groupe)
    

def selectionner_tour(pos_souris):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    for tour in tour_groupe:
        if (souris_grille_x, souris_grille_y) == (tour.souris_grille_x, tour.souris_grille_y):
            return tour
        
def deselectionner_tour():
    for tour in tour_groupe:
        tour.selected = False

#create world
world = World(ENNEMIES_SPAWN_DATA, map_image_grille_100)
world.process_ennemies()


# Création de groupe
ennemies_groupe = pg.sprite.Group()
tour_groupe = pg.sprite.Group()

# Création du chemin

placement_interdit  = [
    (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0),
    (1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    ]






waypoints = [
    (0*c.GRILLE, 7.5*c.GRILLE), 
    (2.5*c.GRILLE, 7.5*c.GRILLE),
    (3*c.GRILLE, 7.7*c.GRILLE),
    (3.3*c.GRILLE, 8*c.GRILLE),
    (3.5*c.GRILLE, 8.5*c.GRILLE), 

    (3.5*c.GRILLE, 11*c.GRILLE),
    (3.7*c.GRILLE, 11.5*c.GRILLE), 
    (4*c.GRILLE, 12*c.GRILLE),
    (4.5*c.GRILLE, 12.3*c.GRILLE),
    (5*c.GRILLE, 12.4*c.GRILLE),
    (5.5*c.GRILLE, 12.3*c.GRILLE),
    (6*c.GRILLE, 12*c.GRILLE),
    (6.4*c.GRILLE, 11.5*c.GRILLE),
    (6.6*c.GRILLE, 11*c.GRILLE),

    (6.6*c.GRILLE, 6.7*c.GRILLE),
    (6.4*c.GRILLE, 6.2*c.GRILLE),
    (6*c.GRILLE, 5.8*c.GRILLE),
    (5.5*c.GRILLE, 5.6*c.GRILLE),

    (4*c.GRILLE, 5.6*c.GRILLE),
    (3.5*c.GRILLE, 5.4*c.GRILLE),
    (3.2*c.GRILLE, 5.1*c.GRILLE),
    (3*c.GRILLE, 4.5*c.GRILLE),
    (3.2*c.GRILLE, 3.9*c.GRILLE),
    (3.5*c.GRILLE, 3.6*c.GRILLE),
    (4*c.GRILLE, 3.5*c.GRILLE),
    
    (8.5*c.GRILLE, 3.5*c.GRILLE),
    (9*c.GRILLE, 3.7*c.GRILLE),
    (9.3*c.GRILLE, 4.0*c.GRILLE),
    (9.5*c.GRILLE, 4.5*c.GRILLE),

    (9.5*c.GRILLE, 13*c.GRILLE),
    (9.6*c.GRILLE, 13.3*c.GRILLE),
    (10*c.GRILLE, 13.8*c.GRILLE),
    (10.5*c.GRILLE, 14.1*c.GRILLE),
    (11*c.GRILLE, 14.15*c.GRILLE),
    (11.5*c.GRILLE, 14.1*c.GRILLE),
    (12*c.GRILLE, 13.8*c.GRILLE),
    (12.4*c.GRILLE, 13.4*c.GRILLE),
    (12.6*c.GRILLE, 13*c.GRILLE),

    (12.6*c.GRILLE, 7.5*c.GRILLE),
    (12.7*c.GRILLE, 7.1*c.GRILLE),
    (13*c.GRILLE, 6.7*c.GRILLE),
    (13.5*c.GRILLE, 6.4*c.GRILLE),
    (16*c.GRILLE, 6.4*c.GRILLE),
    ]




# Création des boutons (centrés dans le panneau de droite)

tour_bouton = Bouton((c.SCREEN_WIDTH + 30), 237.5, acheter_tour_image, True)
annuler_bouton = Bouton((c.SCREEN_WIDTH + 30), 427.9, annuler_image, True)
ameliorer_bouton = Bouton((c.SCREEN_WIDTH + 30), 237.5, ameliorer_image, True)
commencer_bouton = Bouton((c.SCREEN_WIDTH + 30), 133.8, commencer_image, True)
recommencer_bouton = Bouton((c.SCREEN_WIDTH + 31.6), 380, recommencer_image, True)
accelerer_1x_bouton = Bouton((c.SCREEN_WIDTH + 31.6), 635.4, accelerer_1x_image, True)
accelerer_2x_bouton = Bouton((c.SCREEN_WIDTH + 169.7) , 635.4, accelerer_2x_image, True)

#-----------------------------------------------------------------------------------------------------------------------#

# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    #-----------------------------------------------------------#
    #-------------------------Update----------------------------#
    #-----------------------------------------------------------#

    if game_over == False:
        #verifie si le joueur a perdu
        if world.niveau_vie <= 0:
            game_over = True
            game_outcome = -1
        #verifie si le joueur a gagner
        if world.level > c.NOMBRE_NIVEAU:
            game_over = True
            game_outcome = 1


        #Mise à jour des ennemis
        ennemies_groupe.update(world)
        tour_groupe.update(ennemies_groupe, world)


        #Surligner la tour sélectionnée
        if selected_tour:
            selected_tour.selected = True

    #-----------------------------------------------------------#
    #-------------------------Dessin----------------------------#
    #-----------------------------------------------------------#

    screen.fill("grey")

    # Dessiner le monde
    # Change la carte selon si on place une tour ou non
    if placement_tour or selected_tour:
        world.image = map_image_grille_0
    else:
        world.image = map_image_grille_100
    world.draw(screen)
    screen.blit(panel_bg, (c.SCREEN_WIDTH, 0))
    # Dessiner le chemin 
    #for i in range(len(waypoints)-1):
        #pg.draw.line(screen, "black", waypoints[i], waypoints[i+1], 5)

    barre_info_image = pg.image.load("actif//gui/barre_info.png").convert_alpha()
    screen.blit(barre_info_image, (10, 10))



    # Dessiner les ennemis
    ennemies_groupe.draw(screen)
    for tour in tour_groupe:
        tour.draw(screen)


    police_petit = pg.font.SysFont("Arial", 16, bold=True)

    img_niveau_vie = police_petit.render(f"{world.niveau_vie}/{c.NIVEAU_VIE}", True, "grey100")
    rect_niveau_vie = img_niveau_vie.get_rect(bottomright=(114, 54))
    screen.blit(img_niveau_vie, rect_niveau_vie)

    img_monnaie = police_petit.render(str(world.monnaie), True, "grey100")
    rect_monnaie = img_monnaie.get_rect(bottomright=(196, 54))
    screen.blit(img_monnaie, rect_monnaie)

    draw_texte(str(world.level), police_petit, "grey100", 10, 70)

    if game_over == False:
        #Verifie si la partie a commencé
        if niveau_commence == False:
            if commencer_bouton.draw(screen):
                    niveau_commence = True
        #Spawn les ennemis
        else:
            # Accelere le jeu
            if accelerer_2x_bouton.draw(screen):
                world.game_speed = 2
            if accelerer_1x_bouton.draw(screen):
                world.game_speed = 1
            if pg.time.get_ticks() - dernier_ennemies_spawn > c.SPAWN_COOLDOWN:
                if world.spawned_ennemies < len(world.ennemies_liste):
                    ennemies_type = world.ennemies_liste[world.spawned_ennemies]
                    ennemis = Ennemis(ennemies_type, (waypoints), ennemies_images)
                    ennemies_groupe.add(ennemis)
                    world.spawned_ennemies += 1
                    dernier_ennemies_spawn = pg.time.get_ticks()



        #Verifie si la vague est terminé
        if world.verifie_niveau_fini() == True:
            world.monnaie += c.NIVEAU_FINI
            world.level += 1
            niveau_commence = False
            last_ennemies_spawn = pg.time.get_ticks()
            world.reset_niveau()
            world.process_ennemies()


        # Dessiner les boutons
        # Bouton pour placer une tour (caché si une tour est sélectionnée)
        if not selected_tour:
            if tour_bouton.draw(screen):
                placement_tour = True
        # Si le bouton de placement de tour est actif montre le bouton annuler 
        if placement_tour == True:
            #Affiche le curseur de la tour
            curseur_rect = tour_curseur.get_rect()
            curseur_pos = pg.mouse.get_pos()
            curseur_rect.center = curseur_pos
            if curseur_pos[0] < c.SCREEN_WIDTH and curseur_pos[1] < c.SCREEN_HEIGHT:
                screen.blit(tour_curseur, curseur_rect)
            if annuler_bouton.draw(screen):
                placement_tour = False
        #si une tour est sélectionné affiche le bouton ameliorer
        if selected_tour:
            #si une tour peut etre amélioré affiche le bouton ameliorer
            if selected_tour.upgrade_level < c.NIVEAU_MAX:
                if ameliorer_bouton.draw(screen):
                    if world.monnaie >= c.AMELIORER_COUT:
                        selected_tour.upgrade()
                        world.monnaie -= c.AMELIORER_COUT
            # Bouton annuler pour désélectionner la tour
            if annuler_bouton.draw(screen):
                selected_tour = None
                deselectionner_tour()
    else:
        pg.draw.rect(screen, "dodgerblue", (200, 200, 400, 200), border_radius=30)    
        if game_outcome == -1:
            draw_texte("GAME OVER", police_large, "grey0", 210, 230)
        elif game_outcome == 1:
            draw_texte("VICTOIRE !", police_large, "grey0", 210, 230)   
        # Recommence le niveau
        if recommencer_bouton.draw(screen):
            game_over = False
            niveau_commence = False
            placement_tour = False
            selected_tour = None
            dernier_ennemies_spawn = pg.time.get_ticks()
            world = World(ENNEMIES_SPAWN_DATA,map_image_grille_0)
            world.process_ennemies()
            #Vide les groupes
            ennemies_groupe.empty()
            tour_groupe.empty()
     




    # Gestion des événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # CLick de la souris
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            pos_souris = pg.mouse.get_pos()
            # Vérifier si la position de la souris est sur une case de la grille
            if pos_souris[0] < c.SCREEN_WIDTH and pos_souris[1] < c.SCREEN_HEIGHT:
                # Desélectionner la tour précédemment sélectionnée
                selected_tour = None
                deselectionner_tour()
                # Vérifier si la case est un emplacement interdit pour les tours
                if placement_tour == True:
                    if placement_interdit[pos_souris[1] // c.GRILLE][pos_souris[0] // c.GRILLE] == 1:
                        # Vérifier s'il n'y a pas déjà une tour à cet emplacement
                        emplacement_libre = True
                        for tour in tour_groupe:
                            if tour.rect.collidepoint(pos_souris):
                                emplacement_libre = False
                                break
                        # Si l'emplacement est libre, créer une tour
                        if emplacement_libre == True:
                            if placement_tour == True:
                                #Verifier si le joueur a assez de monnaie pour acheter la tour
                                if world.monnaie >= c.ACHETER_COUT:
                                    creer_tour(pos_souris)
                                    #Enleve de la monnaie si le joueur clique pour placer la tour
                                    world.monnaie -= c.ACHETER_COUT
                else:
                    selected_tour = selectionner_tour(pos_souris)

    #mise à jour des ennemis
    pg.display.flip()
pg.quit()









placement_interdit_3 = [
  (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
  (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
  (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1),
  (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
  (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
  (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
  (1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
  (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0),
  (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
  (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0),
  (1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0),
  (1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
  (1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
  (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
  (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
  ]


waypoints_3 = [
    (0*c.GRILLE, 7.5*c.GRILLE), 
    (2.5*c.GRILLE, 7.5*c.GRILLE),
    (3*c.GRILLE, 7.7*c.GRILLE),
    (3.3*c.GRILLE, 8*c.GRILLE),
    (3.5*c.GRILLE, 8.5*c.GRILLE), 

    (3.5*c.GRILLE, 11*c.GRILLE),
    (3.7*c.GRILLE, 11.5*c.GRILLE), 
    (4*c.GRILLE, 12*c.GRILLE),
    (4.5*c.GRILLE, 12.3*c.GRILLE),
    (5*c.GRILLE, 12.4*c.GRILLE),
    (5.5*c.GRILLE, 12.3*c.GRILLE),
    (6*c.GRILLE, 12*c.GRILLE),
    (6.4*c.GRILLE, 11.5*c.GRILLE),
    (6.6*c.GRILLE, 11*c.GRILLE),

    (6.6*c.GRILLE, 6.7*c.GRILLE),
    (6.4*c.GRILLE, 6.2*c.GRILLE),
    (6*c.GRILLE, 5.8*c.GRILLE),
    (5.5*c.GRILLE, 5.6*c.GRILLE),

    (4*c.GRILLE, 5.6*c.GRILLE),
    (3.5*c.GRILLE, 5.4*c.GRILLE),
    (3.2*c.GRILLE, 5.1*c.GRILLE),
    (3*c.GRILLE, 4.5*c.GRILLE),
    (3.2*c.GRILLE, 3.9*c.GRILLE),
    (3.5*c.GRILLE, 3.6*c.GRILLE),
    (4*c.GRILLE, 3.5*c.GRILLE),
    
    (8.5*c.GRILLE, 3.5*c.GRILLE),
    (9*c.GRILLE, 3.7*c.GRILLE),
    (9.3*c.GRILLE, 4.0*c.GRILLE),
    (9.5*c.GRILLE, 4.5*c.GRILLE),

    (9.5*c.GRILLE, 13*c.GRILLE),
    (9.6*c.GRILLE, 13.3*c.GRILLE),
    (10*c.GRILLE, 13.8*c.GRILLE),
    (10.5*c.GRILLE, 14.1*c.GRILLE),
    (11*c.GRILLE, 14.15*c.GRILLE),
    (11.5*c.GRILLE, 14.1*c.GRILLE),
    (12*c.GRILLE, 13.8*c.GRILLE),
    (12.4*c.GRILLE, 13.4*c.GRILLE),
    (12.6*c.GRILLE, 13*c.GRILLE),

    (12.6*c.GRILLE, 7.5*c.GRILLE),
    (12.7*c.GRILLE, 7.1*c.GRILLE),
    (13*c.GRILLE, 6.7*c.GRILLE),
    (13.5*c.GRILLE, 6.4*c.GRILLE),
    (16*c.GRILLE, 6.4*c.GRILLE),
    ]