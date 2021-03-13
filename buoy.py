import pygame


class Buoy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Buoy, self).__init__()
        self.surf = pygame.image.load("images/buoy.png").convert()
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
