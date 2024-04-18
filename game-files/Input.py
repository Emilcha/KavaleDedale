from Global import *

class InputHandler:
    def __init__(self, game):
        self.game = game
        self.input_enabled = True
        self.keys = list(pygame.key.get_pressed())

    def __convertKeyNum(self, num):
        # https://github.com/pygame/pygame/blob/main/src_c/key.c -> pg_key_and_name[]
        if num >= 1073741881:
            num -= 1073742009   # 1073741881 + 128

    def pollEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                continue
            if event.type == pygame.KEYDOWN:
                print("up", event.key)
                self.keys[event.key] = True
                continue
            if event.type == pygame.KEYUP:
                print("down", event.key)
                self.keys[event.key] = False
                continue

    def isPressed(self, key):
        if self.input_enabled:
            return self.keys[key]

    def isPressedBypass(self, key):
        return self.keys[key]