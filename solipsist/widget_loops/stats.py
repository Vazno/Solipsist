import sys
import pygame
import datetime

from widget_loops.game import MUSIC
from main import main_menu
from pygame_utils import Button

from GSS import j
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH


def stats():
    run = True
    best_record_button = Button(
        f"Best record: {datetime.timedelta(seconds=j['stats']['BEST_RECORD'])}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 3),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    go_back_button = Button(
        "Go back",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    clicks_button = Button(
        f"Clicks: {j['stats']['CLICKS']}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    time_button = Button(
        f"Time played: {datetime.timedelta(seconds=j['stats']['TIME_PLAYED'])}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2.4),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
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
        best_record_button.draw_it(SCREEN)
        clicks_button.draw_it(SCREEN)
        time_button.draw_it(SCREEN)
        go_back_button.draw_it(SCREEN)
        pygame.display.flip()
