import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien and set starting position """

    def __init__(self, ai_settings, screen):
        """ Initialise alien and starting position """
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image and assign rect
        self.image = pygame.image.load("Assets/alien.bmp")  # Load the alien image and get its rect.
        self.rect = self.image.get_rect()  # Treat image as a rectangle.

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien to the screen"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """Return true if alien is hitting edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return  True
        elif self.rect.left <= 0:
            return  True

    def update(self):
        """ Moving to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x