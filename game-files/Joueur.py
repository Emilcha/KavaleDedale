from Global import *
from Armes import Arme

class Joueur:
    def __init__(self, game):
        self.game = game
        self.x = 0.0
        self.y = 0.0
        self.dirX = -1.0
        self.dirY = 0.0
        self.camPlaneX = 0
        self.camPlaneY = 0.66

        self.vie = 100

        self.stamina = 1
        self.canRun = True
        
        self.noclip = False

        self.isMoving = False
        self.isRunning = False
        #positionement vertical : HEIGHT-Hauteur fichier*scale+corection bobbing  
        self.arme = Arme(self.game, "main", "game-files/img/wep/main.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7)

    def getSpeed(self):
        if self.game.input.isPressed(self.game.settings["key_sprint"]) and self.canRun == True:
            self.isRunning = True
            self.stamina -= 0.01
            if self.stamina<=0:
                self.canRun = False
            return self.game.settings["move_speed_sprinting"]
        self.isRunning = False
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

    def get_angle_rad(self):
        return math.atan2(self.dirY, self.dirX)

    def get_angle_deg(self):
        return math.degrees(math.atan2(self.dirY, self.dirX)) % 360

    def update(self):
        if self.stamina<1:
            self.stamina += 0.005
        else:
            self.stamina = 1
            self.canRun = True

        self.isMoving = False
        if self.game.input.isPressed(self.game.settings["key_forward"]):
            self.goForward()
            self.isMoving = True
        if self.game.input.isPressed(self.game.settings["key_backward"]):
            self.goBackward()
            self.isMoving = True
        if self.game.input.isPressed(self.game.settings["key_right"]):
            self.lookRight()
        if self.game.input.isPressed(self.game.settings["key_left"]):
            self.lookLeft()

        if self.game.input.isPressed(self.game.settings["key_attack"]):
            self.attack()