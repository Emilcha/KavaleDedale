from Global import *

class Entity:
    def __init__(self, name, x, y, texture_file):
        self.name = name
        self.x = x
        self.y = y
        self.texture = pygame.image.load(texture_file)


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

    def index_sorted_dist(self, joueur):
        dist = {}
        for ent_index in range(len(self.entitys)):
            dist[ent_index] = ((joueur.x - self.entitys[ent_index].x) **2 + (joueur.y - self.entitys[ent_index].y) **2)

        # [(0, 0.2), (3, 1.4)]
        sorted_ent_index = [(key, dist) for key, dist in sorted(dist.items(), reverse=True, key=lambda item: item[1])]
        return sorted_ent_index