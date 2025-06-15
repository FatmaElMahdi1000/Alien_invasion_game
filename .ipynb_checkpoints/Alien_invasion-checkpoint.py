# Main game file
from ourship import Ship
from bullets import bullet
from settings import Settings
import sys
import pygame

Game_Title = "Alien Invasion"

class AlienInvasion(Settings):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(Game_Title)
        self.settings = self
        # Create the ship
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullet = pygame.sprite.Group()
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()  # Added missing screen update call
            self.bullet.update()  #updating bullet position while moving and being fired.
          
    def _check_events(self):  # Fixed method name - missing underscore
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:##
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                    
    def _check_keydown_event(self, event): #pressing buttons
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
            
    def _check_keyup_event(self, event): #releasing buttons
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self): #method to call to fire / create a bullet everytime, player press the spacebar
        new_bullets = bullets(self) ##giving bullet file or the bullets an access to this file. 
        self.bullet.add(new-bullets)
            
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
