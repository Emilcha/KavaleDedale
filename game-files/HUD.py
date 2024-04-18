from Global import *

class HUD:
    def __init__(self, game):
        self.game = game
        self.hudSurface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
        self.DemoFont = FontManager(fontName="Lucida Console", size=25)
        self.DemoText = TextManager(self.DemoFont, "Hello Wold", pygame.Color(255,255,255))

    def getSurface(self):
        return self.hudSurface

    def rendu(self):
        self.hudSurface.fill(pygame.Color(0,0,0,0))
        self.DemoText.drawText(self.hudSurface, 0, 0)
        return self.hudSurface

class FontManager:
    def __init__(self, fontName=None, fontFile=None, size=20, antialiasing=True):
        if fontName != None:
            self.font = pygame.font.SysFont(fontName, size)
        elif fontFile != None:
            self.font = pygame.font.Font(fontFile, size)
        else:
            return self.__del__()

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

    def getSurface(self, text, color, background):
        return self.font.render(text, self.antialiasing, color, background)

class TextManager:
    def __init__(self, font, text, color, background=None):
        self.font = font
        self.text = text
        self.color = color
        self.background = background

        self.rendered_text = self.font.getSurface(self.text, self.color, self.background)

    def drawText(self, surface, x, y):
        surface.blit(self.rendered_text, (x,y))

    def renderText(self):
        self.rendered_text = self.font.getSurface(self.text, self.color, self.background)