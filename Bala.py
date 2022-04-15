import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.rect = pygame.Rect(0, 0, a_game.anchobala, a_game.altobala)
        self.rect.midtop = a_game.gamer.rect.midtop
        self.juego = a_game
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.teclaPress = ''

    def update(self):
        if self.teclaPress == 'W':
            self.y -= self.juego.velocidad
            self.rect.y = self.y
        if self.teclaPress == 'D':
            self.x += self.juego.velocidad
            self.rect.x = self.x
        if self.teclaPress == 'S':
            self.y += self.juego.velocidad
            self.rect.y = self.y
        if self.teclaPress == 'A':
            self.x -= self.juego.velocidad
            self.rect.x = self.x

    def dibujarbala(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
