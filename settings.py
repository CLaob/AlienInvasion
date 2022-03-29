class Settings():
    """ Class will strore all setting mode of the game """

    def __init__(self):
        """ Intialise the game's settings """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # ship Setting
        self.ship_speed_factor = 1.1
