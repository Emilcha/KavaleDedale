from Global import *
from random import randint

class Arme:
    def __init__(self, game, name, texture_file, screen_pos, scale_factor, spread, max_distance, damage, cooldown):
        self.game = game
        self.name = name
        self.texture = pygame.transform.scale_by(pygame.image.load(texture_file), scale_factor)
        self.screen_pos = screen_pos
        self.spread = spread
        self.max_distance = max_distance
        self.damage = damage
        self.cooldown = cooldown

    def attack(self):
        ents = self.game.ents.entitys
        for ent in ents:
            if ent.drawn == False:
                continue
            vec_y = ent.y - self.game.joueur.y
            vec_x = ent.x - self.game.joueur.x
            if math.sqrt(vec_x**2 + vec_y**2) > self.max_distance:
                continue
            # Normaliser le vecteur
            vec_len = math.sqrt(vec_x**2 + vec_y**2)
            vec_x /= vec_len
            vec_y /= vec_len
            # Angle entre joueur et l'entité
            ent_player_angle = math.degrees(math.atan2(vec_y, vec_x) - self.game.joueur.get_angle_rad()) % 360
            if (ent_player_angle>self.spread and ent_player_angle<360-self.spread):
                continue
            
            ent.health -= self.damage
            if DEBUG:
                print(f"-{self.damage}hp: {ent.name} | restant: {ent.health}")


class Inventaire:
    def __init__(self):
        self.spartan = False
        self.zeus = False
        self.poseidon = False
        self.pot_vie = 0
        self.pot_stamina = 0
        self.pot_degat = 0

    def a_object(self, object):
        if object == 'Zeus':
            return self.zeus
        if object == 'Spartan':
            return self.spartan
        if object == 'Poseidon':
            return self.poseidon
        if object == 'Damage Potion':
            return self.pot_degat >= 0
        if object == 'Heal Potion':
            return self.pot_vie >= 0
        if object == 'Stamina Potion':
            return self.pot_stamina >= 0

    def ajouter(self, object):
        if object == 'Zeus':
            self.zeus = True
        if object == 'Spartan':
            self.spartan = True
        if object == 'Poseidon':
            self.poseidon = True
        if object == 'Damage Potion':
            self.pot_degat += 1
        if object == 'Heal Potion':
            self.pot_vie += 1
        if object == 'Stamina Potion':
            self.pot_stamina += 1