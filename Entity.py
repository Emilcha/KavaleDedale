##Imports
# import pygame
# from pygame.locals import *
import random as rd
from MiniHealthbar import MiniHealthbar
from Global import*
# from Game import Game
# from Joueur import Joueur

##TODO
'''
Par exemple a rajouter dans Game.py:
self.caisse = Entity(100, False, (50,50), self)
Ou faire une methode pour faire spawn les entites
'''
'''
A rajouter dans Settings.py defaults():
self.settings ["vie"] = barre_de_vie(niveau)
OR
A rajouter dans Game.py __init__():
self.vie = barre_de_vie(niveau)
'''

##Class
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
        self.isEnnemy = False    #l'entite est une caisse ou un ennemi

    def kill(self):
         
        """         
        if healthPot in self.content:
            self.game.barre_de_vie.gagne_vie(50)   #cf barre_de_vie.py
        if weapon in self.content:
            #TODO armes
            pass 
        """
        self.alive = False
        del self

    def attack(self):
        if self.isEnnemy:
            if (self.game.carte[self.x] == self.game.joueur.x and self.game.carte[self.y] == self.game.joueur.y) or (self.game.carte[self.x] == self.game.joueur.x and self.game.carte[self.y + 1] == self.game.joueur.y) or (self.game.carte[self.x] == self.game.joueur.x and self.game.carte[self.y - 1] == self.game.joueur.y) or (self.game.carte[self.x + 1] == self.game.joueur.x and self.game.carte[self.y] == self.game.joueur.y) or (self.game.carte[self.x - 1] == self.game.joueur.x and self.game.carte[self.y] == self.game.joueur.y) or (self.game.carte[self.x + 1] == self.game.joueur.x and self.game.carte[self.y + 1] == self.game.joueur.y) or (self.game.carte[self.x - 1] == self.game.joueur.x and self.game.carte[self.y - 1] == self.game.joueur.y) or (self.game.carte[self.x + 1] == self.game.joueur.x and self.game.carte[self.y - 1] == self.game.joueur.y) or (self.game.carte[self.x - 1] == self.game.joueur.x and self.game.carte[self.y + 1] == self.game.joueur.y):
                self.game.vie.perte_vie(10)

    def possibleMove(self, direction):
        if direction == 'up':
            if self.game.carte[self.y - 1][self.x] == 0:
                return True
        if direction == 'down':
            if self.game.carte[self.y + 1][self.x] == 0:
                return True
        if direction == 'left':
            if self.game.carte[self.y][self.x - 1] == 0:
                return True
        if direction == 'right':
            if self.game.carte[self.y][self.x + 1] == 0:
                return True
        return False

    def moving(self):
        directions = ['up', 'down', 'left', 'right']
        to = rd.choice(directions)
        while not self.possibleMove(to):
            to = rd.choice(directions)
        if to == 'up':
            self.y -= 1
        if to == 'down':
            self.y += 1
        if to == 'left':
            self.x -= 1
        if to == 'right':
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
