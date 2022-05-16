class Settings():
    """ Class will store all setting mode of the game """

    def __init__(self):
        """ Initialise the game's settings """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # ship Setting
        self.ship_speed_factor = 1.1

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction  1 = right ; -1 = left
        self.fleet_direction = 1

