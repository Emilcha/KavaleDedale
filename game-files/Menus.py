from Global import *
from HUDUtils import FontManager, Button


class MenuESC:
    def __init__(self, game, hudSurface):
        self.game = game
        self.open = False
        self.hudSurface = hudSurface
        self.MenuFont = FontManager(fontName="Lucida Console", size=25)
        self.MenuFont.setEffects(bold=True, underline=True)
        self.Quiter = Button(self.game, "Quiter", self.MenuFont, pygame.Color(200,20,20), pygame.Rect(WIDTH/2-50,HEIGHT-100,100,50), self.quitGame)
    def rendu(self):
        if self.open == True:
            self.hudSurface.fill(pygame.Color(0,0,0,150))
            self.MenuFont.textToSurfacePosCenter(self.hudSurface, "Menu Pause", WIDTH//2, 20, pygame.Color(255,255,255))
            self.Quiter.draw(self.hudSurface)

    def quitGame(self):
        self.game.running = False
