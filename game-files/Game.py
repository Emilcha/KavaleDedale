from Global import *

from Render import Render
from Joueur import Joueur
from Settings import Settings
from Input import InputHandler
from HUD import HUD
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
        self.input.pollEvents()

        if self.isPlaying:          # Si aucun menu ouvert
            self.joueur.update()

    def rendu(self):
        self.renderer.rendu()
        self.renderer.add(self.hud.rendu())

    def changerMap(self, new_map, playerPos):
        self.carte = new_map
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

JeuLabyrinthe = Game(Maps.example,(6,6))
JeuLabyrinthe.gameLoop()
del JeuLabyrinthe