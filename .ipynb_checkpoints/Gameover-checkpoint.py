import pygame
from pygame.font 

class Gameover: 
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = (200, 200)