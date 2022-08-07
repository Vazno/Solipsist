import sys
import pygame

from GSS import SCREEN, FONT, BACKGROUND, FONT_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from main import main, MUSIC

def gameover():
	message = pygame.font.Font(FONT, int(WINDOW_WIDTH/20))
	run = True
	while run:
		SCREEN.fill(BACKGROUND)
		MUSIC.stop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				MUSIC.stop()
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False
				

		text = message.render("Gameover", True, FONT_COLOR)
		SCREEN.blit(text, (int(WINDOW_WIDTH/4), int(WINDOW_HEIGHT/3)))

		pygame.display.flip()

	main()