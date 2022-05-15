import pygame


class Ship():

    def __init__(self,  ai_settings, screen):
        """ Intialize the ship and set its starting positions """
        self.screen = screen
        self.ai_setting = ai_settings
        self.image = pygame.image.load("Assets/ship.bmp")  # Load the ship image and get its rect.
        self.rect = self.image.get_rect()  # Treat image as a rectangle.
        self.screen_rect = screen.get_rect() # Load image to shape
        self.rect.centerx = self.screen_rect.centerx  # Start at the bottom of the screen
        self.rect.centery = self.screen_rect.centery  # Start at the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom  # Start at the bottom of the screen
        self.center = float(self.rect.centerx) # for movement of ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship's position based on the movement flag  """
        if self.moving_right and self.rect.right < self.screen_rect.right: # check if right edge met
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0: #check if left edge met
            self.center -= self.ai_setting.ship_speed_factor

        if self.moving_up and self.rect.centery > self.screen_rect.top: #check if top edge met 
            self.rect.centery -= self.ai_setting.ship_speed_factor

        if self.moving_down and self.rect.centery < self.screen_rect.bottom: #check if bottom edge met
       
            self.rect.centery += self.ai_setting.ship_speed_factor


        self.rect.centerx = self.center






