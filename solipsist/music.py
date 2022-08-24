import pygame
import os
from random import choice

from solipsist.utils import debounce, resource_path
from solipsist.pygame_utils import Button
from solipsist.GSS import GameStatus
from solipsist.GSS import j
from solipsist.GSS import SCREEN
from solipsist.GSS import WINDOW_HEIGHT
from solipsist.GSS import WINDOW_WIDTH
from solipsist.GSS import get_language


class Music(GameStatus):
    def __init__(self) -> None:
        pass

    @classmethod
    def make_description(cls):
        _ = get_language()
        music_text = Button(
            f"{_['music.currently_playing']}: {cls.current_music_name.split('.')[0].replace(resource_path(j['music']['DEFAULT_MUSIC_FOLDER']), '')}",
            (int(WINDOW_WIDTH / 2.5), int(WINDOW_HEIGHT / 40)),
            (int(WINDOW_WIDTH / 40), int(WINDOW_WIDTH / 40)),
        )
        music_text.draw_it(SCREEN)

    @classmethod
    def pick_random_music(cls):
        all_music = []
        for music in os.listdir(resource_path(j["music"]["DEFAULT_MUSIC_FOLDER"])):
            all_music.append(music)
        random_music = (
            f"{resource_path(j['music']['DEFAULT_MUSIC_FOLDER'])}{choice(all_music)}"
        )
        return random_music

    @staticmethod
    def play_random_music():
        if GameStatus.is_music_playing == False:
            random_music_name = Music.pick_random_music()
            music = pygame.mixer.Sound(resource_path(random_music_name))
            music.set_volume(j["music"]["VOLUME"])
            music.play()

            GameStatus.is_music_playing = True
            GameStatus.current_music_name = random_music_name

    @classmethod
    def stop(cls):
        if cls.is_music_playing:
            pygame.mixer.stop()
            GameStatus.is_music_playing = False
            GameStatus.current_music_name = ""

    @debounce(0.1)
    def play(sound_name):
        sound = pygame.mixer.Sound(
            resource_path(
                os.path.join(
                    resource_path(j["music"]["DEFAULT_SOUND_FOLDER"]), sound_name
                )
            )
        )
        sound.set_volume(j["music"]["EFFECT_VOLUME"])
        sound.play()

    @classmethod
    def sound_dead(cls):
        cls.play("dead.mp3")

    @classmethod
    def sound_menu_click(cls):
        cls.play("menu_click.mp3")

    @classmethod
    def sound_jump(cls):
        cls.play("jump.mp3")

    @classmethod
    def sound_new_record(cls):
        cls.play("new_record.mp3")
