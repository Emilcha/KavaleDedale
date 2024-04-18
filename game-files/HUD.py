from Global import *

class HUD:
    def __init__(self, game):
        self.game = game
        self.hudSurface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
        self.Lucida_Console = FontManager(fontName="Lucida Console", size=25)

    def getSurface(self):
        return self.hudSurface

    def rendu(self):
        self.hudSurface.fill(pygame.Color(0,0,0,0))

        self.Lucida_Console.textToSurface(self.hudSurface,
            f"Stamina | {str(int(self.game.joueur.stamina * 100))}",
            0, 0,
            pygame.Color(10,255,120))

        return self.hudSurface

class FontManager:
    def __init__(self, fontName=None, fontFile=None, size=20, antialiasing=True):
        if fontName != None:
            self.font = pygame.font.SysFont(fontName, size)
        elif fontFile != None:
            self.font = pygame.font.Font(fontFile, size)
        else:
            del self
            return

        self.antialiasing = antialiasing

    def setEffects(self, bold=None, italic=None, underline=None, striketrough=None):
        if bold != None:
            self.font.bold = bold
        if italic != None:
            self.font.italic = italic
        if underline != None:
            self.font.underline = underline
        if striketrough != None:
            self.font.striketrough = striketrough

    def textToSurface(self, surface, text, x, y, color, background=None):
        fontSurface = self.font.render(text, self.antialiasing, color, background)
        surface.blit(fontSurface, (x, y))