import pygame
import os
from random import choice

from utils import debounce, resource_path
from GSS import GameStatus
from GSS import j
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH


class Music(GameStatus):
    def __init__(self, music_folder: str = None) -> None:
        if music_folder != None:
            DEFAULT_MUSIC_FOLDER = self.music_folder

    @classmethod
    def make_description(cls):
        _font = pygame.font.Font(resource_path(j["graphic"]["FONT"]), int(WINDOW_WIDTH / 60))
        music_text = _font.render(
            f"Currently playing: {cls.current_music_name.split('.')[0].replace(resource_path(j['music']['DEFAULT_MUSIC_FOLDER']), '')}",
            True,
            j["graphic"]["FONT_COLOR"],
        )
        SCREEN.blit(music_text, (int(WINDOW_WIDTH / 8), int(WINDOW_HEIGHT / 40)))

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

    @staticmethod
    @debounce(0.1)
    def sound_dead():
        sound = pygame.mixer.Sound(
            resource_path(
                os.path.join(
                    resource_path(j["music"]["DEFAULT_SOUND_FOLDER"]), "dead.mp3"
                )
            )
        )
        sound.play()

    @staticmethod
    @debounce(0.1)
    def sound_menu_click():
        sound = pygame.mixer.Sound(
            resource_path(
                os.path.join(
                    resource_path(j["music"]["DEFAULT_SOUND_FOLDER"]), "menu_click.mp3"
                )
            )
        )
        sound.play()

    @staticmethod
    @debounce(0.1)
    def sound_jump():
        sound = pygame.mixer.Sound(
            resource_path(
                os.path.join(
                    resource_path(j["music"]["DEFAULT_SOUND_FOLDER"]), "jump.mp3"
                )
            )
        )
        sound.play()

    @staticmethod
    @debounce(0.1)
    def sound_new_record():
        sound = pygame.mixer.Sound(
            resource_path(
                os.path.join(
                    resource_path(j["music"]["DEFAULT_SOUND_FOLDER"]), "new_record.mp3"
                )
            )
        )
        sound.play()
