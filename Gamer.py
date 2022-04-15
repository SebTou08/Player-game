import pygame.image


class Gamer:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("QUIETO25.jpg")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rigthMove = False
        self.leftMove = False
        self.upMove = False
        self.downMove = False

    def mover(self):
        if self.rigthMove and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.upMove and self.rect.y > 0:
            self.rect.y -= 1
        if self.leftMove and self.rect.x >0:
            self.rect.x -=1
        if self.downMove and self.rect.midbottom < self.screen_rect.midbottom:
            self.rect.y +=1

    def toRun(self):
        self.screen.blit(self.image, self.rect)