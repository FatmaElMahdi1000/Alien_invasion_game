# Main game file
from ourship import Ship
from Alien import Alien
from bullets import Bullet
from settings import Settings
import sys
import pygame

Game_Title = "Alien Invasion"

class AlienInvasion(Settings):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.Screen_width = self.screen.get_rect().width
        self.Screen_height = self.screen.get_rect().height
        pygame.display.set_caption(Game_Title)
        self.settings = self
        # Create the ship
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet() #Calling the helper method
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()  # Added missing screen update call
            self._update_bullets()
            self.bullets.update()   #updating bullet position while moving and being fired
            self.clock.tick(60)
          
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_event(self, event): #releasing buttons
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self): #method to call to fire / create a bullet everytime, player press the spacebar
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullets = Bullet(self) ##giving bullet file or the bullets an access to this file. 
            self.bullets.add(new_bullets)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):  # Fixed method name
                # Change background color to a bright one for visibility
        self.screen.fill(self.bg_colour)  # Fixed attribute access
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
    def _create_fleet(self):
        alien = Alien(self) #creating one instance of Alien
        alien_width = alien.rect.width
        current_x = alien_width

        while current_x < (self.settings.Screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width
            
if __name__ == '__main__':  # Fixed dunder name check
    ai = AlienInvasion()
    ai.run_game()
