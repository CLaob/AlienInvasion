import sys
import pygame
from bullet import Bullet


def check_events(ai_settings,screen,ship,bullet):

    """Keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen,ship,bullet)
        

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event,ai_setting,screen, ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and add it to bullet groups 
        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)



def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False





def update_screen(ai_settings,screen,ship,bullets):
    """ Update images on the screen and flip to the new screen """

    screen.fill(ai_settings.bg_colour)  # Keep redrawing screen

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()  # Most recently drawn screen visible



