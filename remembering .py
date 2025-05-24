import sys #so the user can quit (by using exit method)
import pygame #here to create: game screen / game window 


Screen_width = 1200
Screen_height = 800
Game_title = "Alien Invasion"
class Alien_invasion:
    def __init__(self): #creating game assets / Behaviours 
        pygame.init()
        self.screen = pygame.display.set_mode((Screen_width , Screen_height)) #creating tuples for width , height in pixels
        pygame.display.set_caption(Game_title)
    def run_game(self):
        while True: #updating surface, displayed window the surface with player events or actions
            for events in pygame.event.get():
                if events == pygame.QUIT:
                    sys.exit()
        self.screen.fill((0, 0, 50)) 
        pygame.display.flip()