from Global import *
from Entity import Entity

class Caisse(Entity):
    def __init__(self, game, name, hp, pos):
        super().__init__(game, name, hp, pos, "game-files/img/caisse_osekour.png")

    def kill(self):
        super().kill()

    def update(self):
        if self.health == 0:
            self.kill()


class Objet_au_sol(Entity):
    def __init__(self, game, name, pos, listObjet):
        super().__init___(game, name, 10000, pos, "game-files/...")    #hp = 10000 car cette entite ne peut pas etre tuee
        self.listObjet = listObjet

    def get(self):
        for elt in self.listObjet:
            objet = self.listObjet.pop()
            self.game.joueur.ajouterInventaire(objet)

    def update(self):
        pass