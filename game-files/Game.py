from Global import *

from Render import Render
from Joueur import Joueur
import Maps

class Game:
    def __init__(self, map_array, playerPos):
        pygame.init()
        pygame.display.init()
        pygame.display.set_mode((WIDTH, HEIGHT))
        self.pygame_screen = pygame.display.get_surface()
        self.pygame_clock = pygame.time.Clock()

        self.carte = map_array
        self.renderer = Render(self)
        self.joueur = Joueur(self)
        self.joueur.x = playerPos[0]
        self.joueur.y = playerPos[1]

        self.running = True
        self.max_fps = 60

    def __del__(self):
        pygame.quit()

    def gameLoop(self):
        while(self.running):
            self.event_dispatcher()
            self.pygame_screen.fill(pygame.Color(0, 0, 0)) # TODO : Haut bleu, bas noir
            self.renderer.rendu()
            self.pygame_clock.tick(self.max_fps)
            pygame.display.update()

    def event_dispatcher(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.joueur.update()


JeuLabyrinthe = Game(Maps.playground,(2,2))
JeuLabyrinthe.gameLoop()
del JeuLabyrinthe