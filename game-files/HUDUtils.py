from Global import *

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

    def textToSurfacePosCenter(self, surface, text, x, y, color, background=None):
        fontSurface = self.font.render(text, self.antialiasing, color, background)

        surface.blit(fontSurface, (x - fontSurface.get_width()//2, y - fontSurface.get_height()//2))


class Button:
    def __init__(self, game, text, font: FontManager, color: pygame.Color, rect: pygame.Rect, callback):
        self.text = text
        self.font = font
        self.rect = rect
        self.color = color
        self.game = game
        self.callbackID = self.game.input.setMUpCallback(1, self.rect, callback)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.font.textToSurfacePosCenter(surface, self.text, 
            self.rect.x + self.rect.w//2, self.rect.y + self.rect.h//2,
            pygame.Color(255,255,255))
