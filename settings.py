class Settings:
    def __init__(self):
        self.screen_height  = 1200 #dummy value, I'll override the values in alien_invasion file
        self.screen_width = 200 #dummy value, I'll override the values in alien_invasion file
        self.bg_colour = (255, 255, 255)  # Bright cyan for easy ship visibility
        self.ship_speed = 1.5
        self.ship_limit = 3
        #bullet_settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        #Alien_settings 
        self.alien_speed = 1.0 #alien's horizontal speed, movement 
        self.fleet_drop_speed = 10 #alien's vertical speed.
        #self.fleed_direction = 1, means moving right, -1 means moving left
        self.fleet_direction = 1
        
        