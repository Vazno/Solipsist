'''Game status & game settings data handlers'''
import pygame
from dataclasses import dataclass
from utils import resource_path

SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)



@dataclass
class GameSettings():
	# Settings ######################
	FPS: int = 75
	OBSTACLE_DEFAULT_VEL: int = -20 # It should be negative (Goes from right to left)
	#################################


	# Graphic Settings ##############
	GAME_NAME: str = "Solipsist"
	FONT = resource_path("Quinquefive-0Wonv.ttf")
	FONT_COLOR = [255, 255, 255]
	PLAYER_COLOR = [255, 255, 255]
	BACKGROUND = [0, 0, 0]
	OBSTACLE_COLOR = [255, 255, 255]
	#################################


	# Music #########################
	DEFAULT_MUSIC_FOLDER = resource_path("sounds/music/")
	DEFAULT_SOUND_FOLDER = resource_path("sounds/sounds/")
	#################################


	# Mechanics, changing it, won't give any effect #
	WINDOW_WIDTH: int = 0
	WINDOW_HEIGHT: int = 0
	#################################################
@dataclass
class GameStatus:
	is_game_started: bool = False
	gameover: bool = False
	is_music_playing: bool = False
	current_music_name: str = ""
	clicks: int = 0
