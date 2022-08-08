import sys
import pygame
from game import MUSIC
from main import main_menu

from pygame_utils import Button
from GSS import BACKGROUND, SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, SCREEN
from GSS import j

def about():
	go_back_button = Button("Go back", (WINDOW_WIDTH/2.2, WINDOW_HEIGHT/1.5), (WINDOW_WIDTH/15, WINDOW_HEIGHT/15), False)
	description_button = Button(j['DESCRIPTION'], (WINDOW_WIDTH/2.2, WINDOW_HEIGHT/2), (WINDOW_WIDTH/15, WINDOW_HEIGHT/15), False)
	run = True
	while run:
		SCREEN.fill(BACKGROUND)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				run = False
				sys.exit()
		
		if go_back_button.clicked(events):
			MUSIC.sound_menu_click()
			main_menu()
		description_button.draw_it(SCREEN)
		go_back_button.draw_it(SCREEN)
		pygame.display.flip()