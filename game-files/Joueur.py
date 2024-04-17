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

    def goForward(self):
        if self.game.carte[int(self.x + self.dirX * self.game.settings["movespeed"])][int(self.y)] == 0:
            self.x += self.dirX * self.game.settings["movespeed"]
        if self.game.carte[int(self.x)][int(self.y + self.dirY * self.game.settings["movespeed"])] == 0:
            self.y += self.dirY * self.game.settings["movespeed"]
                
    def goBackward(self):
        if self.game.carte[int(self.x - self.dirX * self.game.settings["movespeed"])][int(self.y)] == 0:
            self.x -= self.dirX * self.game.settings["movespeed"]
        if self.game.carte[int(self.x)][int(self.y - self.dirY * self.game.settings["movespeed"])] == 0:
            self.y -= self.dirY * self.game.settings["movespeed"]

    def goLeft(self):
        oldDirX = self.dirX
        self.dirX = self.dirX * math.cos(self.game.settings["rotatespeed"]) - self.dirY * math.sin(self.game.settings["rotatespeed"])
        self.dirY = oldDirX * math.sin(self.game.settings["rotatespeed"]) + self.dirY * math.cos(self.game.settings["rotatespeed"])
        
        oldPlaneX = self.camPlaneX
        self.camPlaneX = self.camPlaneX * math.cos(self.game.settings["rotatespeed"]) - self.camPlaneY * math.sin(self.game.settings["rotatespeed"])
        self.camPlaneY = oldPlaneX * math.sin(self.game.settings["rotatespeed"]) + self.camPlaneY * math.cos(self.game.settings["rotatespeed"])

    def goRight(self):
        oldDirX = self.dirX
        self.dirX = self.dirX * math.cos(-self.game.settings["rotatespeed"]) - self.dirY * math.sin(-self.game.settings["rotatespeed"])
        self.dirY = oldDirX * math.sin(-self.game.settings["rotatespeed"]) + self.dirY * math.cos(-self.game.settings["rotatespeed"])
        
        oldPlaneX = self.camPlaneX
        self.camPlaneX = self.camPlaneX * math.cos(-self.game.settings["rotatespeed"]) - self.camPlaneY * math.sin(-self.game.settings["rotatespeed"])
        self.camPlaneY = oldPlaneX * math.sin(-self.game.settings["rotatespeed"]) + self.camPlaneY * math.cos(-self.game.settings["rotatespeed"])

    def attack(self):
        pass

    def update(self):
        if self.game.input.isPressed(self.game.settings["key_forward"]):
            self.goForward()
        if self.game.input.isPressed(self.game.settings["key_backward"]):
            self.goBackward()
        if self.game.input.isPressed(self.game.settings["key_right"]):
            self.goRight()
        if self.game.input.isPressed(self.game.settings["key_left"]):
            self.goLeft()
        if self.game.input.isPressed(self.game.settings["key_attack"]):
            self.attack()