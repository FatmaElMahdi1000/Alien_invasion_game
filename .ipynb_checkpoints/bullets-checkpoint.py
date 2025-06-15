import pygame
from pygame import Sprite #class of pygame

class bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #create a bullet 
        self.rect = pygame.rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        
    def update(self):                #A Method to move the bullet/ updating the bullet positions
        self.y -= self.settings.bullet_speed        #bullet speed is 2 px
        self.rect.y = self.y         #updating self.y with the new value
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)