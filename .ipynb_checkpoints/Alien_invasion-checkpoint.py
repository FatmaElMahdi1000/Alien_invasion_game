import sys #control when project exit the game
import pygame 

##pygame window/ Game window creation 

Screen_width = 1200
Screen_height = 800 
Game_Title = "Alien Invasion"

class AlienInvasion: #class for managing game assets and behaviours
    def __init__(self): #initialize the game, create resources.
        pygame.init()
        self.screen = pygame.display.set_mode((Screen_width, Screen_height)) #creates a screen/ our surface where all game elements are going to be displayed.it's stored in self.screen
        pygame.display.set_caption(Game_Title) 
    def run_game(self):
        #start the main loop for the game
        while True:
            """Watch for events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 50)) 
            pygame.display.flip() 

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        
        
        