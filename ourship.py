# Ship file (ourship.py)
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen   # This line assigns the game's screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and scale it down to fit nicely
        self.image = pygame.image.load('Images/rocket-icon.bmp')
        self.image = pygame.transform.scale(self.image, (80, 70))  # Resize to 80x70 pixels
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        
        # Debug prints
        print("Ship image size:", self.image.get_size())
        print("Ship position (midbottom):", self.rect.midbottom)

    def update(self):
        if self.moving_right:
            self.rect.x += 3
        if self.moving_left: 
            self.rect.x -= 3
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)