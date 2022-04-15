import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.image = pygame.transform.scale(pygame.image.load('assets/BALA.png').convert(), (25, 30))
        self.rect = self.image.get_rect()
        self.rect.midtop = a_game.gamer.rect.midtop
        self.juego = a_game
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.teclaPress = ''

    def update(self):
        if self.teclaPress == 'W':
            self.image = pygame.transform.scale(pygame.image.load('assets/BALA3.png').convert(), (25, 30))
            self.y -= self.juego.velocidad
            self.rect.y = self.y
        if self.teclaPress == 'D':
            self.image = pygame.transform.scale(pygame.image.load('assets/BALA.png').convert(), (25, 30))
            self.x += self.juego.velocidad
            self.rect.x = self.x
        if self.teclaPress == 'S':
            self.image = pygame.transform.scale(pygame.image.load('assets/BALA2.png').convert(), (25, 30))
            self.y += self.juego.velocidad
            self.rect.y = self.y
        if self.teclaPress == 'A':
            self.image = pygame.transform.scale(pygame.image.load('assets/BALA4.png').convert(), (25, 30))
            self.x -= self.juego.velocidad
            self.rect.x = self.x

    def dibujarbala(self):
        self.screen.blit(self.image, self.rect)
