from Global import *

class Render:
    def __init__(self, game):
        self.game = game
        # Distance au mur pour chaque ligne verticale de l'ecran: pour affichage entitées
        self.z_buffer = [None for i in range(WIDTH)]
        self.weapon_bobbing_i = 0

    def rendu_entite(self):
        #Rendu des entité de la plus loin a la plus proche
        sorted_ent = self.game.ents.index_sorted_dist(self.game.joueur)
        joueur = self.game.joueur

        #Pour chanque entité (plus loin à plus proche)
        for paire in sorted_ent:
            ent = self.game.ents.get_entity(paire[0])   # Récuperer l'instance de l'entité
            ent.drawn = False
            dist = paire[1] # Distance au joueur
            if dist < 0.07: continue

            # Position relative à la caméra
            rel_pos_x = ent.x - joueur.x
            rel_pos_y = ent.y - joueur.y
            # Déterminant de la matrice joueur inversé
            inv_det = 1 / (joueur.camPlaneX * joueur.dirY - joueur.dirX * joueur.camPlaneY)

            transformX = inv_det * (joueur.dirY * rel_pos_x - joueur.dirX * rel_pos_y)
            transformY = inv_det * (-joueur.camPlaneY * rel_pos_x + joueur.camPlaneX * rel_pos_y)
            
            if transformY <= 0: continue    # Si l'entité est deriere le joueur: ne pas l'afficher
            
            spriteScreenX = int((WIDTH / 2) * (1 + transformX / transformY))

            spriteHeight = abs(int(HEIGHT / (transformY)))
			
            if spriteHeight >= 5*HEIGHT: continue   # Si l'entité fait plus de 5 fois la taille de l'ecran: ne pas l'afficher

            offY = 0
            drawStartY = -spriteHeight / 2 + HEIGHT / 2
            drawEndY = spriteHeight / 2 + HEIGHT / 2
            if drawStartY < 0:
                offY = abs(drawStartY)
                drawStartY = 0
            if drawEndY >= HEIGHT : drawEndY = HEIGHT - 1

            spriteWidth = abs( int(HEIGHT / (transformY)))
            
            offX = 0
            drawStartX = -spriteWidth / 2 + spriteScreenX
            drawEndX = spriteWidth / 2 + spriteScreenX
            if drawStartX < 0 :
                offX = abs(drawStartX)
                drawStartX = 0
            if drawEndX >= WIDTH : drawEndX = WIDTH - 1
            
            # Ne pas afficher l'entité si en dehors de l'ecran
            if drawStartX >= WIDTH: continue
            if drawEndX <= 0: continue

            draw_offsets = []
            i = 0
            offset_start = -1

            # Géneration de slices de l'image de l'entité
            while i < drawEndX - drawStartX:
                x_indx = int(drawStartX + i)
                if x_indx > WIDTH:
                    if offset_start != -1:
                        draw_offsets.append((offset_start, WIDTH))
                        offset_start = -1
                    break
                if self.z_buffer[x_indx] > transformY:
                    if offset_start == -1:
                        offset_start = i
                else:
                    if offset_start != -1:
                        draw_offsets.append((offset_start, i))
                        offset_start = -1
                i += 1
            if offset_start != -1:
                draw_offsets.append((offset_start, drawEndX - drawStartX))
            if len(draw_offsets) == 0:
                continue    # PASSE AU SPRITE SUIVANT
            
            ent_surface_scale = pygame.transform.scale(ent.get_texture(), (spriteWidth, spriteHeight))

            ent.drawn = True

            # Affichage des slices
            for debut, fin in draw_offsets:
                self.add(ent_surface_scale, (drawStartX + debut,drawStartY), pygame.Rect(debut + offX, offY, fin, spriteHeight))


    def rendu_armes(self):
        """
        Affichage de l'arme:
        Deplacement haut-bas de l'arme quand le joueur se déplace grace a une fonction
        sinusoidale.
        """
        arme = self.game.joueur.arme
        texture = arme.texture
        position = arme.screen_pos

        if self.game.joueur.isMoving:
            position = (position[0], position[1] + int(math.sin(self.weapon_bobbing_i)*10))
            if self.game.joueur.isRunning:
                self.weapon_bobbing_i += math.pi / 10
            else:
                self.weapon_bobbing_i += math.pi / 20
        else:
            self.weapon_bobbing_i = 0

        self.add(texture, position)


    def rendu(self):
        """
        Rendu du monde:
        Calcul pour chaque ligne verticale la distance orthogonale au plan de la camera
        Affichage de ligne de taille proportionelle a la distance
        """
        for scr_w in range(WIDTH):
            cameraX = 2 * scr_w / WIDTH - 1
            rayDirX = self.game.joueur.dirX + self.game.joueur.camPlaneX * cameraX
            rayDirY = self.game.joueur.dirY + self.game.joueur.camPlaneY * cameraX

            mapX = int(self.game.joueur.x)
            mapY = int(self.game.joueur.y)

            if rayDirX != 0:
                deltaDistX = abs(1/rayDirX)
            else:
                deltaDistX = 10000000000000  #inf

            if rayDirY != 0:
                deltaDistY = abs(1/rayDirY)
            else:
                deltaDistY = 10000000000000  #inf


            if rayDirX < 0:
                stepX = -1
                sideDistX = (self.game.joueur.x - mapX) * deltaDistX
            else:
                stepX = 1
                sideDistX = (mapX + 1 - self.game.joueur.x) * deltaDistX

            if rayDirY < 0:
                stepY = -1
                sideDistY = (self.game.joueur.y - mapY) * deltaDistY
            else:
                stepY = 1
                sideDistY = (mapY + 1 - self.game.joueur.y) * deltaDistY


            #Algorithme de détection du point de colision rayon-mur
            hit = 0
            while not hit:
                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    mapX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapY += stepY
                    side = 1

                if mapX < 0 or mapY < 0 or mapX >= len(self.game.carte) or mapY >= len(self.game.carte[mapX]): break # En dehors de la carte
                if self.game.carte[mapX][mapY]:
                    hit = 1
            if hit==0: continue # En dehors de la carte

            if side == 0: wallDist = sideDistX - deltaDistX
            else: wallDist = sideDistY - deltaDistY

            self.z_buffer[scr_w] = wallDist

            if wallDist==0: continue

            lineHeight = HEIGHT // wallDist

            lineStart = -lineHeight/2 + HEIGHT/2
            if lineStart < 0: lineStart = 0
            
            lineEnd = lineHeight//2 + HEIGHT//2
            if lineEnd >= HEIGHT: lineEnd = HEIGHT - 1
            
            case_touche = self.game.carte[mapX][mapY]
            r = 0
            g = 0
            b = 0
            if case_touche == 1:
                r = 200
            elif case_touche == 2:
                g = 200
            elif case_touche == 3:
                b = 200
            elif case_touche == 4:
                r = 200
                g = 200
                b = 200
            else:
                g = 200
                b = 200
            
            # Fausse ombre
            if side == 1:
                r//=2
                g//=2
                b//=2

            pygame.draw.line(self.game.pygame_screen,
                             pygame.Color(r,g,b),
                             (scr_w, lineStart),
                             (scr_w, lineEnd))

    def add(self, surface_to_add, dest = (0,0), rect = None):
        #Racourcis pour blit sur la surface de la fenetre
        self.game.pygame_screen.blit(surface_to_add, dest, rect)