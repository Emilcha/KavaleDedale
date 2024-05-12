from Global import *

class Settings:
    def __init__(self):
        self.settings = {}
        self.defaults()     # Application des parametres

    def __getitem__(self, key):
        if self.settings[key]:
            val = self.settings[key]
            return val

    def __setitem__(self, key, val):
        self.settings[key] = val

    def defaults(self):
        #Default settings

        #Images par seconde maximale, a diminuer si le jeu change de vitesse
        self.settings["maxfps"]         = 60

        # Vitesse de déplacement et de rotation de la camera
        self.settings["move_speed"]             = 0.04
        self.settings["move_speed_sprinting"]   = 0.09
        self.settings["rotate_speed"]           = 0.035

        # Parametrage des touches
        #Avancer
        self.settings["key_forward"]    = pygame.K_z
        #Reculer
        self.settings["key_backward"]   = pygame.K_s
        #Regarder a droite
        self.settings["key_right"]      = pygame.K_d
        #Regarder a gauche
        self.settings["key_left"]       = pygame.K_q
        #Courir
        self.settings["key_sprint"]     = pygame.K_LSHIFT
        #Attaquer
        self.settings["key_attack"]     = pygame.K_SPACE

        #Touche pour les armes
        self.settings["key_poing"]      = pygame.K_1
        self.settings["key_epee"]       = pygame.K_2
        self.settings["key_zeus"]       = pygame.K_3
        self.settings["key_poseidon"]   = pygame.K_4

        #Touche pour les potions: PAS UTILISé
        self.settings["key_pot_vie"]    = pygame.K_5
        self.settings["key_pot_stam"]   = pygame.K_6
        self.settings["key_pot_degat"]  = pygame.K_7