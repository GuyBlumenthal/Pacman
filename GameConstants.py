import pygame

FPS = 60

SQUARE_SIZE = 20

UP_KEYS = (pygame.K_w, pygame.K_UP)
RIGHT_KEYS = (pygame.K_d, pygame.K_RIGHT)
DOWN_KEYS = (pygame.K_s, pygame.K_DOWN)
LEFT_KEYS = (pygame.K_a, pygame.K_LEFT)

# Pacman directions
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

VERT_DIRS = [DIR_UP, DIR_DOWN]
HORIZ_DIRS = [DIR_RIGHT, DIR_LEFT]

PAC_SPEED = 1
PAC_COLOR = (255, 255, 0)

GHOST_WALL_COLOR = (133, 117, 163)
GHOST_INNER_COLOR = (45, 29, 51)
