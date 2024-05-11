from Global import *
from HUDUtils import FontManager, Button


class MenuESC:
    def __init__(self, game, hudSurface):
        self.game = game
        self.open = False
        self.hudSurface = hudSurface
        self.MenuFont = FontManager(fontName="Lucida Console", size=25)
        self.MenuFont.setEffects(bold=True, underline=True)

        self.SmallFont = FontManager(fontName="Lucida Console", size=18)

        self.NewLaby = Button(self.game, "Nouveau Laby", self.MenuFont, pygame.Color(20,200,20), pygame.Rect(WIDTH/2-100,HEIGHT-200,200,50), self.nouveau_laby)

        self.dbg_noclip_on  = Button(self.game, "ON", self.SmallFont, pygame.Color(20,200,20), pygame.Rect(WIDTH-150,50,50,40), self.dbg_noclip_turn_on)
        self.dbg_noclip_off = Button(self.game, "OFF", self.SmallFont, pygame.Color(200,20,20), pygame.Rect(WIDTH-100,50,50,40), self.dbg_noclip_turn_off)

        self.dbg_degats = Button(self.game, "-10hp", self.SmallFont, pygame.Color(200,20,20), pygame.Rect(WIDTH-150,100,100,40), self.dbg_degats_10)

        self.Quiter = Button(self.game, "Quiter", self.MenuFont, pygame.Color(200,20,20), pygame.Rect(WIDTH/2-50,HEIGHT-100,100,50), self.quitGame)

    def rendu(self):
        if self.open == True:
            self.hudSurface.fill(pygame.Color(0,0,0,150))

            self.MenuFont.textToSurfacePosCenter(self.hudSurface, "Menu Pause", WIDTH//2, 20, pygame.Color(255,255,255))
            self.NewLaby.draw(self.hudSurface)
            self.Quiter.draw(self.hudSurface)

            self.MenuFont.textToSurfacePosCenter(self.hudSurface, "DEBUG", WIDTH-100, 20, pygame.Color(255,255,255))
            self.SmallFont.textToSurfacePosCenter(self.hudSurface, "Noclip", WIDTH-100, 40, pygame.Color(255,255,255))
            self.dbg_noclip_on.draw(self.hudSurface)
            self.dbg_noclip_off.draw(self.hudSurface)
            self.dbg_degats.draw(self.hudSurface)

    def quitGame(self):
        if self.open:
            self.game.running = False

    def dbg_noclip_turn_on(self):
        if self.open:
            self.game.joueur.noclip = True
    def dbg_noclip_turn_off(self):
        if self.open:
            self.game.joueur.noclip = False
    def dbg_degats_10(self):
        if self.open:
            self.game.joueur.vie -= 10

    def nouveau_laby(self):
        if self.open:
            self.game.nouveauLaby()