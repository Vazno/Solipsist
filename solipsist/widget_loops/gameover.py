import datetime
import sys
import pygame
import time

from main import main_menu
from solipsist.widget_loops.game import MUSIC
from solipsist.pygame_utils import Button

from solipsist.GSS import save_json
from solipsist.GSS import get_language
from solipsist.GSS import j
from solipsist.GSS import SCREEN
from solipsist.GSS import WINDOW_HEIGHT
from solipsist.GSS import WINDOW_WIDTH


def gameover(time_played: int, clicks: int):
    _ = get_language()
    time_message = f"{_['time_played']}:"
    if time_played > j["stats"]["BEST_RECORD"]:
        j["stats"]["BEST_RECORD"] = time_played
        save_json()
        time_message = _["gameover.new_record"]
        MUSIC.sound_new_record()

    time.sleep(0.150)
    gameover_button = Button(
        _["gameover.gameover"],
        (WINDOW_WIDTH / 2.6, WINDOW_HEIGHT / 10),
        (WINDOW_WIDTH / 5, WINDOW_HEIGHT / 5),
    )
    clicks_button = Button(
        f"{_['clicks']}: {clicks}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    )
    time_button = Button(
        f"{time_message} {datetime.timedelta(seconds=time_played)}",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2.4),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    )

    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"][j["graphic"]["theme"]])
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
