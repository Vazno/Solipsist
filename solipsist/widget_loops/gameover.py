import datetime
import sys
import pygame
import time

from widget_loops.game import MUSIC
from main import main_menu
from pygame_utils import Button

from GSS import save_json
from GSS import j
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH


def gameover(time_played: int, clicks: int):
    time_message = "Time played:"
    if time_played > j["stats"]["BEST_RECORD"]:
        j["stats"]["BEST_RECORD"] = time_played
        save_json()
        time_message = "New record!"
        MUSIC.sound_new_record()

    time.sleep(0.150)
    gameover_button = Button(
        "Gameover",
        (WINDOW_WIDTH / 2.6, WINDOW_HEIGHT / 10),
        (WINDOW_WIDTH / 5, WINDOW_HEIGHT / 5),
        False,
    )
    clicks_button = Button(
        f"Clicks: {clicks}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    time_button = Button(
        f"{time_message} {datetime.timedelta(seconds=time_played)}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2.4),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )

    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"])
        MUSIC.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MUSIC.stop()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                main_menu()

        clicks_button.draw_it(SCREEN)
        time_button.draw_it(SCREEN)
        gameover_button.draw_it(SCREEN)

        pygame.display.flip()
