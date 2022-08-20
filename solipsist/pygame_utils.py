import pygame
import random
from abc import ABC, abstractmethod
from typing import Tuple

from utils import resource_path
from GSS import j
from GSS import OBSTACLE_DEFAULT_VEL
from GSS import SCREEN
from GSS import WINDOW_HEIGHT
from GSS import WINDOW_WIDTH


class ScreenObject(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def draw_it():
        pass


# Takes rectangle's size, position and a point. Returns true if that
# point is inside the rectangle and false if it isnt.
def pointInRectangle(px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False


class Button(ScreenObject):
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
        super().__init__()

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


class InputBox(ScreenObject):
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
        super().__init__()

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


class Solipsist(ScreenObject):
    """The main character's class."""

    def __init__(self, screen, left, top, size: int, grav: int, color=None) -> None:
        player = pygame.Rect(left, top, size, size)
        self.functional_grav = 0
        self.screen = screen
        self.size = size
        self.player = player
        self.grav = grav
        self.SCREEN_HEIGHT = screen.get_height()
        if not color:
            self.color = j["graphic"]["PLAYER_COLOR"][j["graphic"]["theme"]]
        super().__init__()

    def get_rect(self):
        return self.player

    def draw_it(self):
        pygame.draw.rect(self.screen, self.color, self.player)

    def fall(self):
        self.player.y += self.functional_grav
        self.functional_grav += self.grav

    def jump(self):
        self.functional_grav = -self.grav * 24


class Obstacle(ScreenObject):
    """Class for obstacles."""

    def __init__(
        self, screen, left, top, width, height, speed: int, color=None
    ) -> None:
        obstacle = pygame.Rect(left, top, width, height)
        self.functional_grav = 0
        self.screen = screen
        self.obstacle = obstacle
        self.speed = speed
        self.SCREEN_HEIGHT = screen.get_height()
        if not color:
            self.color = j["graphic"]["OBSTACLE_COLOR"][j["graphic"]["theme"]]
        super().__init__()

    def get_rect(self):
        return self.obstacle

    def draw_it(self):
        pygame.draw.rect(self.screen, self.color, self.obstacle)

    def move(self, num: int = None):
        if num is None:
            num = OBSTACLE_DEFAULT_VEL
        self.obstacle.x += num

    @staticmethod
    def generate_random_obstacle():
        """Generates obstacles going from the right of the screen"""
        obstacle_class = Obstacle(
            SCREEN,
            random.randint(WINDOW_WIDTH, int(WINDOW_WIDTH + WINDOW_WIDTH / 10)),
            WINDOW_HEIGHT / random.randint(2, 10),
            WINDOW_WIDTH / random.randint(30, 40),
            WINDOW_HEIGHT / random.randint(2, 10),
            OBSTACLE_DEFAULT_VEL,
        )
        return obstacle_class
