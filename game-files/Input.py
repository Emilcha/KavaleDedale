from Global import *

class InputHandler:
    def __init__(self, game):
        self.game = game
        self.input_enabled = True
        self.keys = pygame.key.get_pressed()

    def pollEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN:
                self.keys[event.key] = True
                continue
            if event.type == pygame.KEYUP:
                self.keys[event.key] = False
                continue

    def isPressed(self, key):
        if self.input_enabled:
            return self.keys[key]

    def isPressedBypass(self, key):
        return self.keys[key]