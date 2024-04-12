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

    def __del__(self):
        pygame.quit()

    def gameLoop(self):
        while(self.running):
            print("loop")
            self.update_ents()
            self.pygame_screen.fill(pygame.Color(0, 0, 0)) # TODO : Haut bleu, bas noir
            self.rendu()
            self.pygame_clock.tick(self.settings["maxfps"])
            pygame.display.update()

    def update_ents(self):
        self.joueur.update()

    def rendu(self):
        self.renderer.rendu()
        self.renderer.cpyHud(self.hud.rendu())
        


JeuLabyrinthe = Game(Maps.playground,(2,2))
JeuLabyrinthe.gameLoop()
del JeuLabyrinthe