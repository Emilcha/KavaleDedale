from Global import *

class Joueur:
    def __init__(self, game):
        self.game = game
        self.x = 0.0
        self.y = 0.0
        self.dirX = -1.0
        self.dirY = 0.0
        self.angle = 0
        self.camPlaneX = 0
        self.camPlaneY = 0.66
        self.move_speed = 0.1
        self.rotate_speed = 0.05

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            if self.game.carte[int(self.x + self.dirX * self.move_speed)][int(self.y)] == 0:
                self.x += self.dirX * self.move_speed
            if self.game.carte[int(self.x)][int(self.y + self.dirY * self.move_speed)] == 0:
                self.y += self.dirY * self.move_speed
                
        if keys[pygame.K_s]:
            if self.game.carte[int(self.x - self.dirX * self.move_speed)][int(self.y)] == 0:
                self.x -= self.dirX * self.move_speed
            if self.game.carte[int(self.x)][int(self.y - self.dirY * self.move_speed)] == 0:
                self.y -= self.dirY * self.move_speed
                
        if keys[pygame.K_q]:
            oldDirX = self.dirX
            self.dirX = self.dirX * math.cos(self.rotate_speed) - self.dirY * math.sin(self.rotate_speed)
            self.dirY = oldDirX * math.sin(self.rotate_speed) + self.dirY * math.cos(self.rotate_speed)
            
            oldPlaneX = self.camPlaneX
            self.camPlaneX = self.camPlaneX * math.cos(self.rotate_speed) - self.camPlaneY * math.sin(self.rotate_speed)
            self.camPlaneY = oldPlaneX * math.sin(self.rotate_speed) + self.camPlaneY * math.cos(self.rotate_speed)

        if keys[pygame.K_d]:
            oldDirX = self.dirX
            self.dirX = self.dirX * math.cos(-self.rotate_speed) - self.dirY * math.sin(-self.rotate_speed)
            self.dirY = oldDirX * math.sin(-self.rotate_speed) + self.dirY * math.cos(-self.rotate_speed)
            
            oldPlaneX = self.camPlaneX
            self.camPlaneX = self.camPlaneX * math.cos(-self.rotate_speed) - self.camPlaneY * math.sin(-self.rotate_speed)
            self.camPlaneY = oldPlaneX * math.sin(-self.rotate_speed) + self.camPlaneY * math.cos(-self.rotate_speed)