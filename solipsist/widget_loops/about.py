import sys
import pygame

from main import main_menu
from solipsist.widget_loops.game import MUSIC
from solipsist.pygame_utils import Button

from solipsist.GSS import j
from solipsist.GSS import SCREEN
from solipsist.GSS import WINDOW_HEIGHT
from solipsist.GSS import WINDOW_WIDTH
from solipsist.GSS import get_language


def about():
    _ = get_language()
    go_back_button = Button(
        _["go_back"],
        (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 15),
    )
    description_button = Button(
        _["about.description"],
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 2),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 20),
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
        description_button.draw_it(SCREEN)
        go_back_button.draw_it(SCREEN)
        pygame.display.flip()
