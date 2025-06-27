import pygame
from button import Button 

class Exit_Button(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 80
        self.msg_image_rect.center = self.rect.center
 
        