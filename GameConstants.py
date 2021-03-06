import pygame
import CellType

LAYOUT_PATH = "layout.txt"

FPS = 60

SQUARE_SIZE = 20

UP_KEYS = (pygame.K_w, pygame.K_UP)
RIGHT_KEYS = (pygame.K_d, pygame.K_RIGHT)
DOWN_KEYS = (pygame.K_s, pygame.K_DOWN)
LEFT_KEYS = (pygame.K_a, pygame.K_LEFT)

FOOD_RADIUS = SQUARE_SIZE / 8
POWER_FOOD_RADIUS = SQUARE_SIZE / 4

MAX_MAP_SCORE = 10000

# Pacman directions
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_NONE = 0

VERT_DIRS = [DIR_UP, DIR_DOWN]
HORIZ_DIRS = [DIR_RIGHT, DIR_LEFT]

PASSABLE_CELLS = [
    CellType.EMPTY,
    CellType.FOOD,
    CellType.POWER_FOOD,
    CellType.GHOST_CAGE_INNER,
    CellType.TUNNEL
]

SOLID_CELLS = [
    CellType.GHOST_CAGE_WALL,
    CellType.WALL
]

PAC_SPEED = 1
PAC_COLOR = (255, 255, 0)

GHOST_WALL_COLOR = (133, 117, 163)
GHOST_INNER_COLOR = (0, 0, 0)

PACMAN_OPEN = 'animation/pacman_open.png'
PACMAN_CLOSED = 'animation/pacman_closed.png'

GHOST_PURPLE = 'animation/ghost_purple.png'
GHOST_RED = 'animation/ghost_red.png'
GHOST_GREEN = 'animation/ghost_green.png'
GHOST_BLUE = 'animation/ghost_light_blue.png'

GHOST_SPEED = 1
GHOST_HOME_WIDTH = 2

GHOST_ACTIVATION_TIME = 5000
