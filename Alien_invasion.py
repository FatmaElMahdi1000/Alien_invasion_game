from scoreboard import Score 
from ExitButton import Exit_Button
from time import sleep
from button import Button
from Gamestat import GameStat
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
        pygame.mixer.music.load("Music/Speedier Than Photons.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.music_playing = True
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(Game_Title)

        self.settings = self
        self.stats = GameStat(self)
        self.sb = Score(self) #making an instance/object of Score class here in Alient invasion 
        self.play_button = Button(self, "Play") 
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.game_active = False #start the game in an inactive state
        self.paused = False

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()

            if self.game_active and not self.paused:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self.bullets.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()     #This gives you the (x, y) position of where the player clicked. 
                self._check_play_button(mouse_pos)
                self._check_Exit_Button(mouse_pos)
 
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) #button clicked means the value of self.game_active = True now, not false
        if button_clicked and not self.game_active: 
            """
            When the game IS active (currently playing):
            self.game_active = True
            not self.game_active = not True = False
            So the condition becomes: button_clicked and False
            Result: Even if button is clicked, do nothing 🚫
            """
            self.settings.initialize_dynamic_setting()
            self.stats.reset_stat()   ##reset game stats
            self.sb.prep_score() ##prepping the score when starting a new game, a score of 0
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            self.bullets.empty()###getting red of any remaining bullets and alients, then creating new fleet/centering the ship
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

                
    def _check_Exit_Button(self, mouse_pos):
        if hasattr(self, 'Exit_Button'):
            if self.Exit_Button.rect.collidepoint(mouse_pos) and not self.game_active:
                sys.exit()
                
    def _check_keydown_event(self, event):
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.paused = not self.paused
            if self.paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
                 
        elif event.key == pygame.K_m:  # Press 'M' to mute/unmute
            if self.music_playing:
                pygame.mixer.music.pause()
                self.music_playing = False
            else:
                pygame.mixer.music.unpause()
                self.music_playing = True

    def _check_keyup_event(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #creating a dictionary.
        
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points *  len(alien)
                self.sb.prep_score()
                self.sb.check_high_score()
                self.sb.prep_level()
                
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _update_screen(self):
        self.screen.fill(self.bg_colour)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        
        if not self.game_active:
            self.play_button.draw_button()
            if hasattr(self, 'Exit_Button'):
                self.Exit_Button.draw_button()
        pygame.display.flip()

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.screen_height - 3 * alien_height):
            while current_x < (self.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _ship_hit(self):
        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:   #2, 1, 0, check this 2>0, 1>0, 0
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False
            self.Exit_Button = Exit_Button(self, "Exit")
            pygame.mouse.set_visible(True)
            self._update_screen() #updating screen immediately 


    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_height:
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
