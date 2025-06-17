import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        #Loading our Alient Game
        self.image = pygame.image.load('Images/Microsoft-Fluentui-Emoji-3d-Alien-Monster-3d.512.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        #Positioning our Alien/Alient fleet
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #storing the Alient position (Horizontal Position) 
        self.x = float(self.rect.x)