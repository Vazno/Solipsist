import pygame
from typing import Tuple
from GSS import WINDOW_WIDTH, j
from utils import resource_path

# Takes rectangle's size, position and a point. Returns true if that
# point is inside the rectangle and false if it isnt.
def pointInRectangle(px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False


class Button:
    def __init__(
        self, text: str, position: Tuple, size: Tuple = (200, 50), outline: bool = False
    ) -> None:
        self.position = position
        self.size = size

        self.button = pygame.Surface(size).convert()
        self.button.fill(j["graphic"]["BACKGROUND"][j["graphic"]["theme"]])
        self.outline = outline

        # Text is about 70% the height of the button
        font = pygame.font.Font(
            resource_path(j["graphic"]["FONT"]), int((70 / 100) * self.size[1])
        )
        self.font = font
        # First argument always requires a str, so f-string is used.
        self.textSurf = font.render(
            f"{text}", True, j["graphic"]["FONT_COLOR"][j["graphic"]["theme"]]
        )

    def clicked(self, events) -> None:
        mousePos = pygame.mouse.get_pos()
        if pointInRectangle(
            mousePos[0],
            mousePos[1],
            self.size[0],
            self.size[1],
            self.position[0],
            self.position[1],
        ):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False

    # Renders the button and text. Text position is calculated depending on position of button.
    # Also draws outline if self.outline is true
    def draw_it(self, display: pygame.display) -> None:
        # calculation to centre the text in button
        textx = (
            self.position[0]
            + (self.button.get_rect().width / 2)
            - (self.textSurf.get_rect().width / 2)
        )
        texty = (
            self.position[1]
            + (self.button.get_rect().height / 2)
            - (self.textSurf.get_rect().height / 2)
        )

        # display button first then text
        display.blit(self.button, (self.position[0], self.position[1]))
        display.blit(self.textSurf, (textx, texty))

        # draw outline
        if self.outline:
            thickness = 5
            posx = self.position[0] - thickness
            posy = self.position[1] - thickness
            sizex = self.size[0] + thickness * 2
            sizey = self.size[1] + thickness * 2

            pygame.draw.rect(
                display, (255, 0, 0), (posx, posy, sizex, sizey), thickness
            )

    def change_text(self, text):
        self.textSurf = self.font.render(
            f"{text}", True, j["graphic"]["FONT_COLOR"][j["graphic"]["theme"]]
        )


class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = j["graphic"]["InputBox"]["COLOR_INACTIVE"][j["graphic"]["theme"]]
        pygame.init()
        FONT = pygame.font.Font(
            resource_path(j["graphic"]["FONT"]), int(WINDOW_WIDTH / 40)
        )
        self.FONT = FONT
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (
                j["graphic"]["InputBox"]["COLOR_ACTIVE"][j["graphic"]["theme"]]
                if self.active
                else j["graphic"]["InputBox"]["COLOR_INACTIVE"][j["graphic"]["theme"]]
            )
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, False, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw_it(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
