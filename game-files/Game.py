from Global import *

from Render import Render
from Joueur import Joueur
from Settings import Settings
from Input import InputHandler
from HUD import HUD
from Entity import Entity_Handler, Entity
from Enemies import TrucMechant, FantomeBizare
from Object import Sortie
from GenerationLaby import Labyrinthe, LabyEnts
from Minimap import Minimap
from MenuDebut import MenuDebut
import Maps

class Game:
    def __init__(self, map_array, playerPos):
        #Initalisations
        pygame.init()
        pygame.display.init()
        pygame.display.set_mode((WIDTH, HEIGHT))
        self.pygame_screen = pygame.display.get_surface()
        self.pygame_clock = pygame.time.Clock()

        self.menuDebut = MenuDebut()

        self.settings = Settings()
        self.input = InputHandler(self)
        self.carte = map_array
        self.renderer = Render(self)

        self.joueur = Joueur(self)
        self.hud = HUD(self)
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

        self.ents = Entity_Handler()

        self.running = True
        self.isPlaying = True

    def __del__(self):
        # Pour que le jeu se ferme correctement
        pygame.quit()

    def gameLoop(self):
        # Boucle principale
        self.nouveauLaby()
        while(self.running):
            self.menuDebut.lancement()
            self.events()
            self.pygame_screen.fill(pygame.Color(0, 0, 0), rect=pygame.Rect(0, 0, WIDTH, HEIGHT//2))            # Couleur plafond
            self.pygame_screen.fill(pygame.Color(40, 40, 40), rect=pygame.Rect(0, HEIGHT//2, WIDTH, HEIGHT//2)) # Couleur sol
            self.rendu()
            self.pygame_clock.tick(self.settings["maxfps"]) # Limitation fps max
            pygame.display.update()

    def events(self):
        """
        Evenements : Gestion des entrées sorties, Mise a jour des joueur et des entitées
        """
        pygame.display.set_caption(f"Kavale: Dédale | FPS:{self.pygame_clock.get_fps() : .1f}")
        self.input.pollEvents()

        if self.isPlaying:          # Si aucun menu ouvert
            self.joueur.update()
            self.ents.update_ents()

    def rendu(self):
        """
        Rendu : Rendu du jeu (pseaudo 3D), Rendu des entitées (Sprites)
                Rendu des armes (Sprite), Rendu du HUD (et menus)
        """
        self.renderer.rendu()
        self.renderer.rendu_entite()
        self.renderer.rendu_armes()
        self.renderer.add(self.hud.rendu())

    def changerMap(self, new_map, playerPos):
        self.carte = new_map
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

    def nouveauLaby(self):
        #Réinitalisation de l'inventaire
        self.joueur.inv.__init__()
        #Supression des entitées
        self.ents.vider()
        #Création d'un nouveau labyrinthe
        laby = Labyrinthe(5,5)
        laby.genereLaby()
        #Generation des entitées du labyrinthe
        genEntite = LabyEnts(laby.afficheMapFinale(), self)
        #Reinitalisation de la minicarte
        if self.hud.minimap != None:
            del self.hud.minimap
        self.hud.minimap = Minimap(self, laby.afficheMapFinale(), laby.afficheMinimap(), 4)
        genEntite.gen_ents()
        case_depart = laby.getCaseDepart()
        #Changement de carte
        self.changerMap(genEntite.get_edited_map(),(case_depart[0]*10+5.5,case_depart[1]*10+5.5))
        # Placement du portail de fin
        case_fin = laby.getCaseFin()
        case_fin_type_salle = laby.afficheMinimap()[case_fin[0]][case_fin[1]]
        while case_fin_type_salle not in ["S1","S3","S4","C0","C1"]: # Salles ou le centre est libre
            case_fin = laby.getCaseFin()
            case_fin_type_salle = laby.afficheMinimap()[case_fin[0]][case_fin[1]]

        self.ents.add_entity(Sortie(self, (case_fin[0]*10+5,case_fin[1]*10+5)))

        del laby
        del genEntite
        



JeuLabyrinthe = Game(Maps.playground, (6,6))
JeuLabyrinthe.gameLoop()
del JeuLabyrinthe