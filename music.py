import pygame
import os
from random import choice

from utils import resource_path
from GSS import GameSettings, GameStatus

class Music(GameStatus, GameSettings):
	def __init__(self, music_folder: str = None) -> None:
		if music_folder != None:
			self.DEFAULT_MUSIC_FOLDER = self.music_folder
		super().__init__()

	@classmethod
	def make_description(cls):
		_font = pygame.font.Font(cls.FONT, int(cls.WINDOW_WIDTH/100))
		music_text = _font.render(f"Currently playing: {cls.current_music_name.split('.')[0].replace(cls.DEFAULT_MUSIC_FOLDER, '')}",True, GameSettings.FONT_COLOR)
		cls.screen.blit(music_text, (int(cls.WINDOW_WIDTH/8), int(cls.WINDOW_HEIGHT/40)))

	@classmethod
	def pick_random_music(cls):
		all_music = []
		for music in os.listdir(cls.DEFAULT_MUSIC_FOLDER):
			all_music.append(music)
		random_music = f"{cls.DEFAULT_MUSIC_FOLDER}{choice(all_music)}"
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