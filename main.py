import pygame
import random
import sys
from random import randint

from GSS import GameSettings, GameStatus, SCREEN
from music import Music

MUSIC =  Music()


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


def main():
	pygame.init()
	
	GameSettings.screen = SCREEN
	pygame.display.set_caption(GameSettings.GAME_NAME)
	GameSettings.WINDOW_HEIGHT = SCREEN.get_height()
	GameSettings.WINDOW_WIDTH = SCREEN.get_width()



	clock = pygame.time.Clock()
	game_status = GameStatus(is_game_started=False, gameover=False)

	solipsist = Solipsist(SCREEN, int(GameSettings.WINDOW_WIDTH/3), int(GameSettings.WINDOW_HEIGHT/4), int(GameSettings.WINDOW_HEIGHT/15), 0.5)
	player = solipsist.get_rect()

	obstacle_class = Obstacle.generate_random_obstacle()
	obstacle = obstacle_class.get_rect()


	run = True
	while run:
		SCREEN.fill(GameSettings.BACKGROUND)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN and game_status.gameover is False:
				MUSIC.play_random_music()
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
		if player[1] >= GameSettings.WINDOW_HEIGHT-player.height or player[1] < 0 or player.colliderect(obstacle) and game_status.gameover is False:
			MUSIC.stop()
			if game_status.gameover is False:
				x = pygame.mixer.Sound(GameSettings.DEFAULT_SOUND_FOLDER + "woosh.mp3")
				x.play()
			game_status.gameover = True
			game_status.is_game_started = False
			from gameover import gameover
			gameover()


		solipsist.draw_it()
		obstacle_class.draw_it()
		MUSIC.make_description()
		pygame.display.flip()
		clock.tick(GameSettings.FPS)

if __name__ == "__main__":
	main()