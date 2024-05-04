from Global import *
from HUDUtils import FontManager
from Menus import MenuESC

class HUD:
    def __init__(self, game):
        self.game = game
        self.hudSurface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)

        self.menu = MenuESC(game, self.hudSurface)

        self.game.input.setKDownCallback(pygame.K_ESCAPE, self.toucheMenu)

        self.Lucida_Console = FontManager(fontName="Lucida Console", size=25)

    def getSurface(self):
        return self.hudSurface

    def toucheMenu(self):
        self.game.input.input_enabled = not self.game.input.input_enabled
        self.menu.open = not self.menu.open
        self.game.isPlaying = not self.game.isPlaying

    def rendu(self):
        self.hudSurface.fill(pygame.Color(0,0,0,0))

        self.Lucida_Console.textToSurface(self.hudSurface,
            f"ANGLE° | {str(self.game.joueur.get_angle_deg())}",
            0, HEIGHT - 175,
            pygame.Color(10,255,120))
        self.Lucida_Console.textToSurface(self.hudSurface,
            f"X | {str(self.game.joueur.x)}",
            0, HEIGHT - 150,
            pygame.Color(10,255,120))
        self.Lucida_Console.textToSurface(self.hudSurface,
            f"Y | {str(self.game.joueur.y)}",
            0, HEIGHT - 125,
            pygame.Color(10,255,120))
        self.Lucida_Console.textToSurface(self.hudSurface,
            f"Stamina | {str(int(self.game.joueur.stamina * 100))}",
            0, HEIGHT - 100,
            pygame.Color(10,255,120))
        

        #TODO: Barre de vie rendu -> blit sur hudSurface


        self.menu.rendu()

        return self.hudSurface