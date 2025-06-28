import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, screen, center, duration=1200):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('Images/explosion2.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.start_time = pygame.time.get_ticks()
        self.duration = duration

    def update(self):
        # Remove the explosion after `duration'  milliseconds
        now = pygame.time.get_ticks()
        if now - self.start_time > self.duration:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
