import enum

import pygame
import enum
from GameConstants import SQUARE_SIZE as SIZE


class CellType(enum.Enum):
    EMPTY = 0
    WALL = 1
    FOOD = 2
    GHOST_CAGE_WALL = 3
    GHOST_CAGE_INNER = 4
    POWER_FOOD = 5


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
        elif self.cell_type == CellType.EMPTY:
            pygame.draw.rect(surface, [0] * 3, (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.GHOST_CAGE_WALL:
            pygame.draw.rect(surface, [133, 117, 163], (self.x * SIZE + 1, self.y * SIZE + 1, SIZE - 2, SIZE - 2))
        elif self.cell_type == CellType.GHOST_CAGE_INNER:
            pygame.draw.rect(surface, [45, 29, 51], (self.x * SIZE, self.y * SIZE, SIZE, SIZE))
        elif self.cell_type == CellType.POWER_FOOD:
            pygame.draw.circle(surface, [255, 255, 191], (self.x * SIZE + SIZE / 2, self.y * SIZE + SIZE / 2), SIZE / 4)




