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

        self.canRun = True
        self.stamina = 1
        self.noclip = False

    def getSpeed(self):
        if self.game.input.isPressed(self.game.settings["key_sprint"]) and self.canRun == True:
            self.stamina -= 0.01
            if self.stamina<=0:
                self.canRun = False
            return self.game.settings["move_speed_sprinting"]
        return self.game.settings["move_speed"]

    def goForward(self):
        speed = self.getSpeed()
        if not (int(self.x + self.dirX * speed)<0 or int(self.x + self.dirX * speed)>=len(self.game.carte)):
            if self.game.carte[int(self.x + self.dirX * speed)][int(self.y)] == 0 or self.noclip:
                self.x += self.dirX * speed
        if not (int(self.y + self.dirY * speed)<0 or int(self.y + self.dirY * speed)>=len(self.game.carte[int(self.x)])):
            if self.game.carte[int(self.x)][int(self.y + self.dirY * speed)] == 0 or self.noclip:
                self.y += self.dirY * speed
                
    def goBackward(self):
        speed = self.getSpeed()
        if not (int(self.x - self.dirX * speed)<0 or int(self.x - self.dirX * speed)>=len(self.game.carte)):
            if self.game.carte[int(self.x - self.dirX * speed)][int(self.y)] == 0 or self.noclip:
                self.x -= self.dirX * speed
        if not (int(self.y - self.dirY * speed)<0 or int(self.y - self.dirY * speed)>=len(self.game.carte[int(self.x)])):
            if self.game.carte[int(self.x)][int(self.y - self.dirY * speed)] == 0 or self.noclip:
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
        if self.stamina<1:
            self.stamina += 0.005
        else:
            self.stamina = 1
            self.canRun = True


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