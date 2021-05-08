import enum

import pygame

import GameConstants
from GameConstants import SQUARE_SIZE as SIZE
import CellType


def is_type(target_cell, *cell_types):
    for cell_type in cell_types:
        if target_cell.cell_type == cell_type:
            return True
    return False


class GameCell:

    def __init__(self, x, y, cell_type):
        self.x = x
        self.y = y

        self.cell_type = cell_type

    def render(self, surface):
        if self.cell_type == CellType.WALL:
            pygame.draw.rect(surface, [255] * 3,
                             (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.FOOD:
            pygame.draw.circle(surface, [255] * 3,
                               (self.x * SIZE + SIZE / 2, self.y * SIZE + SIZE / 2),
                               GameConstants.FOOD_RADIUS)
        elif self.cell_type == CellType.EMPTY:
            pygame.draw.rect(surface, [0] * 3,
                             (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.GHOST_CAGE_WALL:
            pygame.draw.rect(surface, GameConstants.GHOST_WALL_COLOR,
                             (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.GHOST_CAGE_INNER:
            pygame.draw.rect(surface, GameConstants.GHOST_INNER_COLOR,
                             (self.x * SIZE, self.y * SIZE, SIZE, SIZE))
        elif self.cell_type == CellType.POWER_FOOD:
            pygame.draw.circle(surface, [255, 255, 191],
                               (self.x * SIZE + SIZE / 2, self.y * SIZE + SIZE / 2),
                               GameConstants.POWER_FOOD_RADIUS)

    def is_touching_food(self, center_loc, radius):
        center_x, center_y = self.x * SIZE + SIZE / 2, self.y * SIZE + SIZE / 2
        distance = pow(pow(center_x - center_loc[0], 2) + pow(center_y - center_loc[1], 2), 0.5)
        if self.cell_type == CellType.FOOD:
            return distance <= GameConstants.FOOD_RADIUS + radius
        if self.cell_type == CellType.POWER_FOOD:
            return distance <= GameConstants.POWER_FOOD_RADIUS + radius
        else:
            return False

    def eat(self):
        if self.cell_type == CellType.FOOD:
            self.cell_type = CellType.EMPTY
            return 100, False
        elif self.cell_type == CellType.POWER_FOOD:
            self.cell_type = CellType.EMPTY
            return 500, True
        return 0, False



