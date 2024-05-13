import pygame
from pygame.locals import *
from HUDUtils import FontManager,Button
from math import *
from pygame.transform import *
from Global import *


#TODO --> YOU DIED GAME OVER

class GAME_OVER:
    def __init__(self,game):
        #pygame.init()
        self.window = game.pygame_screen
        self.game = game
        self.hauteur = HEIGHT
        self.largeur = WIDTH
        self.running = True


        #marqueurs de temps
        self.temps = pygame.time.get_ticks()
        self.chrono = pygame.time.get_ticks()
        self.temps_fondu = pygame.time.get_ticks()

        self.nombre_fondu = 0
        self.temoin = False

        #polices
        self.Lucida_Console = FontManager(fontName="Lucida Console", size=int(self.largeur/(19/2)))
        self.Consolas_Console = FontManager(fontName="Copperplate Gothic", size=int(self.largeur/16))
        self.button_console = FontManager(fontName="Tahoma", size=15)
        self.button_console.setEffects(1)

        #surface
        self.fondu = pygame.Surface((self.largeur,self.hauteur))
        self.image = pygame.image.load("img\ents\FantomeGAMEOVER.png")
        #self.ecran = self.game.pygame_screen
        self.nb = -200
        self.liste = ["G"," ","A"," ","M"," ","E"," "," ","O"," ","V"," ","E"," ","R"]
        self.gameover = ''
        self.image = pygame.transform.scale_by(self.image,2)

        #boutton
        self.NewLaby = Button(game,"Nouveau Laby",self.button_console, pygame.Color(20,200,20),pygame.Rect(int((self.largeur/2)-80),int(self.hauteur*(2/3)),160,65),self.nouveau_laby())
        self.quitter = Button(game,"Quitter Le Jeu",self.button_console, pygame.Color(240,0,32),pygame.Rect(int((self.largeur/2)+30),int(self.hauteur*(2/3))+100,160,65),self.quitGame())
        self.menu = Button(game,"Menu",self.button_console, pygame.Color(240,195,0),pygame.Rect(int((self.largeur/2)-190),int(self.hauteur*(2/3))+100,160,65),self.nouveau_laby) # y a t il un menu?
        self.bord_NewLaby = pygame.Rect(int((self.largeur/2)-80),int(self.hauteur*(2/3)),160,65)
        self.bord_quitter = pygame.Rect(int((self.largeur/2)+30),int(self.hauteur*(2/3))+100,160,65)
        self.bord_menu = pygame.Rect(int((self.largeur/2)-190),int(self.hauteur*(2/3))+100,160,65)

    def affichage_game_over(self):
        if int(self.largeur*(3/4))>(self.nb+100) > int(self.largeur/4):
            self.gameover = ''
            t = floor((((self.nb+100)-self.largeur/4)/(self.largeur/2))*17)
            for i in range(t):
                self.gameover += self.liste[i]


    def avancer(self):
        if (pygame.time.get_ticks()-self.temps)>0.1 and self.nb<(self.largeur+100):
            self.nb+=1
            self.temps = pygame.time.get_ticks()

    def nouveau_laby(self):
        self.game.nouveauLaby()
        self.running = False

    def quitGame(self):
        self.game.running = False
        self.running = False


    def update_fondu(self):
        if (pygame.time.get_ticks()-self.temps_fondu)>10 and self.nombre_fondu < 255:
                self.nombre_fondu += 0.005
                self.temps_fondu = pygame.time.get_ticks()
                if self.nombre_fondu>2.5:
                    self.nombre_fondu = 255
        self.fondu.set_alpha(self.nombre_fondu)
        if self.nombre_fondu == 255:
            self.temoin = True

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.rendu()
            pygame.display.update()


    def rendu(self):
        if not self.temoin :
            #self.window.blit(self.ecran,(0,0))
            self.update_fondu()
            self.window.blit(self.fondu,(0,0))
            self.Lucida_Console.textToSurface(self.window,
                f" Y O U  D I E D ",
                0, int(self.hauteur/4)-50,
                pygame.Color(149,0,0))
        if self.temoin :
            self.window.fill((0,0,0))
            self.Lucida_Console.textToSurface(self.window,
                f" Y O U  D I E D ",
                0, int(self.hauteur/4)-50,
                pygame.Color(149,0,0))
            self.affichage_game_over()
            self.Consolas_Console.textToSurface(self.window,
                f"{str(self.gameover)}",
                int(self.largeur/4), int(self.hauteur*3/6)-50,
                pygame.Color(1,49,180))
            self.avancer()
            self.window.blit(self.image,(self.nb,int(self.hauteur*2/6)-40))
            if self.nb == (self.largeur+100):
                self.NewLaby.draw(self.window)
                self.quitter.draw(self.window)
                self.menu.draw(self.window)
                pygame.draw.rect(self.window,(0,170,0),self.bord_NewLaby,4)
                pygame.draw.rect(self.window,(210,0,2),self.bord_quitter,4)
                pygame.draw.rect(self.window,(210,165,0),self.bord_menu,4)












##ressources
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)

##boucle de jeu

hauteur = 800
largeur = 1280


