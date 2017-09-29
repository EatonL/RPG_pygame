import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("杨思远的幸福生活")
    ship = Ship(screen)

    while 1:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        

run_game()