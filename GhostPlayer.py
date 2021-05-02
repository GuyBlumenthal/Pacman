import pygame

from GameConstants import SQUARE_SIZE as SIZE
import GameConstants


class Ghost:

    def __init__(self, left_home, ghostNum):

        self.left_home = left_home
        self.pos = [left_home[0] * SIZE, left_home[1] * SIZE]

        self.vel = [0, 0]
        self.speed = GameConstants.GHOST_SPEED

        self.home_width = GameConstants.GHOST_HOME_WIDTH

        self.ghost_sprite = None
        self.state = 'idle'

        if ghostNum == 1:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_PURPLE)
        elif ghostNum == 2:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_RED)
        elif ghostNum == 3:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_GREEN)
        elif ghostNum == 4:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_BLUE)

    def render(self, surface):
        ghost_rect = pygame.rect.Rect(self.pos, (SIZE, SIZE))
        ghost_image = self.ghost_sprite

        surface.blit(ghost_image, ghost_rect)

    def tick(self):
        if self.state == 'idle':
            if self.at_home():
                self.wiggle()

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def wiggle(self):
        estimate_col = self.pos[0] / SIZE
        estimate_row = self.pos[1] / SIZE

        at_left = self.left_home[0] == estimate_col
        at_right = self.left_home[0] + self.home_width == estimate_col

        if at_left:
            self.vel = [self.speed, 0]
        elif at_right:
            self.vel = [-self.speed, 0]

    def at_home(self):
        estimate_col = self.pos[0] / SIZE
        estimate_row = self.pos[1] / SIZE

        center_row = (estimate_row - int(estimate_row)) == 0

        if center_row and estimate_row == self.left_home[1]:
            if self.left_home[0] <= estimate_col <= self.left_home[0] + self.home_width:
                return True

        return False
