import pygame
from pygame.locals import *
from HUDUtils import FontManager,Button
from math import *
from Global import *
# TODO -->  YOU WIN

class VICTORY:
    def __init__(self,hauteur,largeur,game):
        pygame.init()
        self.window = pygame.display.set_mode((largeur,hauteur))
        self.game = game
        self.hauteur = hauteur
        self.largeur = largeur
        self.running = True

        self.color = (255,215,0)
        self.color2 = (255,255,255)
        #marqueur de temps
        self.temps = pygame.time.get_ticks()

        #image
        self.kavale = pygame.image.load("img/icon/Logo.png")
        self.kavale = pygame.transform.scale_by(self.kavale,4)
        self.momie = pygame.image.load("img/ents/momiemorte.png")
        self.momie = pygame.transform.scale_by(self.momie,2.5)
        #polices
        self.Lucida_Console = FontManager(fontName="Copperplate Gothic", size=int((self.largeur/34)))
        self.button_console = FontManager(fontName="Tahoma", size=15)
        self.button_console.setEffects(1)

        #surface
        self.cadre1 = pygame.Rect(int((self.largeur/4)),int(self.hauteur/5-50),int(largeur/2),int(largeur/12-50))
        self.cadre2 = pygame.Rect(int((self.largeur/4)+5),int(self.hauteur/5-45),int(largeur/2-10),int(largeur/12-60))
        self.cadre3 = pygame.Rect(int((self.largeur/4)),int(self.hauteur/5-50),int(largeur/2),int(largeur/12-50))


        #boutton
        self.NewLaby = Button(game,"Nouveau Laby",self.button_console, pygame.Color(20,200,20),pygame.Rect(int((self.largeur/2)-80),int(self.hauteur*(2/3)),160,65),self.nouveau_laby)
        self.quitter = Button(game,"Quitter Le Jeu",self.button_console, pygame.Color(240,0,32),pygame.Rect(int((self.largeur/2)+30),int(self.hauteur*(2/3))+100,160,65),self.quitGame)
        self.menu = Button(game,"Menu",self.button_console, pygame.Color(240,195,0),pygame.Rect(int((self.largeur/2)-190),int(self.hauteur*(2/3))+100,160,65),self.nouveau_menu)
        self.bord_NewLaby = pygame.Rect(int((self.largeur/2)-80),int(self.hauteur*(2/3)),160,65)
        self.bord_quitter = pygame.Rect(int((self.largeur/2)+30),int(self.hauteur*(2/3))+100,160,65)
        self.bord_menu = pygame.Rect(int((self.largeur/2)-190),int(self.hauteur*(2/3))+100,160,65)

    def nouveau_laby(self):
        self.running = False
        self.game.nouveauLaby()

    def nouveau_menu(self):
        self.running = False
        self.game.running = False
        JeuLabyrinthe = Game(Maps.playground, (6,6))
        JeuLabyrinthe.gameLoop()
        del JeuLabyrinthe


    def quitGame(self):
        self.running = False
        self.game.running = False

    def UpdateColor(self):
        if (pygame.time.get_ticks()-self.temps)>500:
            self.color,self.color2 = self.color2,self.color
            self.temps = pygame.time.get_ticks()


    def rendu(self):
        self.window.fill((255,255,255))
        pygame.draw.rect(self.window,self.color2,self.cadre3)
        pygame.draw.rect(self.window,(0,0,0),self.cadre1,1)
        pygame.draw.rect(self.window,self.color,self.cadre2,5)
        self.Lucida_Console.textToSurface(self.window,
                f" CONGRATULATION, YOU WIN ! ",
                int((self.largeur/4)+11),int(((self.hauteur/5-64)+((self.largeur/12-60)/2))),
                pygame.Color(self.color))
        self.NewLaby.draw(self.window)
        self.quitter.draw(self.window)
        self.menu.draw(self.window)
        pygame.draw.rect(self.window,(0,170,0),self.bord_NewLaby,4)
        pygame.draw.rect(self.window,(210,0,2),self.bord_quitter,4)
        pygame.draw.rect(self.window,(210,165,0),self.bord_menu,4)
        self.window.blit(self.kavale,(int(self.largeur/2-185),int(self.hauteur/2-200)))
        self.window.blit(self.momie,(75,self.hauteur-200))
        self.UpdateColor()


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.rendu()
            pygame.display.update()
        pygame.quit()



