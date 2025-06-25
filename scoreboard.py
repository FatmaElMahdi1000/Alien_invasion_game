import pygame.font

class Score:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        #font settings
        self.text_colour = (30, 30, 30) #RGB
        self.font = pygame.font.SysFont(None, 48) #None means the standard font.
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)    
        self.score_image = self.font.render(score_str,True, self.text_colour,self.settings.bg_colour) #color of text, back ground, the text itself
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 #place the top edge 20 px down from the top of the screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)