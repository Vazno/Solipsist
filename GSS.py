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


OBSTACLE_DEFAULT_VEL = j["game_settings"]["OBSTACLE_DEFAULT_VEL"]
if OBSTACLE_DEFAULT_VEL == 0:
	OBSTACLE_DEFAULT_VEL = -WINDOW_WIDTH/100


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