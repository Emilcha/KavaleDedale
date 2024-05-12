from Global import *
from Armes import Arme, Inventaire

class Joueur:
    def __init__(self, game):
        # Initalisation des variables du joueur et de l'inventaire et de l'arme
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
        self.arme = Arme(self.game, "Poing", "game-files/img/wep/poing.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7, 10, 1, 10, 10)
        self.frames_since_last_attack = 0
        self.inv = Inventaire()

    def getSpeed(self):
        """
        Renvoie la vitesse a laquel faire avancer le joueur en fonction du stamina et de la touche pour courir
        """
        if self.game.input.isPressed(self.game.settings["key_sprint"]) and self.canRun == True:
            self.isRunning = True
            self.stamina -= 0.01
            if self.stamina<=0:
                self.canRun = False
            return self.game.settings["move_speed_sprinting"]
        self.isRunning = False
        return self.game.settings["move_speed"]

    def goForward(self):
        # Trigonometrie (self.dirX = cos(angle du joueur)) (self.dirY = sin(angle du joueur))
        # Test colision : Tester si un mur ou si en dehorse de la carte a la position d'arrivé
        speed = self.getSpeed()
        if not (int(self.x + self.dirX * speed)<0 or int(self.x + self.dirX * speed)>=len(self.game.carte)):
            if self.game.carte[int(self.x + self.dirX * speed)][int(self.y)] == 0 or self.noclip:
                self.x += self.dirX * speed
        if not (int(self.y + self.dirY * speed)<0 or int(self.y + self.dirY * speed)>=len(self.game.carte[int(self.x)])):
            if self.game.carte[int(self.x)][int(self.y + self.dirY * speed)] == 0 or self.noclip:
                self.y += self.dirY * speed
                
    def goBackward(self):
        # Similaire a goForward()
        speed = self.getSpeed()
        if not (int(self.x - self.dirX * speed)<0 or int(self.x - self.dirX * speed)>=len(self.game.carte)):
            if self.game.carte[int(self.x - self.dirX * speed)][int(self.y)] == 0 or self.noclip:
                self.x -= self.dirX * speed
        if not (int(self.y - self.dirY * speed)<0 or int(self.y - self.dirY * speed)>=len(self.game.carte[int(self.x)])):
            if self.game.carte[int(self.x)][int(self.y - self.dirY * speed)] == 0 or self.noclip:
                self.y -= self.dirY * speed

    def lookLeft(self):
        # Rotation de la camera (direction et plan)
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
        # Appel de la fonction attack de l'arme en verifiant si le temp d'attente le permet
        if self.frames_since_last_attack > self.arme.cooldown:
            self.arme.attack()
            self.frames_since_last_attack = 0

    def get_angle_rad(self):
        # angle = atan2(sin(angle),cos(angle))
        return math.atan2(self.dirY, self.dirX)

    def get_angle_deg(self):
        # convertion en degrées
        return math.degrees(math.atan2(self.dirY, self.dirX)) % 360

    def update(self):
        # Mise a jour de la quantité de stamina
        if self.stamina<1:
            self.stamina += 0.005
        else:
            self.stamina = 1
            self.canRun = True
            
        self.frames_since_last_attack += 1


        # Test touches pour le mouvment
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

        # Touches changement d'armes
        if self.game.input.isPressed(self.game.settings["key_poing"]):
            self.arme = Arme(self.game, "Poing", "game-files/img/wep/poing.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7, 20, 1, 10, 20)

        if self.game.input.isPressed(self.game.settings["key_epee"]):
            if self.inv.a_object('Spartan'):
                self.arme = Arme(self.game, "Epee", "game-files/img/wep/epee.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7, 25, 2, 15, 30)

        if self.game.input.isPressed(self.game.settings["key_zeus"]):
            if self.inv.a_object('Zeus'):
                self.arme = Arme(self.game, "Zeus", "game-files/img/wep/zeus.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7, 10, 5, 15, 45)

        if self.game.input.isPressed(self.game.settings["key_poseidon"]):
            if self.inv.a_object('Poseidon'):
                self.arme = Arme(self.game, "Poseidon", "game-files/img/wep/trident.png", ((WIDTH//5)*3, HEIGHT-79*7+10), 7, 15, 2.5, 20, 60)

        # Touche pour attaquer
        if self.game.input.isPressed(self.game.settings["key_attack"]):
            self.attack()