import pygame

import Cell
from GameConstants import SQUARE_SIZE as SIZE
import GameConstants
from Cell import CellType


def next_cell_valid(direction, game_board, pos):
    target_cell = game_board[0][0]
    col, row = pos
    if direction == GameConstants.DIR_UP:
        target_cell = game_board[row - 1][col]
    elif direction == GameConstants.DIR_RIGHT:
        target_cell = game_board[row][col + 1]
    elif direction == GameConstants.DIR_DOWN:
        target_cell = game_board[row + 1][col]
    elif direction == GameConstants.DIR_LEFT:
        target_cell = game_board[row][col - 1]
    return Cell.is_type(target_cell, CellType.FOOD, CellType.EMPTY, CellType.POWER_FOOD)


class Pacman:

    def __init__(self, loc):
        self.center_loc = [loc[0] * SIZE + SIZE / 2, loc[1] * SIZE + SIZE / 2]
        self.radius = SIZE / 3
        self.color = GameConstants.PAC_COLOR

        self.speed = GameConstants.PAC_SPEED

        # 1 - 4 Starting at Up going Clock wise
        self.direction = 0
        self.target_direction = 0

    def render(self, surface):
        pygame.draw.circle(surface, self.color, self.center_loc, self.radius)

    def tick(self, game_board):
        x_change = 0
        y_change = 0

        estimate_col = (self.center_loc[0] - SIZE / 2) / SIZE
        estimate_row = (self.center_loc [1] - SIZE / 2) / SIZE

        row, col = round(estimate_row), round(estimate_col)

        is_target_centered = False
        is_actual_centered = False

        if self.target_direction in GameConstants.VERT_DIRS:
            if estimate_col - 1.0 * int(estimate_col) == 0.:
                is_target_centered = True
        elif self.target_direction in GameConstants.HORIZ_DIRS:
            if estimate_row - 1.0 * int(estimate_row) == 0.:
                is_target_centered = True

        if self.direction in GameConstants.HORIZ_DIRS:
            if estimate_col - 1.0 * int(estimate_col) == 0.0:
                is_actual_centered = True
        elif self.direction in GameConstants.VERT_DIRS:
            if estimate_row - 1.0 * int(estimate_row) == 0.0:
                is_actual_centered = True

        if is_target_centered and next_cell_valid(self.target_direction, game_board, (col, row)):
            self.direction = self.target_direction

        if is_actual_centered and not next_cell_valid(self.direction, game_board, (col, row)):
            self.direction = 0

        if self.direction == 1 or self.direction == 3:
            y_change = self.speed * (self.direction - 2)
        elif self.direction == 2 or self.direction == 4:
            x_change = self.speed * (3 - self.direction)

        self.center_loc[0] += x_change
        self.center_loc[1] += y_change

    def set_direction(self, target_direction):
        self.target_direction = target_direction

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

