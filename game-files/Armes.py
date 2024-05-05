from Global import *

class Arme:
    def __init__(self, game, name, texture_file, screen_pos, scale_factor):
        self.texture = pygame.transform.scale_by(pygame.image.load(texture_file), scale_factor)
        self.screen_pos = screen_pos