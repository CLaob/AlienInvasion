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
        self.rect.bottom = self.screen_rect.bottom  # Start at the bottom of the screen
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship's position based on the movement flag  """
        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center






