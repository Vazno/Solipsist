import sys

import pygame

from GSS import GAME_NAME, SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, j
from GSS import get_language
from widget_loops.game import MUSIC, main
from pygame_utils import Button
from utils import resource_path

# Some imports are below, to prevent circular import


def main_menu():
    _ = get_language()

    pygame.display.set_caption(GAME_NAME)
    pygame.init()

    game_icon = pygame.image.load(resource_path("icon.png"))
    pygame.display.set_icon(game_icon)
    clock = pygame.time.Clock()

    solipsist_button = Button(
        "Solipsist",
        (WINDOW_WIDTH / 2.5, WINDOW_HEIGHT / 10),
        (WINDOW_WIDTH / 5, WINDOW_HEIGHT / 5),
    )
    start_button = Button(
        _["main_menu.start"],
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 3),
        (WINDOW_WIDTH / 10, WINDOW_HEIGHT / 15),
    )
    options_button = Button(
        _["main_menu.options"],
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 2.4),
        (WINDOW_WIDTH / 8, WINDOW_HEIGHT / 15),
    )
    stats_button = Button(
        _["main_menu.stats"],
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 10, WINDOW_HEIGHT / 15),
    )
    about_button = Button(
        _["main_menu.about"],
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 1.70),
        (WINDOW_WIDTH / 10, WINDOW_HEIGHT / 15),
    )
    quit_button = Button(
        _["main_menu.quit"],
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 10, WINDOW_HEIGHT / 15),
    )

    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"][j["graphic"]["theme"]])
        MUSIC.stop()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                MUSIC.stop()
                sys.exit()

        if start_button.clicked(events):
            MUSIC.sound_menu_click()
            main()

        if options_button.clicked(events):
            MUSIC.sound_menu_click()
            from widget_loops.options import options

            options()

        if stats_button.clicked(events):
            MUSIC.sound_menu_click()
            from widget_loops.stats import stats

            stats()

        if about_button.clicked(events):
            MUSIC.sound_menu_click()
            from widget_loops.about import about

            about()

        if quit_button.clicked(events):
            MUSIC.sound_menu_click()
            sys.exit()

        if solipsist_button.clicked(events):
            pass  # May add someting here, when player clicks logo

        solipsist_button.draw_it(SCREEN)
        start_button.draw_it(SCREEN)
        options_button.draw_it(SCREEN)
        stats_button.draw_it(SCREEN)
        about_button.draw_it(SCREEN)
        quit_button.draw_it(SCREEN)

        pygame.display.flip()
        clock.tick(j["game_settings"]["FPS"])


if __name__ == "__main__":
    main_menu()
