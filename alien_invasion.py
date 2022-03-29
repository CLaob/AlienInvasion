import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():

    # Initialise game and screen object
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Start Main Game Loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)





if __name__ == '__main__':
    run_game()