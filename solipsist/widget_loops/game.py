import pygame

import sys
from time import time

from GSS import GAME_NAME, GameStatus
from GSS import save_json
from GSS import j
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH
from pygame_utils import Solipsist, Obstacle

from music import Music

MUSIC = Music()


def main():
    pygame.display.set_caption(GAME_NAME)

    clock = pygame.time.Clock()
    game_status = GameStatus(is_game_started=False, gameover=False)
    if WINDOW_HEIGHT > WINDOW_WIDTH:
        solipsist = Solipsist(
            SCREEN,
            int(WINDOW_WIDTH / 3),
            int(WINDOW_HEIGHT / 4),
            int(WINDOW_WIDTH / 15),
            WINDOW_HEIGHT / 1500,
        )
    else:
        solipsist = Solipsist(
            SCREEN,
            int(WINDOW_WIDTH / 3),
            int(WINDOW_HEIGHT / 4),
            int(WINDOW_HEIGHT / 15),
            WINDOW_HEIGHT / 1500,
        )

    player = solipsist.get_rect()

    obstacle_class = Obstacle.generate_random_obstacle()
    obstacle = obstacle_class.get_rect()

    current_time = time()
    previousPointAwardedTime = current_time

    run = True
    while run:
        SCREEN.fill(j["graphic"]["BACKGROUND"][j["graphic"]["theme"]])
        MUSIC.play_random_music()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and game_status.gameover is False:
                game_status.clicks += 1
                j["stats"]["CLICKS"] += 1
                solipsist.jump()
                MUSIC.sound_jump()

        if player[1] < WINDOW_HEIGHT - player.height and game_status.gameover is False:
            solipsist.fall()
            obstacle_class.move()
            if obstacle.x < 0 - obstacle.width:  # If it left the screen
                # Regenerating obstacles
                obstacle_class = Obstacle.generate_random_obstacle()
                obstacle = obstacle_class.get_rect()

        # If player reached top, or bottom of window or touched obstacle
        if (
            player[1] >= WINDOW_HEIGHT - player.height
            or player[1] < 0
            or player.colliderect(obstacle)
        ):
            MUSIC.stop()
            MUSIC.sound_dead()
            pygame.display.flip()
            game_status.gameover = True
            game_status.is_game_started = False
            from widget_loops.gameover import (
                gameover,
            )  # Left it here, to avoid circular import

            gameover(game_status.time_played, game_status.clicks)

        solipsist.draw_it()
        obstacle_class.draw_it()
        MUSIC.make_description()
        pygame.display.flip()

        # Adds 1 second to time_played stats
        current_time = time()
        if (current_time - previousPointAwardedTime) >= 1:
            game_status.time_played += 1
            j["stats"]["TIME_PLAYED"] += 1
            previousPointAwardedTime = current_time
        save_json()
        clock.tick(j["game_settings"]["FPS"])
