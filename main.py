import pygame
import random
import sys
from random import randint
from time import time


from GSS import GameStatus
from GSS import save_json
from GSS import GAME_NAME
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH
from GSS import OBSTACLE_COLOR
from GSS import PLAYER_COLOR
from GSS import OBSTACLE_DEFAULT_VEL
from GSS import BACKGROUND
from GSS import DEFAULT_SOUND_FOLDER
from GSS import FPS
from GSS import j

from music import Music

MUSIC =  Music()


class Solipsist():
	'''The main character's class.'''
	
	def __init__(self, screen, left, top, size: int, grav: int, color=None) -> None:
		player = pygame.Rect(left, top, size, size)
		self.functional_grav = 0
		self.screen = screen
		self.size = size
		self.player = player
		self.grav = grav
		self.SCREEN_HEIGHT = screen.get_height()
		if not color:
			self.color = PLAYER_COLOR

	def get_rect(self):
		return self.player

	def draw_it(self):
		pygame.draw.rect(self.screen, self.color, self.player)

	def fall(self):
		self.player.y += self.functional_grav
		self.functional_grav += self.grav

	def jump(self):
		
		self.functional_grav = -self.grav*24


class Obstacle():
	'''Class for obstacles.'''
	def __init__(self, screen, left, top, width, height, speed: int, color=None) -> None:
		obstacle = pygame.Rect(left, top, width, height)
		self.functional_grav = 0
		self.screen = screen
		self.obstacle = obstacle
		self.speed = speed
		self.SCREEN_HEIGHT = screen.get_height()
		if not color:
			self.color = OBSTACLE_COLOR

	def get_rect(self):
		return self.obstacle

	def draw_it(self):
		pygame.draw.rect(self.screen, self.color, self.obstacle)

	def move(self, num: int = None):
		if num == None:
			num = OBSTACLE_DEFAULT_VEL
		self.obstacle.x += num

	@staticmethod
	def generate_random_obstacle():
		'''Generates obstacles going from the right of the screen'''
		obstacle_class = Obstacle(SCREEN,
		randint(WINDOW_WIDTH, WINDOW_WIDTH+WINDOW_WIDTH/10),
		WINDOW_HEIGHT/random.randint(2, 10),
		WINDOW_WIDTH/random.randint(20, 30),
		WINDOW_HEIGHT/random.randint(2, 10),
		OBSTACLE_DEFAULT_VEL)
		return obstacle_class


def main():
	pygame.init()
	pygame.display.set_caption(GAME_NAME)




	clock = pygame.time.Clock()
	game_status = GameStatus(is_game_started=False, gameover=False)

	solipsist = Solipsist(SCREEN, int(WINDOW_WIDTH/3), int(WINDOW_HEIGHT/4), int(WINDOW_HEIGHT/15), 0.5)
	player = solipsist.get_rect()

	obstacle_class = Obstacle.generate_random_obstacle()
	obstacle = obstacle_class.get_rect()


	current_time = time()
	previousPointAwardedTime = current_time
	run = True
	while run:
		SCREEN.fill(BACKGROUND)
		MUSIC.play_random_music()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN and game_status.gameover is False:
				j["stats"]["CLICKS"] += 1
				solipsist.jump()



		if player[1] < WINDOW_HEIGHT - player.height and game_status.gameover is False:
			solipsist.fall()
			obstacle_class.move()
			if obstacle.x < 0 - obstacle.width: # If it left the screen
				# Regenerating obstacles
				obstacle_class = Obstacle.generate_random_obstacle()
				obstacle = obstacle_class.get_rect()
	
		# If player reached top, or bottom of window
		if player[1] >= WINDOW_HEIGHT-player.height or player[1] < 0 or player.colliderect(obstacle):
			MUSIC.stop()
			MUSIC.sound_woosh()
			game_status.gameover = True
			game_status.is_game_started = False
			from gameover import gameover # Left it here, to avoid circular import
			gameover()


		solipsist.draw_it()
		obstacle_class.draw_it()
		MUSIC.make_description()
		pygame.display.flip()

		# Adds 1 second to time_played stats
		current_time = time()
		if (current_time - previousPointAwardedTime) >= 1:
			j["stats"]["TIME_PLAYED"] += 1
			previousPointAwardedTime = current_time
		save_json()
		clock.tick(FPS)
		

if __name__ == "__main__":
	main()