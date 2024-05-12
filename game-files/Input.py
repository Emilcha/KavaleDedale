from Global import *

class InputHandler:
    def __init__(self, game):
        self.game = game
        self.input_enabled = True
        self.keys = list(pygame.key.get_pressed())
        self.key_down_callback = {}
        self.key_up_callback = {}
        self.mouse_up_callback = {}

    def __convertKeyNum(self, num):
        # Corection index touches suite a une maj de pygame
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
                self.keys[keyCode] = True
                if keyCode in self.key_down_callback:
                    self.key_down_callback[keyCode]() # Appel d'un fonction lié a la touche

            elif event.type == pygame.KEYUP:
                keyCode = self.__convertKeyNum(event.key)
                self.keys[keyCode] = False
                if keyCode in self.key_up_callback:
                    self.key_up_callback[keyCode]() # Appel d'un fonction lié a la touche

            elif event.type == pygame.MOUSEBUTTONUP:
                for key, elm in self.mouse_up_callback.items():
                    if elm["key"]==event.button:
                        if elm["rect"].collidepoint(event.pos):
                            elm["callback"]() # Appel d'un fonction lié au clic a une certaine position


    def setKDownCallback(self, key, callback):
        key = self.__convertKeyNum(key)
        self.key_down_callback[key] = callback
    def removeKDownCallback(self, key):
        key = self.__convertKeyNum(key)
        if key in self.key_down_callback:
            del self.key_down_callback[key]

    def setKUpCallback(self, key, callback):
        key = self.__convertKeyNum(key)
        self.key_up_callback[key] = callback
    def removeKUpCallback(self, key):
        key = self.__convertKeyNum(key)
        if key in self.key_up_callback:
            del self.key_up_callback[key]

    def setMUpCallback(self, key, rect, callback):
        appendID = len(self.mouse_up_callback)
        self.mouse_up_callback[appendID] = {"key": key, "rect": rect, "callback": callback}
        return appendID

    def removeMUpCallback(self, idCb):
        self.mouse_up_callback[idCb]["callback"] = lambda: 0

    def isPressed(self, key):
        if self.input_enabled:
            key = self.__convertKeyNum(key)
            return self.keys[key]

    def isPressedBypass(self, key):
        key = self.__convertKeyNum(key)
        return self.keys[key]