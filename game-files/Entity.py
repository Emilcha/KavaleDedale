import random as rd
from Global import*

class Entity:
    def __init__(self, name, hp, monsterPos, game):
        self.game = game

        self.name = name
        self.health = MiniHealthbar(hp, self)
        self.content = []

        self.x = monsterPos[0]
        self.y = monsterPos[1]

        self.temp = 0
        self.alive = True
        self.isEnnemy = isEnnemy    #l'entite est une caisse ou un ennemi

    def kill(self):
        if healthPot in self.content:
            self.game.barre_de_vie.gagne_vie(50)   #cf barre_de_vie.py
        if weapon in self.content:
            #TODO armes
            pass
        self.alive = False
        del self

    def attack(self):
        if self.isEnnemy:
            if self.game.carte[self.x] == game.joueur.x and self.game.carte[self.y] == game.joueur.y
            or self.game.carte[self.x] == game.joueur.x and self.game.carte[self.y + 1] == game.joueur.y
            or self.game.carte[self.x] == game.joueur.x and self.game.carte[self.y - 1] == game.joueur.y
            or self.game.carte[self.x + 1] == game.joueur.x and self.game.carte[self.y] == game.joueur.y
            or self.game.carte[self.x - 1] == game.joueur.x and self.game.carte[self.y] == game.joueur.y
            or self.game.carte[self.x + 1] == game.joueur.x and self.game.carte[self.y + 1] == game.joueur.y
            or self.game.carte[self.x - 1] == game.joueur.x and self.game.carte[self.y - 1] == game.joueur.y
            or self.game.carte[self.x + 1] == game.joueur.x and self.game.carte[self.y - 1] == game.joueur.y
            or self.game.carte[self.x - 1] == game.joueur.x and self.game.carte[self.y + 1] == game.joueur.y:
                self.game.vie.perte_vie(10)

    def possibleMove(self, direction):
        if direction == up:
            if self.game.carte[self.y - 1][self.x] == 0:
                return True
        if direction == down:
            if self.game.carte[self.y + 1][self.x] == 0:
                return True
        if direction == left:
            if self.game.carte[self.y][self.x - 1] == 0:
                return True
        if direction == right:
            if self.game.carte[self.y][self.x + 1] == 0:
                return True
        return False

    def moving(self):
        directions = [up, down, left, right]
        to = random.choice(directions)
        while not possibleMove(to):
            to = random.choice(directions)
        if to == up:
            self.y -= 1
        if to == down:
            self.y += 1
        if to == left:
            self.x -= 1
        if to == right:
            self.x += 1

    def show(self):
        #TODO affichage de l'entite
        pass

    def update(self):
        self.temp += 1
        if self.health.hp == 0:
            self.kill()
        else:
            #self.show()
            self.health.update()
            if self.temp == 60:
                self.moving()
            if self.temp == 120:
                self.attack()
                self.temp = 0

class MiniHealthbar:
    def __init__(self, hp, entity):
        self.hpfull = hp
        self.hp = hp

        self.entity = entity

        self.edge = pygame.Rect(self.entity.y - 10, self.entity.x - 20, 50, 10)
        self.zone = pygame.Rect(self.entity.y - 9, self.entity.x - 19, 48, 8)
        self.touche = pygame.time.get_ticks()
        self.flash = pygame.time.get_ticks()

    def couleur(self):
        if self.hp <= self.hpfull//2:
            return (255, int((self.hp/50)*255), 0)
        return (int((1-(self.hp-50)/50)*255),255,0)

    def perte_vie(self, point):
        if self.hp > 0:
            self.hp -= point

    def update(self):
        while self.entity.alive:
            pygame.draw.rect(self.entity.game, (0, 0, 0), self.edge, 1)
            self.zone = pygame.Rect(self.entite.y - 10, (self.hp//100)*50, 10)
            pygame.draw.rect(self.entity.game, self.couleur(), self.zone)


        if event.type == pygame.MOUSEBUTTONDOWN and (pygame.time.get_ticks()-self.touche)>5000:
            self.perte_vie(10)
            self.touche = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - self.touche)<1200:
            if (pygame.time.get_ticks() - self.flash)<150:
                pygame.draw.rect(self.entity.game, (205,0,0), self.zone)
            if (pygame.time.get_ticks() - self.flash)>300:
                self.flash = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - self.touche)<1200:
            if (pygame.time.get_ticks() - self.flash)<150:
                pygame.draw.rect(self.entity.game, (205,0,0), self.zone)
            if (pygame.time.get_ticks() - self.flash)>300:
                self.flash = pygame.time.get_ticks()

        pygame.display.update()
