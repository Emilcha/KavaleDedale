import pygame
from GenerationLaby import Labyrinthe
from time import time

class Minimap:
    def __init__(self, game, map_bloc, map_salles, taille):
        self.game = game
        self.map_bloc = map_bloc
        self.map_salles = map_salles
        self.scale = taille
        self.vue = [[False for j in range(len(self.map_bloc[0]))] for i in range(len(self.map_bloc))]

    def draw(self):
        block_width = self.scale
        block_height = self.scale
        surface = pygame.Surface((len(self.map_bloc[0])*block_width, len(self.map_bloc)*block_height))

        for h in range(len(self.map_bloc)):
            for w in range(len(self.map_bloc[0])):
                salle_h = h//10
                salle_w = w//10

                if "SAV" in self.map_salles[salle_h][salle_w]:
                    color = pygame.Color(200,20,200)
                elif "SPWN" in self.map_salles[salle_h][salle_w]:
                    color = pygame.Color(20,200,20)
                elif "S" in self.map_salles[salle_h][salle_w]:
                    color = pygame.Color(200,100,20)
                elif "C" in self.map_salles[salle_h][salle_w]:
                    color = pygame.Color(50,50,50)

                if self.map_bloc[h][w] == 0:
                    color //= pygame.Color(2, 2, 2)
                elif self.map_bloc[h][w] < 0:
                    color //= pygame.Color(4, 4, 4)

                if self.vue[salle_h][salle_w] == False:
                    color = pygame.Color(10,10,10)

                pygame.draw.rect(surface,
                    color,
                    (w*block_width,h*block_height,block_width,block_height))

        joueur_salle_y = int(self.game.joueur.x) // 10
        joueur_salle_x = int(self.game.joueur.y) // 10

        if self.vue[joueur_salle_y][joueur_salle_x] == False:
            self.vue[joueur_salle_y][joueur_salle_x] = True

        pygame.draw.rect(surface,
                    pygame.Color(255,255,0),
                    (
                        joueur_salle_x * 10 * block_width, joueur_salle_y * 10 * block_height,
                        10 * block_width, 10 * block_height
                    ),
                    width = 1)

        pygame.draw.rect(surface,
                    pygame.Color(255,255,255),
                    (int(self.game.joueur.y*block_width)-1,int(self.game.joueur.x*block_height)-1,2,2))
        return surface