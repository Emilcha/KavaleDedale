from Global import *
from Entity import Entity

class TrucMechant(Entity):
    def __init__(self, game, name, hp, pos):
        super().__init__(game, name, hp, pos, "game-files/img/ents/Momie1.png")
        self.dx = 0
        self.dy = 0
        self.next_random_move = random.randint(2,10)

    def move(self):
        if self.tick_count == 30:
            self.direction = random.random() * 2 * math.pi
            self.dx = math.cos(self.direction) / 10
            self.dy = math.sin(self.direction) / 10
            self.next_random_move = random.randint(2,10)
            self.tick_count = 0
        if self.tick_count > self.next_random_move:
            if self.game.carte[int(self.x + self.dx)][int(self.y)] == 0:
                self.x += self.dx
            else:
                self.direction = - self.direction
            
            if self.game.carte[int(self.x)][int(self.y + self.dy)] == 0:
                self.y += self.dy
            else:
                self.direction = - self.direction


class FantomeBizare(Entity):
    def __init__(self, game, name, hp, pos):
        super().__init__(game, name, hp, pos, None)
        self.texture_index = 0
        self.texture = [
            pygame.image.load("game-files/img/ents/FantomeAggro.png"),
            pygame.image.load("game-files/img/ents/FantomePassif.png")
        ]

    def get_texture(self):
        return self.texture[self.texture_index]

    def move(self):
        vec_y = self.y - self.game.joueur.y
        vec_x = self.x - self.game.joueur.x
        # Normaliser le vecteur
        vec_len = math.sqrt(vec_x**2 + vec_y**2)
        if vec_len>= 10:
            self.texture_index = 1
            return
        vec_x /= vec_len
        vec_y /= vec_len
        # Angle entre joueur et fanthomme
        ent_player_angle = math.degrees(math.atan2(vec_y, vec_x) - self.game.joueur.get_angle_rad()) % 360
        # Test deplacements
        if (ent_player_angle>10 and ent_player_angle<360-10):
            dx = self.game.joueur.x - self.x
            dy = self.game.joueur.y - self.y
            self.x += dx / 100
            self.y += dy / 100
            self.texture_index = 0
        else:
            self.texture_index = 1

    def attack(self):
        dx = self.game.joueur.x - self.x
        dy = self.game.joueur.y - self.y
        if math.sqrt(dx**2 + dy**2) < 0.4:
            self.game.joueur.vie -= 10
            self.game.ents.del_entity(self.name)
        
