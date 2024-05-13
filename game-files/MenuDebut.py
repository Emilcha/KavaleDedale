# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *


class MenuDebut :
    def __init__(self):
        """Initialisation des variables utiles"""
        self.pos1y = -550     
        self.pos2y = -1100     
        self.pos3y = -1650      
        self.pos4y = 1300      
        self.posx = 400       
        self.pos4x = 350     
        self.pos = True        
        self.temps = True       
        self.pop = False       
        self.TpsZero = 0        
        self.time = 0
        self.continuer = False
        self.running = True
        self.runMenu = False
        self.runDocu = False
        self.res = (1280,800)

        self.color_dark = (100,100,100)
        self.color_light = (170,170,170)

        self.window = pygame.display.set_mode(self.res)


        self.widthPlay = 1150
        self.heightPlay = 600

        self.widthDocu = 1150
        self.heightDocu = 950

        self.widthQuit = 1150
        self.heightQuit = 1300

        self.widthRetour = 1150
        self.heightRetour = 1200

        self.widthNext = 1700
        self.heightNext = 550

        self.widthPrec = 550
        self.heightPrec = 1100

        self.nextText = False

        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.textQuit = self.smallfont.render('Quit' , True , (0,0,0)) 
        self.textPlay = self.smallfont.render('Play' , True , (0,0,0)) 

        # # # # # # Page documentation # # # # # #
        self.textDocu = self.smallfont.render('Documentation' , True , (0,0,0))
        self.textNext = self.smallfont.render('Suivant' , True , (0,0,0))
        self.textPrec = self.smallfont.render('Precedent' , True , (0,0,0))
        self.textRetour = self.smallfont.render('Retour' , True , (0,0,0))

        self.docufont = pygame.font.SysFont('Corbel', 25)
        self.lore1 = self.docufont.render('Afin de savoir si vous serez digne d\'accéder au royaume', True , (0,0,0))
        self.lore2 = self.docufont.render('de l\'Olympe, les dieux de la Grèce antique vous ont', True, (0,0,0))
        self.lore3 = self.docufont.render('lancé un defi. Serez vous capable de vous échapper du', True, (0,0,0))
        self.lore4 = self.docufont.render('labyrinthe construit par le fameux architecte et génie', True, (0,0,0))
        self.lore5 = self.docufont.render('Dédale? Vous ferez face a de nombreux énemis mais', True, (0,0,0))
        self.lore6 = self.docufont.render('n\'ayez crainte! Pour vous enfuir du labyrinthe vous', True, (0,0,0))
        self.lore7 = self.docufont.render('devrez trouver les armes de trois des dieux de l\'Olympe:', True, (0,0,0))
        self.lore8 = self.docufont.render('La foudre de Zeus, dieu des dieux', True, (0,0,0))
        self.lore9 = self.docufont.render('Le trident de Poséidon, dieu des mers et oceans', True, (0,0,0))
        self.lore10 = self.docufont.render('Le glaive d\'Athéna, déesse de la guerre et de la strategie', True, (0,0,0))
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


        self.image1 = pygame.image.load("game-files/img/icon/Logo.png").convert_alpha()
        self.image2 = pygame.image.load("game-files/img/icon/Logo.png").convert_alpha()
        self.image3 = pygame.image.load("game-files/img/icon/Logo.png").convert_alpha()
        self.image4 = pygame.image.load("game-files/img/icon/PAK.png").convert_alpha()
        self.image5 = pygame.image.load("game-files/img/icon/Tag.png").convert_alpha()
        self.image6 = pygame.image.load("game-files/img/icon/fondMenu.png").convert_alpha()
        self.image7 = pygame.image.load("game-files/img/icon/Tag2.png").convert_alpha()

        self.image1 = pygame.transform.scale(self.image1,(850,400))
        self.image2 = pygame.transform.scale(self.image2,(850,400))
        self.image3 = pygame.transform.scale(self.image3,(850,400))
        self.image4 = pygame.transform.scale(self.image4,(650,400))
        self.image5 = pygame.transform.scale(self.image5,(400,200))
        self.image7 = pygame.transform.scale(self.image7,(400,200))

        # # # # # # Page documentation # # # # # #
        self.image8 = pygame.image.load("game-files/img/icon/keyZ.png")
        self.expl1 = self.docufont.render('Move forward', True, (0,0,0))
        self.image9 = pygame.image.load("game-files/img/icon/keyS.png")
        self.expl2 = self.docufont.render('Move backwards', True, (0,0,0))
        self.image10 = pygame.image.load("game-files/img/icon/keyQ.png")
        self.expl3 = self.docufont.render('Look left', True, (0,0,0))
        self.image11 = pygame.image.load("game-files/img/icon/keyD.png")
        self.expl4 = self.docufont.render('Look right', True, (0,0,0))
        self.image12 = pygame.image.load("game-files/img/icon/key_space.png")
        self.expl5 = self.docufont.render('Attack', True, (0,0,0))
        self.image13 = pygame.image.load("game-files/img/icon/key_shift.png")
        self.expl6 = self.docufont.render('Sprint', True, (0,0,0))
        self.expl7 = self.docufont.render('Use number keys to switch objects', True, (0,0,0))
        
        self.message1 = self.docufont.render('Dans cette quete, vous devrez faire face a l\'adversité.', True, (0,0,0))
        self.message2 = self.docufont.render('Gardez votre force et votre courage et vous vaincrez.', True, (0,0,0))
        # # # # # # # # # # # # # # # # # # # # # 



    """Création d'un chronomètre"""
    def chrono(self):
        seconds = (pygame.time.get_ticks() - self.TpsZero) / 1000
        return seconds


    """Fonction principale"""
    def lancement(self):
        
        """Boucle principale"""
        while self.running:
            """Phase 1, animation lors du lancement du programme"""
            if self.runMenu == False:        
                """Permet de faire clignoter le 'Press Any Key' lors de la fin de l'animation"""
                if self.pop == True:
                    """Utilisation du chronomètre pour faire clignoter le 'Press Any Key' tout les x secondes """
                    self.time = self.chrono()
                    if self.temps == True:
                        """On change de position le 'Press Any Key' pour donner l'illusion du clignotement"""
                        self.pos4x = 350
                        """On passe la variable en TRUE pour signifier que l'animation est finie et 
                        qu'il donc possible d'appuyer sur une touche pour passer à la suite"""
                        self.continuer = True

                    """Puis tout les x temps on remet le 'Press Any Key' à sa place"""
                    if self.time > 0.7:
                        self.pos4x = 1280
                        self.TpsZero = pygame.time.get_ticks()
                        if self.temps == True:
                            self.temps = False
                        else:
                            self.temps = True

                """Permet le mouvement du logo lors de la première animation"""
                if self.pos == True:
                    color = 255
                    self.pos1y+=0.5
                    self.pos2y+=0.5
                    self.pos3y+=0.5
                    self.window.fill(pygame.Color(color,color,color))

                """Permet le changement de couleur progressive du fond lorsque la première animation est finie, blanc fondu en noir"""
                if color > 0 and self.pos == False:
                    color -= 1

                """Permet l'arrêt de la première animation"""
                if self.pos1y == 1350 and self.pos == True:
                    self.pos = False
                    """On arrête le programme pour que éviter le fondu en noir se fasse instantanément"""
                    pygame.time.delay(2000)

                """On lance le programme permettant l'apparition et le clignotemment du 'Press Any Key' """
                if self.pos == False:
                    self.window.fill(pygame.Color(color,color,color))
                    if color == 0 and self.pop == False:
                        pygame.time.delay(1000)
                        self.pos4y = 400
                        self.TpsZero = pygame.time.get_ticks()
                        self.pop = True


                """On affiche les différentes images"""
                self.window.blit(self.image1,(self.posx,self.pos1y))
                self.window.blit(self.image2,(self.posx,self.pos2y))
                self.window.blit(self.image3,(self.posx,self.pos3y))
                self.window.blit(self.image4,(self.pos4x,self.pos4y))
                self.window.blit(self.image5,(0,0))

                """On récupère les action faites par le joueur"""
                for event in pygame.event.get():
                    """Si il clique sur la croix en haut à droit pour fermer la page"""
                    if event.type == QUIT:
                        pygame.quit()
                    """Si il appuie sur n'importe quel touche lors du 'Press Any Key' """
                    if event.type == pygame.KEYDOWN and self.continuer == True:
                        """Lance la Phase 2 et arrêt de la Phase 1"""
                        self.runMenu = True

            """Phase 2, le Menu lors du lancement"""
            if self.runMenu == True and self.runDocu == False:
                """Affichage du fond"""
                self.window.blit(self.image6,(0,0))
                """On récupère les action faites par le joueur"""
                for ev in pygame.event.get(): 
                    """Si la souris est cliqué"""
                    if ev.type == pygame.MOUSEBUTTONDOWN: 

                        #if the mouse is clicked on the 
                        # button the game is terminated 
                        """Si la souris est à l'emplacement du bout 'Quit' """
                        if self.widthQuit/2 <= mouse[0] <= self.widthQuit/2+140 and self.heightQuit/2 <= mouse[1] <= self.heightQuit/2+40: 
                            pygame.quit()

                        """Si la souris est à l'emplacement du bout 'Play' """
                        if self.widthPlay/2 <= mouse[0] <= self.widthPlay/2+140 and self.heightPlay/2 <= mouse[1] <= self.heightPlay/2+40: 
                            """Fin de la boucle du Menu, le jeu se lance alors """
                            self.running = False
                        """Si la souris est à l'emplacement du bout 'Documentation' """
                        if self.widthDocu/2-50 <= mouse[0] <= self.widthDocu/2+240 and self.heightDocu/2 <= mouse[1] <= self.heightDocu/2+40: 
                            self.runDocu = True

                    """Si il clique sur la croix en haut à droit pour fermer la page"""   
                    if ev.type == QUIT:
                        pygame.quit()

                """On récupère la position de la souris à chaque itération de boucle"""
                mouse = pygame.mouse.get_pos() 

                """Permet de faire changer de couleur le bouton 'Quit' lorsque la souris est dessus"""
                if self.widthQuit/2 <= mouse[0] <= self.widthQuit/2+140 and self.heightQuit/2 <= mouse[1] <= self.heightQuit/2+40: 
                    pygame.draw.rect(self.window,self.color_light,[self.widthQuit/2,self.heightQuit/2,140,40]) 
                else: 
                    """Permet de remettre la couleur du bouton 'Quit' lorsque la souris n'est plus dessus"""
                    pygame.draw.rect(self.window,self.color_dark,[self.widthQuit/2,self.heightQuit/2,140,40]) 

                """Permet de faire changer de couleur le bouton 'Play' lorsque la souris est dessus"""
                if self.widthPlay/2 <= mouse[0] <= self.widthPlay/2+140 and self.heightPlay/2 <= mouse[1] <= self.heightPlay/2+40: 
                    pygame.draw.rect(self.window,self.color_light,[self.widthPlay/2,self.heightPlay/2,140,40]) 
                else:
                    """Permet de remettre la couleur du bouton 'Play' lorsque la souris n'est plus dessus"""
                    pygame.draw.rect(self.window,self.color_dark,[self.widthPlay/2,self.heightPlay/2,140,40]) 
 
                """Permet de faire changer de couleur le bouton 'Documentation' lorsque la souris est dessus"""
                if self.widthDocu/2-50 <= mouse[0] <= self.widthDocu/2+190 and self.heightDocu/2 <= mouse[1] <= self.heightDocu/2+40: 
                    pygame.draw.rect(self.window,self.color_light,[self.widthDocu/2 - 50,self.heightDocu/2,240,40]) 
                else: 
                    """Permet de remettre la couleur du bouton 'Documentation' lorsque la souris n'est plus dessus"""
                    pygame.draw.rect(self.window,self.color_dark,[self.widthDocu/2 - 50,self.heightDocu/2,240,40]) 

                """On affiche les différents boutons"""
                self.window.blit(self.textQuit , (self.widthQuit/2 +40,self.heightQuit/2 + 3)) 
                self.window.blit(self.textPlay , (self.widthPlay/2 +40,self.heightPlay/2 + 3))
                self.window.blit(self.textDocu , (self.widthDocu/2 - 38 ,self.heightDocu/2 + 3))

                self.window.blit(self.image7,(900,0))

            """Affichage de la documentation du jeu"""
            if self.runDocu == True:
                """Affichage du fond"""
                self.window.blit(self.image6,(0,0))

                """On récupère les action faites par le joueur"""
                for ev in pygame.event.get(): 
                    """Si la souris est cliqué"""
                    if ev.type == pygame.MOUSEBUTTONDOWN: 

                        #if the mouse is clicked on the 
                        # button the game is terminated 
                        """Si la souris est à l'emplacement du bout 'Quit' """
                        if self.widthQuit/2 <= mouse[0] <= self.widthQuit/2+140 and self.heightQuit/2 <= mouse[1] <= self.heightQuit/2+40: 
                            pygame.quit()

                        """Si la souris est à l'emplacement du bout 'Retour' """
                        if self.widthRetour/2 <= mouse[0] <= self.widthRetour/2+140 and self.heightRetour/2 <= mouse[1] <= self.heightRetour/2+40: 
                            self.runDocu = False
                        """Si la souris est à l'emplacement du bout 'Next' """
                        if self.widthNext/2+100 <= mouse[0] <= self.widthNext/2+240 and self.heightNext/2 <= mouse[1] <= self.heightNext/2+40 and self.nextText == False: 
                            self.nextText = True
                        """Si la souris est à l'emplacement du bout 'Retour' """
                        if self.widthPrec/2-131 <= mouse[0] <= self.widthPrec/2+71 and self.heightPrec/2 <= mouse[1] <= self.heightPrec/2+40 and self.nextText == True:
                            self.nextText = False


                    """Si il clique sur la croix en haut à droite pour fermer la page"""   
                    if ev.type == QUIT:
                        pygame.quit()

                """On récupère la position de la souris à chaque itération de boucle"""
                mouse = pygame.mouse.get_pos()

                """Permet de faire changer de couleur le bouton 'Quit' lorsque la souris est dessus"""
                if self.widthQuit/2 <= mouse[0] <= self.widthQuit/2+140 and self.heightQuit/2 <= mouse[1] <= self.heightQuit/2+40: 
                    pygame.draw.rect(self.window,self.color_light,[self.widthQuit/2,self.heightQuit/2,140,40]) 
                else: 
                    """Permet de remettre la couleur du bouton 'Quit' lorsque la souris n'est plus dessus"""
                    pygame.draw.rect(self.window,self.color_dark,[self.widthQuit/2,self.heightQuit/2,140,40]) 

                """Permet de faire changer de couleur le bouton 'Retour' lorsque la souris est dessus"""
                if self.widthRetour/2 <= mouse[0] <= self.widthRetour/2+140 and self.heightRetour/2 <= mouse[1] <= self.heightRetour/2+40: 
                    pygame.draw.rect(self.window,self.color_light,[self.widthRetour/2,self.heightRetour/2,140,40]) 
                else:
                    """Permet de remettre la couleur du bouton 'Retour' lorsque la souris n'est plus dessus"""
                    pygame.draw.rect(self.window,self.color_dark,[self.widthRetour/2,self.heightRetour/2,140,40]) 


                """On affiche les differents boutons"""
                self.window.blit(self.textRetour , (self.widthRetour/2 + 20,self.heightRetour/2 + 3))
                self.window.blit(self.textQuit , (self.widthQuit/2 + 40,self.heightQuit/2 + 3))

                """Affichage en fonction de la page"""
                if self.nextText:
                    """Permet de faire changer de couleur le bouton 'Precedent' lorsque la souris est dessus"""
                    if self.widthPrec/2 - 131<= mouse[0] <= self.widthPrec/2+91 and self.heightPrec/2 <= mouse[1] <= self.heightPrec/2+40: 
                        """Permet de remettre la couleur du bouton 'Precedent' lorsque la souris n'est plus dessus"""
                        pygame.draw.rect(self.window,self.color_light,[self.widthPrec/2 -131,self.heightPrec/2,200,40]) 
                    else: 
                        pygame.draw.rect(self.window,self.color_dark,[self.widthPrec/2 -131,self.heightPrec/2,200,40])

                    """Affichage des touches"""
                    self.window.blit(self.image8, (370, 280))
                    self.window.blit(self.image9, (640, 280))
                    self.window.blit(self.image10, (370, 350))
                    self.window.blit(self.image11, (640, 350))
                    self.window.blit(self.image12, (370, 420))
                    self.window.blit(self.image13, (640, 420))

                    """Explication des touches"""
                    self.window.blit(self.expl1, (480, 300))
                    self.window.blit(self.expl2, (740, 300))
                    self.window.blit(self.expl3, (480, 370))
                    self.window.blit(self.expl4, (740, 370))
                    self.window.blit(self.expl5, (500, 440))
                    self.window.blit(self.expl6, (740, 440))
                    self.window.blit(self.expl7, (490, 490))


                    """Message au joueur"""
                    self.window.blit(self.message1, (370, 530))
                    self.window.blit(self.message2, (370, 550))

                    """Bouton Precedent"""
                    self.window.blit(self.textPrec , (self.widthPrec/2 - 100,self.heightPrec/2 + 3))

                else:
                    """Permet de faire changer de couleur le bouton 'Suivant' lorsque la souris est dessus"""
                    if self.widthNext/2+100 <= mouse[0] <= self.widthNext/2+240 and self.heightNext/2 <= mouse[1] <= self.heightNext/2+40: 
                        pygame.draw.rect(self.window,self.color_light,[self.widthNext/2 + 100,self.heightNext/2,140,40]) 
                    else: 
                        pygame.draw.rect(self.window,self.color_dark,[self.widthNext/2 + 100,self.heightNext/2,140,40])

                    """Affichage du scenario du jeu"""
                    self.window.blit(self.lore1, (370, 280))
                    self.window.blit(self.lore2, (390, 310))
                    self.window.blit(self.lore3, (377, 340))
                    self.window.blit(self.lore4, (384, 370))
                    self.window.blit(self.lore5, (385, 400))
                    self.window.blit(self.lore6, (376, 430))
                    self.window.blit(self.lore7, (370, 460))
                    self.window.blit(self.lore8, (465, 490))
                    self.window.blit(self.lore9, (405, 520))
                    self.window.blit(self.lore10, (370, 550))

                    """Bouton Suivant"""
                    self.window.blit(self.textNext , (self.widthNext/2 + 120,self.heightNext/2 + 3))



            """On actualise la fenêtre à chaque itération de boucle"""
            pygame.display.update()