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

    def getSpeed(self):
        '''
        if self.game.input.isPressed(self.game.settings["key_sprint"]):
            return self.game.settings["move_speed_sprinting"]
        else:
        '''
        return self.game.settings["move_speed"]

    def goForward(self):
        speed = self.getSpeed()
        if self.game.carte[int(self.x + self.dirX * speed)][int(self.y)] == 0:
            self.x += self.dirX * speed
        if self.game.carte[int(self.x)][int(self.y + self.dirY * speed)] == 0:
            self.y += self.dirY * speed
                
    def goBackward(self):
        speed = self.getSpeed()
        if self.game.carte[int(self.x - self.dirX * speed)][int(self.y)] == 0:
            self.x -= self.dirX * speed
        if self.game.carte[int(self.x)][int(self.y - self.dirY * speed)] == 0:
            self.y -= self.dirY * speed

    def lookLeft(self):
        oldDirX = self.dirX
        self.dirX = self.dirX * math.cos(self.game.settings["rotate_speed"]) - self.dirY * math.sin(self.game.settings["rotate_speed"])
        self.dirY = oldDirX * math.sin(self.game.settings["rotate_speed"]) + self.dirY * math.cos(self.game.settings["rotate_speed"])
        
        oldPlaneX = self.camPlaneX
        self.camPlaneX = self.camPlaneX * math.cos(self.game.settings["rotate_speed"]) - self.camPlaneY * math.sin(self.game.settings["rotate_speed"])
        self.camPlaneY = oldPlaneX * math.sin(self.game.settings["rotate_speed"]) + self.camPlaneY * math.cos(self.game.settings["rotate_speed"])

    def lookRight(self):
        oldDirX = self.dirX
        self.dirX = self.dirX * math.cos(-self.game.settings["rotate_speed"]) - self.dirY * math.sin(-self.game.settings["rotate_speed"])
        self.dirY = oldDirX * math.sin(-self.game.settings["rotate_speed"]) + self.dirY * math.cos(-self.game.settings["rotate_speed"])
        
        oldPlaneX = self.camPlaneX
        self.camPlaneX = self.camPlaneX * math.cos(-self.game.settings["rotate_speed"]) - self.camPlaneY * math.sin(-self.game.settings["rotate_speed"])
        self.camPlaneY = oldPlaneX * math.sin(-self.game.settings["rotate_speed"]) + self.camPlaneY * math.cos(-self.game.settings["rotate_speed"])

    def attack(self):
        pass

    def update(self):
        if self.game.input.isPressed(self.game.settings["key_forward"]):
            self.goForward()
        if self.game.input.isPressed(self.game.settings["key_backward"]):
            self.goBackward()
        if self.game.input.isPressed(self.game.settings["key_right"]):
            self.lookRight()
        if self.game.input.isPressed(self.game.settings["key_left"]):
            self.lookLeft()
        if self.game.input.isPressed(self.game.settings["key_attack"]):
            self.attack()