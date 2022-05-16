from email.headerregistry import Group
import imp
import pygame
from bullet import Bullet
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():

    # Initialise game and screen object
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Store bullets and fleet of aliens
    bullets = Group()
    aliens = Group()

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Create a fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start Main Game Loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)





if __name__ == '__main__':
    run_game()