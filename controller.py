import sys

import pygame

from Bala import Bala
from Gamer import Gamer

clock = pygame.time.Clock()

class GameController:
    def __init__(self):
        pygame.init()
        self.maxW = 800
        self.maxH = 500
        self.screen = pygame.display.set_mode((self.maxW, self.maxH))
        pygame.display.set_caption("IA GAME")
        self.color = (230, 230, 230)
        self.velocidad = 3
        self.anchobala = 8
        self.altobala = 5
        self.colorbala = (225, 0, 0)
        self.gamer = Gamer(self)
        self.balas = pygame.sprite.Group()
        self.balaTeclaPressed = ''

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.gamer.rigthMove = True
                    if event.key == pygame.K_LEFT:
                        self.gamer.leftMove = True
                    if event.key == pygame.K_UP:
                        self.gamer.upMove = True
                    if event.key == pygame.K_DOWN:
                        self.gamer.downMove = True
                    if event.key == pygame.K_w:
                        self.balaTeclaPressed = 'W'
                        self._fire_bala()
                    if event.key == pygame.K_d:
                        self.balaTeclaPressed = 'D'
                        self._fire_bala()
                    if event.key == pygame.K_a:
                        self.balaTeclaPressed = 'A'
                        self._fire_bala()
                    if event.key == pygame.K_s:
                        self.balaTeclaPressed = 'S'
                        self._fire_bala()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.gamer.rigthMove = False
                    if event.key == pygame.K_LEFT:
                        self.gamer.leftMove = False
                    if event.key == pygame.K_UP:
                        self.gamer.upMove = False
                    if event.key == pygame.K_DOWN:
                        self.gamer.downMove = False

            self.gamer.mover()
            self.screen.fill(self.color)
            self.gamer.toRun()
            self.balas.update()
            for bala in self.balas.copy():
                if bala.rect.bottom <= 0:
                    self.balas.remove(bala)
                elif bala.rect.bottom > self.maxH:
                    self.balas.remove(bala)
                elif bala.rect.x == 0:
                    self.balas.remove(bala)
                elif bala.rect.x == self.maxW:
                    self.balas.remove(bala)

            for bala in self.balas.sprites():
                bala.dibujarbala()
            pygame.display.flip()
            clock.tick(60)

    def _fire_bala(self):
        newBala = Bala(self)
        newBala.teclaPress = self.balaTeclaPressed
        self.balas.add(newBala)


if __name__ == "__main__":
    a = GameController()
    a.runGame()
