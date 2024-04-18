from Global import *

class InputHandler:
    def __init__(self, game):
        self.game = game
        self.input_enabled = True
        self.keys = list(pygame.key.get_pressed())

    def __convertKeyNum(self, num):
        # https://github.com/pygame/pygame/blob/main/src_c/key.c -> pg_key_and_name[]
        if num >= 1073741881:
            num -= 1073741881 - 128
        return num

    def pollEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                keyCode = self.__convertKeyNum(event.key)
                print("up", keyCode)
                self.keys[keyCode] = True

            elif event.type == pygame.KEYUP:
                keyCode = self.__convertKeyNum(event.key)
                print("down", keyCode)
                self.keys[keyCode] = False

    def isPressed(self, key):
        if self.input_enabled:
            key = self.__convertKeyNum(key)
            return self.keys[key]

    def isPressedBypass(self, key):
        key = self.__convertKeyNum(key)
        return self.keys[key]