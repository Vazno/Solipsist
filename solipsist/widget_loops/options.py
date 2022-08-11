import sys
import pygame

from GSS import SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, save_json
from GSS import j
from main import main_menu
from widget_loops.game import MUSIC
from pygame_utils import Button, InputBox


def options():
    go_back_button = Button(
        "Go back",
        (WINDOW_WIDTH / 2.2, WINDOW_HEIGHT / 1.5),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    volume_button = Button(
        f"Music volume: {j['music']['VOLUME']}",
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 4),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    effect_volume_button = Button(
        f"Effect volume: {j['music']['EFFECT_VOLUME']}",
        (WINDOW_WIDTH / 2.3, WINDOW_HEIGHT / 4.9),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    fps_button = Button(
        "FPS:",
        (WINDOW_WIDTH / 2.6, WINDOW_HEIGHT / 3.05),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    full_screen_button = Button(
        f"Full Screen: {j['graphic']['FULL_SCREEN']}",
        (WINDOW_WIDTH / 2.65, WINDOW_HEIGHT / 2.15),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    width_button = Button(
        "Width:",
        (WINDOW_WIDTH / 2.65, WINDOW_HEIGHT / 1.85),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )
    height_button = Button(
        "Height:",
        (WINDOW_WIDTH / 2.69, WINDOW_HEIGHT / 1.69),
        (WINDOW_WIDTH / 15, WINDOW_HEIGHT / 15),
        False,
    )

    fps_input_box = InputBox(
        WINDOW_WIDTH / 2.1,
        WINDOW_HEIGHT / 2.9,
        WINDOW_WIDTH / 25,
        WINDOW_HEIGHT / 25,
        str(j["game_settings"]["FPS"]),
    )
    window_width_box = InputBox(
        WINDOW_WIDTH / 2.1,
        WINDOW_HEIGHT / 1.8,
        WINDOW_WIDTH / 25,
        WINDOW_HEIGHT / 25,
        str(WINDOW_WIDTH),
    )
    window_height_box = InputBox(
        WINDOW_WIDTH / 2.1,
        WINDOW_HEIGHT / 1.65,
        WINDOW_WIDTH / 25,
        WINDOW_HEIGHT / 25,
        str(WINDOW_HEIGHT),
    )
    run = True
    while run:
        events = pygame.event.get()
        SCREEN.fill(j["graphic"]["BACKGROUND"])
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            fps_input_box.handle_event(event)
            window_width_box.handle_event(event)
            window_height_box.handle_event(event)

        if fps_input_box.active is True:
            try:
                j["game_settings"]["FPS"] = int(fps_input_box.text)
                save_json()
            except ValueError:
                pass

        if window_width_box.active is True:
            try:
                j["graphic"]["resolution"] = [
                    int(window_width_box.text),
                    int(window_height_box.text),
                ]
                save_json()
            except ValueError:
                pass

        if window_height_box.active is True:
            try:
                j["graphic"]["resolution"] = [
                    int(window_width_box.text),
                    int(window_height_box.text),
                ]
                save_json()
            except ValueError:
                pass

        if volume_button.clicked(events):
            if j["music"]["VOLUME"] >= 1:
                j["music"]["VOLUME"] = 0.0
            else:
                j["music"]["VOLUME"] = round(j["music"]["VOLUME"] + 0.1, 1)
            save_json()
            volume_button.change_text(f"Music volume: {j['music']['VOLUME']}")

        if effect_volume_button.clicked(events):
            if j["music"]["EFFECT_VOLUME"] >= 1:
                j["music"]["EFFECT_VOLUME"] = 0.0
            else:
                j["music"]["EFFECT_VOLUME"] = round(j["music"]["EFFECT_VOLUME"] + 0.1, 1)
            save_json()
            effect_volume_button.change_text(f"Effect volume: {j['music']['EFFECT_VOLUME']}")

        if full_screen_button.clicked(events):
            full_screen = not j["graphic"]["FULL_SCREEN"]
            j["graphic"]["FULL_SCREEN"] = full_screen
            save_json()
            full_screen_button.change_text(
                f"Full Screen: {j['graphic']['FULL_SCREEN']}"
            )

        if go_back_button.clicked(events):
            MUSIC.sound_menu_click()
            main_menu()

        go_back_button.draw_it(SCREEN)
        effect_volume_button.draw_it(SCREEN)
        volume_button.draw_it(SCREEN)

        fps_button.draw_it(SCREEN)
        fps_input_box.draw_it(SCREEN)
        fps_input_box.update()

        full_screen_button.draw_it(SCREEN)

        height_button.draw_it(SCREEN)
        window_height_box.draw_it(SCREEN)
        window_height_box.update()

        width_button.draw_it(SCREEN)
        window_width_box.draw_it(SCREEN)
        window_width_box.update()

        pygame.display.flip()
