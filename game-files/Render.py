from Global import *

class Render:
    def __init__(self, game):
        self.game = game

    def rendu(self):
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

                if self.game.carte[mapX][mapY]:
                    hit = 1

            if side == 0: wallDist = sideDistX - deltaDistX
            else: wallDist = sideDistY - deltaDistY
            
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
            
            if side == 1:
                r//=2
                g//=2
                b//=2

            pygame.draw.line(self.game.pygame_screen,
                             pygame.Color(r,g,b),
                             (scr_w, lineStart),
                             (scr_w, lineEnd))

    def add(self, surface_to_add):
        self.game.pygame_screen.blit(surface_to_add, (0,0))