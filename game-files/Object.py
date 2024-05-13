from Global import *
from Entity import Entity
from Enemies import FantomeBizare
from Successful_Game import *

class Sortie(Entity):
    def __init__(self, game, pos):
        super().__init__(game, "SORTIE", 10000, pos, "game-files/img/ents/exit_closed.png")
        self.z = 0
        self.p = 0
        self.s = 0
        self.texture_closed     = pygame.image.load("game-files/img/ents/exit_closed.png")
        self.texture_oppened    = pygame.image.load("game-files/img/ents/exit_open.png")
        self.zeus_texture       = pygame.image.load("game-files/img/ents/exit_part_zeus.png")
        self.trident_texture    = pygame.image.load("game-files/img/ents/exit_part_trident.png")
        self.epee_texture       = pygame.image.load("game-files/img/ents/exit_part_epee.png")

    def get_texture(self):
        self.texture_copy = self.texture_closed.copy()
        self.z = 0
        self.p = 0
        self.s = 0
        if self.game.joueur.inv.a_object("Zeus"):
            self.z=1
            self.texture_copy.blit(self.zeus_texture,(0,0))
        if self.game.joueur.inv.a_object("Poseidon"):
            self.p=1
            self.texture_copy.blit(self.trident_texture,(0,0))
        if self.game.joueur.inv.a_object("Spartan"):
            self.s=1
            self.texture_copy.blit(self.epee_texture,(0,0))

        if self.z + self.p + self.s == 3:
            self.texture_copy = self.texture_oppened

        return self.texture_copy

    def update(self):
        if self.z + self.p + self.s == 3:
            vec_y = self.y - self.game.joueur.y
            vec_x = self.x - self.game.joueur.x
            vec_len = math.sqrt(vec_x**2 + vec_y**2)
            if vec_len < 0.5:
                a = VICTORY(HEIGHT,WIDTH,self.game)
                a.loop()

class Caisse(Entity):
    def __init__(self, game, name, hp, pos):
        super().__init__(game, name, hp, pos, "game-files/img/ents/caisse.png")
        
        self.content = []
        
        nb_object = random.randint(0,2)
        for i in range(nb_object):
            self.content.append(random.choice(listObject))

    def kill(self):
        num_potion = 1
        """
        Si la caisse était vide, on donne une petite chance qu'un fantome apparaisse
        Sinon on fait apparaître son contenu
        """
        if self.content == []:
            fantomeSpawn = random.randint(0,1)
            if fantomeSpawn == 1:
                position_fantome = (self.x + random.uniform(-10, 10), self.y + random.uniform(-10, 10))
                self.game.ents.add_entity(FantomeBizare(self.game, self.name + '_fantome', position_fantome))
                print('Un fantome vous suit')
        else:
            for elt in self.content:
                newPos = (self.x + random.uniform(-0.5, 0.5), self.y + random.uniform(-0.5, 0.5))
                self.game.ents.add_entity(Objet_au_sol(self.game, self.name + "_" + f"elt{str(num_potion)}", newPos, elt))
                num_potion += 1

        self.game.ents.del_entity(self.name)

    def update(self):
        if self.health <= 0:
            self.kill()


class Objet_au_sol(Entity):
    def __init__(self, game, name, pos, type_object):
        """Initialisation d'une entité en fonction du type d'objet"""
        if type_object == 'Heal Potion':
            self.type_obj = 'Heal Potion'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_HealPotion.png")

        if type_object == 'Stamina Potion':
            self.type_obj = 'Stamina Potion'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_StaminaPotion.png")

        if type_object == 'Damage Potion':
            self.type_obj = 'Damage Potion'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_DamagePotion.png")

        if type_object == 'Zeus':
            self.type_obj = 'Zeus'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_Zeus.png")

        if type_object == 'Poseidon':
            self.type_obj = 'Poseidon'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_Trident.png")

        if type_object == 'Spartan':
            self.type_obj = 'Spartan'
            super().__init__(game, name, 10000, pos, "game-files/img/ents/Obj_Epee.png")

    def use_object(self):
        """Les potions ont un effet sur le joueur"""
        if self.type_obj == 'Heal Potion':
            if self.game.joueur.vie + 20 < 100:
                self.game.joueur.vie += 20
            elif self.game.joueur.vie < 100:
                self.game.joueur.vie = 100

        if self.type_obj == 'Stamina Potion':
            if self.game.joueur.stamina + 0.5 < 1:
                self.game.joueur.stamina += 0.5
            elif self.game.joueur.stamina < 1:
                self.game.joueur.stamina = 1

        if self.type_obj == 'Damage Potion':     #TODO Damage Potion est une potion de vitesse
            self.game.joueur.potionEffect += 1

        """Les armes sont ajoutées à l'inventaire"""
        if self.type_obj == 'Zeus':
            self.game.joueur.inv.ajouter(self.type_obj)

        if self.type_obj == 'Poseidon':
            self.game.joueur.inv.ajouter(self.type_obj)

        if self.type_obj == 'Spartan':
            self.game.joueur.inv.ajouter(self.type_obj)


    def update(self):
        """On vérifie la distance au joueur, s'il est suffisamment proche il ramasse l'objet"""
        vec_y = self.y - self.game.joueur.y
        vec_x = self.x - self.game.joueur.x
        vec_len = math.sqrt(vec_x**2 + vec_y**2)
        if vec_len < 0.5:
            self.use_object()
            self.kill()
