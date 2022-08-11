import sys
import pygame

from widget_loops.game import MUSIC
from main import main_menu
from pygame_utils import Button

from GSS import j
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH


def about():
    go_back_button = Button(
        "Go back",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    description_button = Button(
        j["DESCRIPTION"],
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 19, WINDOW_HEIGHT / 19),
        False,
    )
    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        if go_back_button.clicked(events):
            MUSIC.sound_menu_click()
            main_menu()
        description_button.draw_it(SCREEN)
        go_back_button.draw_it(SCREEN)
        pygame.display.flip()
