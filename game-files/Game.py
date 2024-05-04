from Global import *

from Render import Render
from Joueur import Joueur
from Settings import Settings
from Input import InputHandler
from HUD import HUD
from Entity import Entity_Handler, Entity
from Enemies import TrucMechant, FantomeBizare
from GenerationLaby import Labyrinthe, LabyEnts
import Maps

class Game:
    def __init__(self, map_array, playerPos):
        pygame.init()
        pygame.display.init()
        pygame.display.set_mode((WIDTH, HEIGHT))
        self.pygame_screen = pygame.display.get_surface()
        self.pygame_clock = pygame.time.Clock()

        self.settings = Settings()
        self.input = InputHandler(self)
        self.carte = map_array
        self.renderer = Render(self)

        self.joueur = Joueur(self)
        self.hud = HUD(self)
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

        self.ents = Entity_Handler()

        for i in range(10):
            self.ents.add_entity(TrucMechant(self, f"pasgentil{i}", 100, (4, 5)))
		
        #self.ents.add_entity(FantomeBizare(self, "fanthome", 20, (4, 5)))
        #self.ents.add_entity(TrucMechant(self, "pasgentil", 100, (4, 5)))
        self.running = True
        self.isPlaying = True

    def __del__(self):
        pygame.quit()

    def gameLoop(self):
        while(self.running):
            self.events()
            self.pygame_screen.fill(pygame.Color(0, 0, 0), rect=pygame.Rect(0, 0, WIDTH, HEIGHT//2))
            self.pygame_screen.fill(pygame.Color(40, 40, 40), rect=pygame.Rect(0, HEIGHT//2, WIDTH, HEIGHT//2))
            self.rendu()
            self.pygame_clock.tick(self.settings["maxfps"])
            pygame.display.update()

    def events(self):
        pygame.display.set_caption(f"{self.pygame_clock.get_fps() : .1f}")
        self.input.pollEvents()

        if self.isPlaying:          # Si aucun menu ouvert
            self.joueur.update()
            self.ents.update_ents()

    def rendu(self):
        self.renderer.rendu()
        self.renderer.rendu_entite()
        self.renderer.add(self.hud.rendu())

    def changerMap(self, new_map, playerPos):
        self.carte = new_map
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

    def nouveauLaby(self):
        self.ents.vider()

        laby = Labyrinthe(4,4)
        laby.genereLaby()

        genEntite = LabyEnts(laby.getMap(), self)
        del laby

        genEntite.gen_ents()

        self.changerMap(genEntite.get_edited_map(),(1,1))

        del genEntite
        



JeuLabyrinthe = Game(Maps.rooms, (6,6))
JeuLabyrinthe.gameLoop()
del JeuLabyrinthe