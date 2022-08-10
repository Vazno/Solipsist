import sys
import pygame

from GSS import SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, save_json
from GSS import j
from main import main_menu
from game import MUSIC
from pygame_utils import Button, InputBox


def options():
    go_back_button = Button(
        "Go back",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    volume_button = Button(
    f"Music volume {j['music']['VOLUME']}",
    (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 3),
    (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    False
    )
    fps_button = Button(
    "FPS",
    (WINDOW_WIDTH / 2.4, WINDOW_HEIGHT / 2.05),
    (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
    False
    )

    fps_input_box = InputBox(WINDOW_WIDTH/2.1, WINDOW_HEIGHT/2, WINDOW_WIDTH/25, WINDOW_HEIGHT/25, str(j["game_settings"]["FPS"]))

    run = True
    while run:
        events = pygame.event.get()
        SCREEN.fill(j["graphic"]["BACKGROUND"])
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            fps_input_box.handle_event(event)

        if fps_input_box.active is True:
            try:
                j['game_settings']['FPS'] = int(fps_input_box.text)
                save_json()
            except ValueError:
                pass

        if volume_button.clicked(events):
            if j['music']['VOLUME'] >= 1:
                j['music']['VOLUME'] = 0
            else:
                j['music']['VOLUME'] = round(j['music']['VOLUME'] + 0.1, 1)
            save_json()
            volume_button.change_text(f"Music volume {j['music']['VOLUME']}")

        if go_back_button.clicked(events):
            MUSIC.sound_menu_click()
            main_menu()

        volume_button.draw_it(SCREEN)
        fps_button.draw_it(SCREEN)
        go_back_button.draw_it(SCREEN)
        fps_input_box.draw_it(SCREEN)
        fps_input_box.update()
        pygame.display.flip()