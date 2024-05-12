from Object import Caisse
from random import randint, choice
import math
import copy

class Pile:
    """Classe Pile"""

    def __init__(self):
        """Initialisation d'une pile vide de type liste Python"""
        self.contenu=[]

    def est_vide(self):
        """Test si la pile est vide (retourne True) ou non (retourne False)"""
        return self.contenu==[]

    def empiler(self,x):
        """Empile un élément x au sommet de la pile"""
        self.contenu.append(x)

    def depiler(self):
        """Depile le sommet de la pile et le retourne"""
        if not self.est_vide():
            return self.contenu.pop()
        else:
            print("Pile vide !")
        """Autre méthode"""
        """assert not self.est_vide(),\"Pile vide !\""""
        """return self.contenu.pop()"""

    def taille(self):
        return len(self.contenu)

    def sommet(self):
        if not self.est_vide():
            return self.contenu[-1]
        else:
            print("Pile vide !")

#NON UTILISé (Pour l'instrant)
class Arbre:
    solution = None
    profondeur = 0

    def __init__(self, val, sa=[]):
        self.valeur = val
        self.sa = sa

    def ajout_sa(self,arbre):
        self.sa.append(arbre)

    def chemin_plus_profond(self):
        Arbre.solution = None
        Arbre.profondeur = 0
        Arbre.__chemin_profond(self,0)
        return (Arbre.solution, Arbre.profondeur)

    def __chemin_profond(self, profondeur_courante):
        if len(self.sa) == 0:
            if profondeur_courante >= Arbre.profondeur:
                Arbre.profondeur = profondeur_courante
                Arbre.solution = self.valeur
        else:
            for ab in self.sa:
                Arbre.__chemin_profond(ab, profondeur_courante + 1)

class Labyrinthe:
    def __init__(self,longueur,hauteur):

        self.longueur = longueur
        self.hauteur = hauteur
        self.nbSalle = longueur + hauteur
        self.nbMonstre = int(longueur / hauteur)
        
        self.CaseDepart = None
        self.CaseFinale = None
        
        self.laby = []
        for i in range(hauteur):
            self.laby.append([2 for i in range(self.longueur)])
       
        self.map = []
        for i in range(hauteur):
            self.map.append([2 for i in range(self.longueur)])
        
       
        self.Minimap = []
        for i in range(self.hauteur):
            self.Minimap.append([0 for i in range(self.longueur)])
            
       
        
        self.mapFinale= []


        #Différents types de matrices
        
        """ 0 = Sol, 1 = Mur , 2 = Trou , 3 = Potentiel Coffre , 4 = Statue pour Sauvegarder
        """        
        self.Salle1=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,0,3,2,0,0,0,0,0,1],
                       [1,0,0,2,2,0,0,0,0,1],
                       [1,0,0,2,2,1,1,0,0,1],
                       [1,0,0,2,2,1,3,0,0,1],
                       [1,0,0,2,2,1,1,0,0,1],
                       [1,0,0,2,2,0,0,0,0,1],
                       [1,0,0,0,0,0,0,3,2,1],
                       [1,0,0,0,0,0,2,2,2,1],
                       [1,1,1,1,1,1,1,1,1,1]]
      
        self.Salle2=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,0,3,1,0,0,0,0,0,1],
                       [1,0,0,1,0,0,0,0,0,1],
                       [1,0,0,1,1,1,1,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,1,0,0,0,0,0,1],
                       [1,0,0,1,0,0,1,1,1,1],
                       [1,0,0,1,0,0,0,0,3,1],
                       [1,3,1,1,0,0,0,0,3,1],
                       [1,1,1,1,1,1,1,1,1,1]]
       
        self.Salle3=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,3,0,0,0,0,0,0,3,1],
                       [1,0,1,3,0,0,0,1,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,2,2,0,0,0,1],
                       [1,0,0,0,2,2,0,0,0,1],
                       [1,0,0,0,0,0,0,3,0,1],
                       [1,0,1,0,0,0,0,1,0,1],
                       [1,3,0,0,0,0,0,0,3,1],
                       [1,1,1,1,1,1,1,1,1,1]]
        
        self.Salle4=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,1,1,1,0,0,1,1,1,1],
                       [1,1,1,3,0,0,3,1,1,1],
                       [1,1,0,0,0,0,0,0,1,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,1,0,0,0,0,0,0,1,1],
                       [1,1,1,3,0,0,3,1,1,1],
                       [1,1,1,1,0,0,1,1,1,1],
                       [1,1,1,1,1,1,1,1,1,1]]
        
        self.Salle5=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,2,2,0,0,0,0,0,0,1],
                       [1,2,2,0,0,3,3,0,0,1],
                       [1,0,0,0,0,1,1,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,1,1,0,0,0,0,1],
                       [1,0,0,3,3,0,0,2,2,1],
                       [1,0,0,0,0,0,0,2,2,1],
                       [1,1,1,1,1,1,1,1,1,1]]
        
        self.Salle6=  [[1,1,1,1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,3,1,0,0,0,1],
                       [1,0,0,1,1,1,1,0,0,1],
                       [1,0,0,3,1,1,3,0,0,1],
                       [1,0,0,0,3,1,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1,1,1,1]]
       
        self.Sauvegarde1=  [[1,1,1,1,1,1,1,1,1,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,1,1,0,0,1,1,0,1],
                            [1,0,1,0,0,0,4,1,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,1,0,0,0,0,1,0,1],
                            [1,0,1,1,0,0,1,1,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,1,1,1,1,1,1,1,1,1]]
       
        self.Sauvegarde2=  [[1,1,1,1,1,1,1,1,1,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,1,1,0,0,1,1,0,1],
                            [1,0,1,0,0,0,0,1,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,0,1,4,0,0,0,1,0,1],
                            [1,0,1,1,0,0,1,1,0,1],
                            [1,0,0,0,0,0,0,0,0,1],
                            [1,1,1,1,1,1,1,1,1,1]]
       
        self.Couloir1=  [[1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,0,0,0,0,0,0,0,0,1],
                         [1,0,0,0,0,0,0,0,0,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1]]
       
        
        self.Couloir2=  [[1,1,1,1,1,1,1,1,1,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,0,0,0,0,0,0,0,0,1],
                         [1,0,0,0,0,0,0,0,0,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,2,2,2,0,0,2,2,2,1],
                         [1,1,1,1,1,1,1,1,1,1]]

        self.Spawn= [[1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,2,0,0,0,0,2,0,1],
                     [1,0,0,2,0,0,2,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,2,0,0,2,0,0,1],
                     [1,0,2,0,0,0,0,2,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1]]

        self.listeCouloir = [self.Couloir1,self.Couloir2]
        self.listeSalle = [self.Salle1,self.Salle2,self.Salle3,self.Salle4,self.Salle5,self.Salle6,self.Sauvegarde1,self.Sauvegarde2]
        
    
    def ecrireFichier(self):
        f = open("ListeLaby.txt","w")
        f.write(str(self.mapFinale))
        f.close()

    def afficheLaby(self):
        return self.laby
    
    def afficheMap(self):
        return self.map
    
    def afficheMapFinale(self):
        return self.mapFinale
    
    def afficheMinimap(self):
        return self.Minimap

    def getCaseDepart(self):
        return self.CaseDepart


    def getCaseFin(self):
        # TEMPORAIRE:
        self.CaseFinale = (randint(0,self.hauteur - 1),randint(0,self.longueur - 1))
        while math.sqrt((self.CaseFinale[0]-self.CaseDepart[0])**2+(self.CaseFinale[1]-self.CaseDepart[1])**2) < 3:
            self.CaseFinale = (randint(0,self.hauteur - 1),randint(0,self.longueur - 1))
        return self.CaseFinale
"""
        minmap_arbre = [[None for j in range(self.longueur)] for i in range(self.hauteur)]
        for i in range(self.hauteur):
            for j in range(self.longueur):
                listeDir = []
                if self.map[i][j][0][4] != 1:
                    listeDir.append('N')
                if self.map[i][j][9][4] != 1:
                    listeDir.append('S')
                if self.map[i][j][4][0] != 1:
                    listeDir.append('W')
                if self.map[i][j][4][9] != 1:    
                    listeDir.append('E')

                minmap_arbre[i][j] = listeDir
        
        pile = Pile()
        arbre = Arbre(0)
        pile.empiler(self.CaseDepart)
        while(not pile.est_vide()):
            val = pile.depiler()
            arbre.valeur = val
            h = val[0]
            l = val[1]

            #TODO: Finir generation arbre
"""
            

    def __directions_possibles(self,i,j):
        directions = []
        if i < self.hauteur -1 :
            if not self.laby[i+1][j] == 'Vue' :
                directions.append('S')
        if i >0 :
            if not self.laby[i-1][j] == 'Vue':
                directions.append('N')
        if j < self.longueur -1:
            if not self.laby[i][j+1] == 'Vue':
                directions.append('E')
        if j > 0 :
            if not self.laby[i][j-1] == 'Vue':    
                directions.append('W')
        return directions            



    def __abattre_mur(self,i,j,dire,pile):
        for elem in dire:
            if elem == 'S' and not self.laby[i+1][j] == 'Vue':
                self.map[i][j][9][4] = 0
                self.map[i][j][9][5] = 0
                self.map[i+1][j][0][4] = 0
                self.map[i+1][j][0][5] = 0
                self.laby[i+1][j] = 'Vue'
                pile.empiler((i+1, j))
            if elem == 'N' and not self.laby[i-1][j] == 'Vue': 
                self.map[i][j][0][4] = 0
                self.map[i][j][0][5] = 0
                self.map[i-1][j][9][4] = 0
                self.map[i-1][j][9][5] = 0
                self.laby[i-1][j] = 'Vue'
                pile.empiler((i-1,j))
            if elem == 'W' and not self.laby[i][j-1] == 'Vue':
                self.map[i][j][4][0] = 0
                self.map[i][j][5][0] = 0
                self.map[i][j-1][4][9] = 0
                self.map[i][j-1][5][9] = 0
                self.laby[i][j-1] = 'Vue'
                pile.empiler((i, j-1))
            if elem == 'E' and not self.laby[i][j+1] == 'Vue':
                self.map[i][j][4][9] = 0
                self.map[i][j][5][9] = 0
                self.map[i][j+1][4][0] = 0
                self.map[i][j+1][5][0] = 0
                self.laby[i][j+1] = 'Vue'
                pile.empiler((i, j+1))




    def genereLaby(self):
        pile = Pile()
        
        typeCase = [1] * self.nbSalle
        CaseDepart = (randint(0,self.hauteur - 1),randint(0,self.longueur - 1))
        self.CaseDepart = CaseDepart
        pile.empiler(CaseDepart)

#Generation des emplacements des salles et des couloirs     
        while typeCase != []:
            for i in range(self.hauteur):
                for j in range(self.longueur):
                    if self.laby[i][j] == 2:    
                        a = randint(1,2)
                        if a == 1:
                            try: 
                                typeCase.pop()
                                self.laby[i][j] = 3
                                self.map[i][j] = 3
                            except:
                                break
#Generation des types de salle et de couloir
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if (i,j) == CaseDepart:
                        self.map[i][j] = copy.deepcopy(self.Spawn)
                        continue
                if self.map[i][j] == 2:
                    a = choice(self.listeCouloir)
                    self.map[i][j] = copy.deepcopy(a)
                if self.map[i][j] == 3:
                    a = choice(self.listeSalle)
                    self.map[i][j] = copy.deepcopy(a)
                    if self.map[i][j] == self.Sauvegarde1 or self.map[i][j] == self.Sauvegarde2:
                        self.listeSalle.remove(self.Sauvegarde1)
                        self.listeSalle.remove(self.Sauvegarde2)                
 
        
#Debut generation minimap 
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.map[i][j] == self.listeCouloir[0]:
                    self.Minimap[i][j] = 'C0'
                if self.map[i][j] == self.listeCouloir[1]:
                    self.Minimap[i][j] = 'C1'
                if self.map[i][j] == self.listeSalle[0]:
                    self.Minimap[i][j] = 'S0'
                if self.map[i][j] == self.listeSalle[1]:
                    self.Minimap[i][j] = 'S1'
                if self.map[i][j] == self.listeSalle[2]:
                    self.Minimap[i][j] = 'S2'
                if self.map[i][j] == self.listeSalle[3]:
                    self.Minimap[i][j] = 'S3'
                if self.map[i][j] == self.listeSalle[4]:
                    self.Minimap[i][j] = 'S4'
                if self.map[i][j] == self.listeSalle[5]:
                    self.Minimap[i][j] = 'S5'
                if self.map[i][j] == self.Sauvegarde1:
                    self.Minimap[i][j] = 'SAV0'
                if self.map[i][j] == self.Sauvegarde2:                
                    self.Minimap[i][j] = 'SAV1'
                if self.map[i][j] == self.Spawn:
                    self.Minimap[i][j] = 'SPWN'


#Generation des ouvertures , des passages du labyrinthe        
        self.laby[CaseDepart[0]][CaseDepart[1]] = 'Vue'
        while not pile.est_vide():
            c = pile.depiler()
            #print(c)
            liste = self.__directions_possibles(c[0],c[1])
            if len(liste) > 1:
                pile.empiler(c)
            if len(liste) > 0:
                direction = choice(liste)
                if len(direction) > 2 :
                    direction.pop(randint(0,len(direction)))
                    #print(direction)
                self.__abattre_mur(c[0],c[1],direction,pile)
        
        
        
        for i in range(self.hauteur):  
            for k in range(10):
                self.map[0][i][0][k] = 1
                self.map[4][i][9][k] = 1
                self.map[i][0][k][0] = 1
                self.map[i][4][k][9] = 1
                
#Generation aléatoire des coffres                                
        for i in range (self.hauteur):
            for j in range(self.longueur):
                for k in range(10):
                    for l in range(10):
                        if self.map[i][j][k][l] == 3:        
                            a = randint(1,2)
                            if a == 1:
                                self.map[i][j][k][l] = 0

        
#Compilation de toutes les listes        
        for j in range(self.longueur):
            for k in range(10):
                ligne = []
                for l in range(self.hauteur):
                    ligne += self.map[j][l][k]
                self.mapFinale.append(ligne)
        
        
class LabyEnts:
    def __init__(self, map_array, game):
        self.game = game
        self.map = map_array

    def gen_ents(self):
        num_caisse = 1
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 3:
                    self.map[i][j] = 0
                    self.game.ents.add_entity(Caisse(self.game, f"Caisse{str(num_caisse)}", 30, (i + 0.5, j + 0.5)))
                    num_caisse += 1
                if self.map[i][j] == 4:
                    self.map[i][j] = 0
                    # Entité statue sauvgarde

    def get_edited_map(self):
        return self.map



"""
if __name__=='__main__':
    laby = Labyrinthe(5,5)
    laby.genereLaby()
    laby.ecrireFichier()
"""
    







