import pygame
from GameConstants import SQUARE_SIZE as SIZE
import GameConstants


class Pacman:

    def __init__(self, loc):
        self.center_loc = [loc[0] * SIZE + SIZE / 2, loc[1] * SIZE + SIZE / 2]
        self.radius = SIZE / 3
        self.color = GameConstants.PAC_COLOR

        self.speed = GameConstants.PAC_SPEED

        # 1 - 4 Starting at Up going Clock wise
        self.direction = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center_loc, self.radius)

    def tick(self):
        x_change = 0
        y_change = 0

        if self.direction == 1 or self.direction == 3:
            y_change = self.speed * (self.direction - 2)
        elif self.direction == 2 or self.direction == 4:
            x_change = self.speed * (3 - self.direction)

        self.center_loc[0] += x_change
        self.center_loc[1] += y_change

    def set_direction(self, target_direction):
        self.direction = target_direction

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key in GameConstants.UP_KEYS:
                self.set_direction(1)
            elif event.key in GameConstants.RIGHT_KEYS:
                self.set_direction(2)
            elif event.key in GameConstants.DOWN_KEYS:
                self.set_direction(3)
            elif event.key in GameConstants.LEFT_KEYS:
                self.set_direction(4)

