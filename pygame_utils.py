import pygame
from typing import Tuple
from GSS import FONT, FONT_COLOR, BACKGROUND

#Takes rectangle's size, position and a point. Returns true if that
#point is inside the rectangle and false if it isnt.
def pointInRectangle(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False

class Button:
    def __init__(self, text:str, position:Tuple, size:Tuple=(200, 50), outline:bool=True)->None:
        self.position = position
        self.size = size

        self.button = pygame.Surface(size).convert()
        self.button.fill(BACKGROUND)
        self.outline = outline

        #Text is about 70% the height of the button
        font = pygame.font.Font(FONT, int((70/100)*self.size[1]))

        #First argument always requires a str, so f-string is used.
        self.textSurf = font.render(f"{text}", True, FONT_COLOR)

    def clicked(self, events)->None:
        mousePos = pygame.mouse.get_pos()
        if pointInRectangle(mousePos[0], mousePos[1], self.size[0], self.size[1], self.position[0], self.position[1]):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False

    #Renders the button and text. Text position is calculated depending on position of button.
    #Also draws outline if self.outline is true
    def draw_it(self, display:pygame.display) -> None:
        #calculation to centre the text in button
        textx = self.position[0] + (self.button.get_rect().width/2) - (self.textSurf.get_rect().width/2)
        texty = self.position[1] + (self.button.get_rect().height/2) - (self.textSurf.get_rect().height/2)

        #display button first then text
        display.blit(self.button, (self.position[0], self.position[1]))
        display.blit(self.textSurf, (textx, texty))
        
        #draw outline
        if self.outline:
            thickness = 5
            posx = self.position[0] - thickness
            posy = self.position[1] - thickness
            sizex = self.size[0] + thickness * 2
            sizey = self.size[1] + thickness * 2

            pygame.draw.rect(display, (255, 0, 0), (posx, posy, sizex, sizey), thickness)
