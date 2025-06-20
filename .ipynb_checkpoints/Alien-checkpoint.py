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
        self.settings = ai_game.settings
        
        #Positioning our Alien/Alient fleet
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #storing the Alient position (Horizontal Position) 
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >=  screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction #for math (float number), moving horizonrally to the right
        self.rect.x = self.x    #to show the alien on the screen both, self.x self.rect.x(.x and .self.rect are from "pygame.Rect") 


            