# Ship file (ourship.py)
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game): 
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen   # This line assigns the game's screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and scale it down to fit nicely
        self.image = pygame.image.load('Images/q4p9_rmax_210520 (1).bmp')
        self.image = pygame.transform.scale(self.image, (80, 90))  
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        
        # Debug prints
        print("Ship image size:", self.image.get_size())
        print("Ship position (midbottom):", self.rect.midbottom)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)