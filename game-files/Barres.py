from Global import *

class barre_de_sprint:
    def __init__(self,game,largeur,hauteur):
        self.game = game
        self.hauteur = hauteur
        self.largeur = largeur
        self.zone = pygame.Rect(largeur-15,int((hauteur/7)*2),15,int(hauteur/7)*3)
        self.zone_barre = pygame.Rect(largeur-15,int((hauteur/7)*2),15,int(hauteur/7)*3)
        self.longueur = int(self.game.joueur.stamina * 100)
        self.tps = pygame.time.get_ticks()
        self.wait = pygame.time.get_ticks()

    def longueur_barre(self):
        self.longueur = int(self.game.joueur.stamina * 100)
        a = int(((self.hauteur//7)*2)+(((100-self.longueur)/100)*((self.hauteur/7)*3)))
        self.zone_barre = pygame.Rect(self.largeur-15,a,15,(int(self.hauteur/7)*5-a))

    def rendu(self,window):
        self.longueur_barre()
        pygame.draw.rect(window,(50, 50, 50),self.zone)
        pygame.draw.rect(window,(0, 0, 255),self.zone_barre)


class barre_de_vie:
    def __init__(self,game,largeur,hauteur):
        self.largeur = largeur
        self.hauteur= hauteur
        self.point_vie = game.joueur.vie
        self.game = game
        """
        self.wait = pygame.time.get_ticks()
        self.temoin = pygame.time.get_ticks()
        self.temps_de_touche = pygame.time.get_ticks()
        self.flash = pygame.time.get_ticks()
        """
        self.bord_barre = pygame.Rect(int(self.largeur//4),self.hauteur-25,int(self.largeur//2),20)
        self.zone_barre = pygame.Rect(int((self.largeur//4)+1),self.hauteur-24,int((self.largeur//2)-2),19)
        self.couleur_barre = (0,255,0)

    def update(self):
        self.point_vie = self.game.joueur.vie

        if self.point_vie<=50:
            self.couleur_barre = (255,int((self.point_vie/50)*255),0)
        else:
            self.couleur_barre = (int((1-(self.point_vie-50)/50)*255),255,0)

        self.zone_barre = pygame.Rect(int((self.largeur//4)+1),self.hauteur-24,int((self.point_vie/100)*(self.largeur//2)-2),19)


    def rendu(self,window):
        self.update()
        """         => Connsome trop de resources (pygame.time)
        if (pygame.time.get_ticks()-self.temps_de_touche)<1200:
            if (pygame.time.get_ticks()-self.flash)<150:
                self.couleur = (205,0,0)
            if (pygame.time.get_ticks()-self.flash)>300:
                self.flash = pygame.time.get_ticks()"""
        pygame.draw.rect(window,(0, 0, 0),self.bord_barre,1)
        pygame.draw.rect(window,self.couleur_barre,self.zone_barre)

