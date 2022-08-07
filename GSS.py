'''Game status & game settings data handlers'''
import pygame
import json
from dataclasses import dataclass
from utils import resource_path


SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)



WINDOW_HEIGHT = SCREEN.get_height()
WINDOW_WIDTH = SCREEN.get_width()

with open(resource_path("settings.json")) as f:
	j = json.load(f)

video = j["video"]
FPS = video["FPS"]
OBSTACLE_DEFAULT_VEL = video["OBSTACLE_DEFAULT_VEL"]


graphic = j["graphic"]
GAME_NAME = graphic["GAME_NAME"]
FONT = graphic["FONT"]
FONT_COLOR = graphic["FONT_COLOR"]
PLAYER_COLOR = graphic["PLAYER_COLOR"]
BACKGROUND = graphic["BACKGROUND"]
OBSTACLE_COLOR = graphic["OBSTACLE_COLOR"]


music = j["music"]
VOLUME = music["VOLUME"]
DEFAULT_MUSIC_FOLDER = resource_path(music["DEFAULT_MUSIC_FOLDER"])
DEFAULT_SOUND_FOLDER = resource_path(music["DEFAULT_SOUND_FOLDER"])


stats = j["stats"]
CLICKS = stats["CLICKS"]
TIME_PLAYED = stats["TIME_PLAYED"]


@dataclass
class GameStatus:
	is_game_started: bool = False
	gameover: bool = False
	is_music_playing: bool = False
	current_music_name: str = ""


def save_json():
	with open(resource_path("settings.json"), "w") as f:
		json.dump(j, f, indent=4)