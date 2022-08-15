"""Game status & game settings data handlers"""
import os
import pygame
import json
import yaml
from dataclasses import dataclass
from pathlib import Path

try:
    from platformdirs import user_data_dir
except ModuleNotFoundError:
    print("### pip install platformdirs ###")

from utils import resource_path

GAME_NAME = "Solipsist"


def create_user_data():
    data_folder = Path(os.path.join(user_data_dir(), GAME_NAME))
    data_folder.mkdir(exist_ok=True)
    with open(resource_path("settings.json"), "r") as old_json:
        json_to_save = json.load(old_json)

    with open(os.path.join(data_folder, "settings.json"), "w") as new_json_file:
        json.dump(json_to_save, new_json_file, indent=4)

    with open(os.path.join(data_folder, "settings.json"), "r") as new_json_file:
        j = json.load(new_json_file)


try:
    with open(
        os.path.join(os.path.join(user_data_dir(), GAME_NAME), "settings.json")
    ) as f:
        j = json.load(f)
except FileNotFoundError:
    create_user_data()
    with open(
        os.path.join(os.path.join(user_data_dir(), GAME_NAME), "settings.json")
    ) as f:
        j = json.load(f)


def get_language():
    languages = os.listdir("translations/")
    with open(f"translations\\{languages[j['language']]}", "r") as f:
        _ = yaml.safe_load(f)
        return _


if j["graphic"]["FULL_SCREEN"]:
    try:
        SCREEN = pygame.display.set_mode(
            j["graphic"]["resolution"], flags=pygame.FULLSCREEN
        )
    except pygame.error:
        create_user_data()
        SCREEN = pygame.display.set_mode(
            j["graphic"]["resolution"], flags=pygame.FULLSCREEN
        )
else:
    try:
        SCREEN = pygame.display.set_mode(j["graphic"]["resolution"])
    except pygame.error:
        create_user_data()
        SCREEN = pygame.display.set_mode(j["graphic"]["resolution"])

WINDOW_HEIGHT = SCREEN.get_height()
WINDOW_WIDTH = SCREEN.get_width()


OBSTACLE_DEFAULT_VEL = j["game_settings"]["OBSTACLE_DEFAULT_VEL"]
if OBSTACLE_DEFAULT_VEL == 0:
    OBSTACLE_DEFAULT_VEL = -WINDOW_WIDTH / 100


@dataclass
class GameStatus:
    is_game_started: bool = False
    gameover: bool = False
    is_music_playing: bool = False
    current_music_name: str = ""
    time_played: int = 0
    clicks: int = 0


def save_json():
    data_folder = Path(os.path.join(user_data_dir(), GAME_NAME))
    with open(os.path.join(data_folder, "settings.json"), "w") as f:
        json.dump(j, f, indent=4)
