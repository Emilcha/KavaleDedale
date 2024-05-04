from Object import Caisse
from random import randint, choice

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




class Labyrinthe:
    def __init__(self,longueur,hauteur):

        self.longueur = longueur
        self.hauteur = hauteur
        self.nbSalle = longueur + hauteur
        self.nbMonstre = int(longueur / hauteur)
        
        
        self.laby = []
        for i in range(hauteur):
            self.laby.append([2 for i in range(self.longueur)])
       
        self.map = []
        for i in range(hauteur):
            self.map.append([2 for i in range(self.longueur)])
       
        
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

        self.listeCouloir = [self.Couloir1,self.Couloir2]
        self.listeSalle = [self.Salle1,self.Salle2,self.Salle3,self.Salle4,self.Salle5,self.Salle6,self.Sauvegarde1,self.Sauvegarde2]
        
    
    def ecrireFichier(self):
        f = open("ListeLaby.txt","w")
        f.write(str(self.mapFinale))
        f.close()

    def afficheLaby(self):
        return self.laby
    
    def getMap(self):
        return self.mapFinale


    def __directions_possibles(self,i,j):
        directions = []
        if j < self.hauteur -1:
            if not self.laby[i][j+1] == 4 :
                directions.append('S')
        if j-1 >=0 :
            if self.laby[i][j-1] != 4:
                directions.append('N')
        if i < self.longueur - 1:
            if not self.laby[i+1][j] == 4:
                directions.append('E')
        if i -1 >= 0 :
            if self.laby[i-1][j] != 4:    
                directions.append('W')
        return directions            



    def __abattre_mur(self,i,j,dire,pile):

        if dire == 'S':
            self.map[i][j][9][4] = 0 
            self.map[i][j][9][5] = 0 
            self.map[i][j+1][0][4] = 0
            self.map[i][j+1][0][5] = 0
            self.laby[i][j+1] = 4
            pile.empiler((i, j+1))
        if dire == 'N': 
            self.map[i][j][0][4] = 0
            self.map[i][j][0][5] = 0
            self.map[i][j-1][9][4] = 0 
            self.map[i][j-1][9][5] = 0 
            self.laby[i][j-1] = 4
            pile.empiler((i, j-1))
        if dire == 'W':
            self.map[i][j][4][0] = 0
            self.map[i][j][5][0] = 0
            self.map[i-1][j][4][9] = 0
            self.map[i-1][j][5][9] = 0
            self.laby[i-1][j] = 4
            pile.empiler((i-1, j))
        if dire == 'E':
            self.map[i][j][4][9] = 0
            self.map[i][j][5][9] = 0
            self.map[i+1][j][4][0] = 0
            self.map[i+1][j][5][0] = 0
            self.laby[i+1][j] = 4
            pile.empiler((i+1, j))




    def genereLaby(self):
        pile = Pile()
        
        typeCase = [1] * self.nbSalle
        CaseDepart = (randint(0,self.longueur - 1 ),randint(0,self.hauteur - 1))
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
                if self.map[i][j] == 2:
                    self.map[i][j] = choice(self.listeCouloir)
                if self.map[i][j] == 3:
                    self.map[i][j] = choice(self.listeSalle)
                    if self.map[i][j] == self.Sauvegarde1 or self.map[i][j] == self.Sauvegarde2:
                        self.listeSalle.remove(self.Sauvegarde1)
                        self.listeSalle.remove(self.Sauvegarde2)                
        
        
        
#Generation des ouvertures , des passages du labyrinthe        
        self.laby[CaseDepart[0]][CaseDepart[1]] = 4
        while not pile.est_vide():
            c = pile.depiler()
            liste = self.__directions_possibles(c[0],c[1])
            if len(liste) > 1:
                pile.empiler(c)
            if len(liste) > 0:
                self.__abattre_mur(c[0],c[1],choice(liste),pile)
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
                    self.game.ents.add_entity(Caisse(self, f"Caisse{str(num_caisse)}", 30, (i + 0.5, j + 0.5)))
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
    







