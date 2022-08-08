'''Game status & game settings data handlers'''
import pygame
import json
from dataclasses import dataclass
from utils import resource_path

with open(resource_path("settings.json")) as f:
	j = json.load(f)

if j["graphic"]["FULL_SCREEN"]:
	SCREEN = pygame.display.set_mode(j["graphic"]["resolution"], flags=pygame.FULLSCREEN)
else:
	SCREEN = pygame.display.set_mode(j["graphic"]["resolution"])



WINDOW_HEIGHT = SCREEN.get_height()
WINDOW_WIDTH = SCREEN.get_width()



DESCRIPTION = j["DESCRIPTION"]

game_settings = j["game_settings"]
FPS = game_settings["FPS"]
OBSTACLE_DEFAULT_VEL = game_settings["OBSTACLE_DEFAULT_VEL"]


graphic = j["graphic"]
GAME_NAME = graphic["GAME_NAME"]
resolution = graphic["resolution"]
FULL_SCREEN = graphic["FULL_SCREEN"]
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
	time_played: int = 0
	clicks: int = 0


def save_json():
	with open(resource_path("settings.json"), "w") as f:
		json.dump(j, f, indent=4)