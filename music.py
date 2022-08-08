import pygame
import os
from random import choice

from utils import resource_path
from GSS import GameStatus
from GSS import SCREEN
from GSS import FONT
from GSS import FONT_COLOR
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH
from GSS import DEFAULT_MUSIC_FOLDER
from GSS import DEFAULT_SOUND_FOLDER



class Music(GameStatus):
	def __init__(self, music_folder: str = None) -> None:
		if music_folder != None:
			DEFAULT_MUSIC_FOLDER = self.music_folder

	@classmethod
	def make_description(cls):
		_font = pygame.font.Font(FONT, int(WINDOW_WIDTH/60))
		music_text = _font.render(f"Currently playing: {cls.current_music_name.split('.')[0].replace(DEFAULT_MUSIC_FOLDER, '')}",True, FONT_COLOR)
		SCREEN.blit(music_text, (int(WINDOW_WIDTH/8), int(WINDOW_HEIGHT/40)))

	@classmethod
	def pick_random_music(cls):
		all_music = []
		for music in os.listdir(DEFAULT_MUSIC_FOLDER):
			all_music.append(music)
		random_music = f"{DEFAULT_MUSIC_FOLDER}{choice(all_music)}"
		return random_music

	@staticmethod
	def play_random_music():
		if GameStatus.is_music_playing == False:
			random_music_name = Music.pick_random_music()
			music = pygame.mixer.Sound(resource_path(random_music_name))
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
	def sound_dead():
		sound = pygame.mixer.Sound(resource_path(os.path.join(DEFAULT_SOUND_FOLDER, "dead.mp3")))
		sound.play()

	@staticmethod
	def sound_menu_click():
		sound = pygame.mixer.Sound(resource_path(os.path.join(DEFAULT_SOUND_FOLDER, "menu_click.mp3")))
		sound.play()

	@staticmethod
	def sound_jump():
		sound = pygame.mixer.Sound(resource_path(os.path.join(DEFAULT_SOUND_FOLDER, "jump.mp3")))
		sound.play()