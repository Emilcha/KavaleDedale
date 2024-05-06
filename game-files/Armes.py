from Global import *

class Arme:
    def __init__(self, game, name, texture_file, screen_pos, scale_factor, spread, hitchance, max_distance, damage):
        self.game = game
        self.name = name
        self.texture = pygame.transform.scale_by(pygame.image.load(texture_file), scale_factor)
        self.screen_pos = screen_pos

    def attack(self):
        ents = self.game.ents.entitys
        for ent in ents:
            if ent.drawn == False:
                continue

            vec_y = ent.y - self.game.joueur.y
            vec_x = ent.x - self.game.joueur.x
            # Normaliser le vecteur
            vec_len = math.sqrt(vec_x**2 + vec_y**2)
            vec_x /= vec_len
            vec_y /= vec_len
            # Angle entre joueur et l'entité
            ent_player_angle = math.degrees(math.atan2(vec_y, vec_x) - self.game.joueur.get_angle_rad()) % 360

