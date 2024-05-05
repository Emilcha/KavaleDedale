from Global import *

class Entity:
    def __init__(self,game, name, hp, pos, texture_file):
        self.game = game
        
        self.name = name

        if texture_file != None:
            self.texture = pygame.image.load(texture_file)
        
        self.x = pos[0]
        self.y = pos[1]
        
        self.health = hp
        self.content = []

        self.tick_count = 0
        self.alive = True

    def get_texture(self):
        return self.texture

    def kill(self):
        self.alive = False

    def attack(self):
        pass

    def move(self):
        pass

    def update(self):
        self.tick_count += 1
        if self.health == 0:
            self.kill()
        else:
            self.move()


class Entity_Handler:
    def __init__(self):
        self.entitys = []

    def get_entity(self, name_or_index):
        if isinstance(name_or_index, str):
            for ent_index in range(len(entitys)):
                if self.entitys[ent_index].name == name:
                    return self.entitys[ent_index]

        if isinstance(name_or_index, int):
            return self.entitys[name_or_index]

    def add_entity(self, entity):
        self.entitys.append(entity)

    def del_entity(self, name):
        for ent_index in range(len(self.entitys)):
            if self.entitys[ent_index].name == name:
                self.entitys.pop(ent_index)

    def vider(self):
        self.entitys = []

    def index_sorted_dist(self, joueur):
        dist = {}
        for ent_index in range(len(self.entitys)):
            dist[ent_index] = ((joueur.x - self.entitys[ent_index].x) **2 + (joueur.y - self.entitys[ent_index].y) **2)

        # [(0, 0.2), (3, 1.4)]
        sorted_ent_index = [(key, dist) for key, dist in sorted(dist.items(), reverse=True, key=lambda item: item[1])]
        return sorted_ent_index
    
    def update_ents(self):
        for ent in self.entitys:
            ent.update()