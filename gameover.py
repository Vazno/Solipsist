import sys
import pygame

from GSS import GameSettings, SCREEN
from main import main, MUSIC

def gameover():
	message = pygame.font.Font(GameSettings.FONT, int(GameSettings.WINDOW_WIDTH/20))
	run = True
	while run:
		SCREEN.fill(GameSettings.BACKGROUND)
		MUSIC.stop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				MUSIC.stop()
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False
				

		text = message.render("Gameover", True, GameSettings.FONT_COLOR)
		SCREEN.blit(text, (int(GameSettings.WINDOW_WIDTH/4), int(GameSettings.WINDOW_HEIGHT/3)))

		pygame.display.flip()

	main()