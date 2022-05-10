import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __innit__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet,self).__init__
        self.screen= screen

        # Create a bullet rect 
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height) 
        self.rect.centerx = ship.rect.centerxx
        self.rect.top = ship.rect.top

        # Store bullet's position as decimal value 
        self.y = float(self.rect.y)

        # Set color 
        self.colour = ai_settings.bullet.colour

        # Set Speed
        self.speed_factor = ai_settings.bullet_speed_factor 


    def update(self):
        """Move the bullet up the screen"""

        #Update decimal position of the bullet 
        self.y -= self.speed_factor
        #Update rect position 
        self.rect.y = self.y 

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen,self.colour,self.rect)
        