import pygame

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


        if pygame.event.type == pygame.MOUSEBUTTONDOWN and (pygame.time.get_ticks()-self.touche)>5000:
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
