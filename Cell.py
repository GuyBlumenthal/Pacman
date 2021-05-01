import enum

import pygame
import enum
from main import SQUARE_SIZE as SIZE


class CellType(enum.Enum):
    EMPTY = 0
    WALL = 1
    FOOD = 2


class GameCell:

    def __init__(self, x, y, cell_type):
        self.x = x
        self.y = y

        self.cell_type = cell_type

    def draw(self, surface):
        if self.cell_type == CellType.WALL:
            pygame.draw.rect(surface, [255] * 3, (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.FOOD:
            pygame.draw.circle(surface, [255] * 3, (self.x * SIZE + SIZE / 2, self.y * SIZE + SIZE / 2), SIZE / 8)



