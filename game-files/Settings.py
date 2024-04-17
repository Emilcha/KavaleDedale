from Global import *

class Settings:
    def __init__(self):
        self.settings = {}
        self.defaults()

    def __getitem__(self, key):
        if self.settings[key]:
            val = self.settings[key]
            return val

    def __setitem__(self, key, val):
        self.settings[key] = val

    def defaults(self):
        #Default settings
        self.settings["maxfps"]         = 60
        self.settings["movespeed"]      = 0.1
        self.settings["rotatespeed"]    = 0.05
        self.settings["key_forward"]    = pygame.K_z
        self.settings["key_backward"]   = pygame.K_s
        self.settings["key_right"]      = pygame.K_d
        self.settings["key_left"]       = pygame.K_q
        self.settings["key_attack"]     = pygame.K_SPACE