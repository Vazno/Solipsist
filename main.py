import pygame
import os
import random
from random import randint
from random import choice
from dataclasses import dataclass

from utils import resource_path


@dataclass
class GameSettings():
	#### Mechanics, changing it, won't give any effect ##########
	WINDOW_WIDTH: int = 0
	WINDOW_HEIGHT: int = 0
	screen = None
	#############################################################

	FPS: int = 75
	GAME_NAME: str = "Solipsist"
	FONT = resource_path("Quinquefive-0Wonv.ttf")
	DEFAULT_MUSIC_FOLDER = "sounds/music/"
	DEFAULT_SOUND_FOLDER = "sounds/sounds/"
	OBSTACLE_DEFAULT_VEL: int = -20 # It should be negative (Goes from right to left)



	############# RGB ###############
	PLAYER_COLOR = [255, 255, 255]
	BACKGROUND = [0, 0, 0]
	OBSTACLE_COLOR = [255, 255, 255]
	#################################

@dataclass
class GameStatus:
	is_game_started: bool = False
	gameover: bool = False
	is_music_playing: bool = False
	current_music_name: str = ""
	clicks: int = 0


class Solipsist(GameSettings):
	'''The main character's class.'''
	
	def __init__(self, screen, left, top, size: int, grav: int, color=None) -> None:
		super().__init__()
		player = pygame.Rect(left, top, size, size)
		self.functional_grav = 0
		self.screen = screen
		self.size = size
		self.player = player
		self.grav = grav
		self.SCREEN_HEIGHT = screen.get_height()
		if not color:
			self.color = self.PLAYER_COLOR

	def get_rect(self):
		return self.player

	def draw_it(self):
		pygame.draw.rect(self.screen, self.color, self.player)

	def fall(self):
		self.player.y += self.functional_grav
		self.functional_grav += self.grav

	def jump(self):
		self.functional_grav = -self.grav*24


class Obstacle(GameSettings):
	'''Class for obstacles.'''
	def __init__(self, screen, left, top, width, height, speed: int, color=None) -> None:
		super().OBSTACLE_COLOR
		obstacle = pygame.Rect(left, top, width, height)
		self.functional_grav = 0
		self.screen = screen
		self.obstacle = obstacle
		self.speed = speed
		self.SCREEN_HEIGHT = screen.get_height()
		if not color:
			self.color = self.OBSTACLE_COLOR

	def get_rect(self):
		return self.obstacle

	def draw_it(self):
		pygame.draw.rect(self.screen, self.color, self.obstacle)

	def move(self, num: int = None):
		if num == None:
			num = self.OBSTACLE_DEFAULT_VEL
		self.obstacle.x += num

	@classmethod
	def generate_random_obstacle(cls):
		'''Generates obstacles going from the right of the screen'''
		obstacle_class = Obstacle(cls.screen,
		randint(cls.WINDOW_WIDTH, cls.WINDOW_WIDTH+cls.WINDOW_WIDTH/10),
		cls.WINDOW_HEIGHT/random.randint(2, 10),
		cls.WINDOW_WIDTH/random.randint(20, 30),
		cls.WINDOW_HEIGHT/random.randint(2, 10),
		cls.OBSTACLE_DEFAULT_VEL)
		return obstacle_class


class Music(GameStatus, GameSettings):
	def __init__(self, music_folder: str = None) -> None:
		if not music_folder:
			self.DEFAULT_MUSIC_FOLDER = self.music_folder
		super().__init__()

	@classmethod
	def make_description(cls):
		_font = pygame.font.Font(cls.FONT, int(cls.WINDOW_WIDTH/100))
		music_text = _font.render(f"Currently playing: {cls.current_music_name.split('.')[0].replace(cls.DEFAULT_MUSIC_FOLDER, '')}",True, (255,255,255))
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


def main():
	pygame.init()
	screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
	GameSettings.screen = screen
	pygame.display.set_caption(GameSettings.GAME_NAME)
	GameSettings.WINDOW_HEIGHT = screen.get_height()
	GameSettings.WINDOW_WIDTH = screen.get_width()

	clock = pygame.time.Clock()
	game_status = GameStatus(is_game_started=False, gameover=False)

	solipsist = Solipsist(screen, int(GameSettings.WINDOW_WIDTH/3), int(GameSettings.WINDOW_HEIGHT/4), int(GameSettings.WINDOW_HEIGHT/15), 0.5)
	player = solipsist.get_rect()

	obstacle_class = Obstacle.generate_random_obstacle()
	obstacle = obstacle_class.get_rect()


	run = True
	while run:
		screen.fill(GameSettings.BACKGROUND)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN and game_status.gameover is False:
				Music.play_random_music()
				solipsist.jump()
				game_status.is_game_started = True


			if event.type == pygame.MOUSEBUTTONDOWN and game_status.gameover is True:
				run = False
				main()

					

		if player[1] < GameSettings.WINDOW_HEIGHT - player.height and game_status.is_game_started is True and game_status.gameover is False:
			solipsist.fall()
			obstacle_class.move()
			if obstacle.x < 0 - obstacle.width: # If it left the screen
				# Regenerating obstacles
				obstacle_class = Obstacle.generate_random_obstacle()
				obstacle = obstacle_class.get_rect()
	
		# If player reached top, or bottom of window
		if player[1] >= GameSettings.WINDOW_HEIGHT-player.height or player[1] < 0 or player.colliderect(obstacle):
			
			message = pygame.font.Font("Quinquefive-0Wonv.ttf", int(GameSettings.WINDOW_WIDTH/20))
			text = message.render("Gameover", True, (255,255,255), (0,0,0))
			screen.blit(text, (int(GameSettings.WINDOW_WIDTH/4), int(GameSettings.WINDOW_HEIGHT/3)))

			Music.stop()
			if game_status.gameover is False:
				x = pygame.mixer.Sound(GameSettings.DEFAULT_SOUND_FOLDER + "woosh.mp3")
				x.play()
			game_status.gameover = True
			game_status.is_game_started = False


		solipsist.draw_it()
		obstacle_class.draw_it()
		Music.make_description()
		pygame.display.flip()
		clock.tick(GameSettings.FPS)

if __name__ == "__main__":
	main()