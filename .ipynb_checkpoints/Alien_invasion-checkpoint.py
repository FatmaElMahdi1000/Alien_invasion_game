# Main game file
from ourship import Ship
from settings import Settings
import sys
import pygame

Game_Title = "Alien Invasion"

class AlienInvasion(Settings):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.screen = pygame.display.set_mode((self.Screen_width, self.Screen_height))
        pygame.display.set_caption(Game_Title)
        # Create the ship
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()  # Added missing screen update call
          
    def _check_events(self):  # Fixed method name - missing underscore
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True 
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                        
    def _update_screen(self):  # Fixed method name
        # Change background color to a bright one for visibility
        self.screen.fill(self.bg_colour)  # Fixed attribute access
        # Draw the ship
        self.ship.blitme()
        self.ship.update()
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':  # Fixed dunder name check
    ai = AlienInvasion()
    ai.run_game()
