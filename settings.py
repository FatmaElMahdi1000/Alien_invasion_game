class Settings:
    def __init__(self):
        self.Screen_width = 1200 #dummy value, I'll override the values in alien_invasion file
        self.Screen_height = 200 #dummy value, I'll override the values in alien_invasion file
        self.bg_colour = (255, 255, 255)  # Bright cyan for easy ship visibility
        self.ship_speed = 1.5
        #bullet_settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        