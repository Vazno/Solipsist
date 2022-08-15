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
from GSS import get_language


def stats():
    _ = get_language()
    go_back_button = Button(
        _["go_back"],
        (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 15),
    )
    best_record_button = Button(
        f"{_['stats.best_record']}: {datetime.timedelta(seconds=j['stats']['BEST_RECORD'])}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 3),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    )
    clicks_button = Button(
        f"{_['clicks']}: {j['stats']['CLICKS']}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    )
    time_button = Button(
        f"{_['time_played']}: {datetime.timedelta(seconds=j['stats']['TIME_PLAYED'])}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2.4),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    )
    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"][j["graphic"]["theme"]])
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
