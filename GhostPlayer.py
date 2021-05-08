import pygame

import Cell
from GameConstants import SQUARE_SIZE as SIZE
import GameConstants


class Ghost:

    def __init__(self, left_home, ghost_num, start_time):

        self.left_home = left_home
        self.pos = [left_home[0] * SIZE, left_home[1] * SIZE]
        self.num = ghost_num

        self.vel = [0, 0]
        self.speed = GameConstants.GHOST_SPEED

        self.home_width = GameConstants.GHOST_HOME_WIDTH

        self.ghost_sprite = None
        self.state = 'idle'

        self.start_time = start_time

        if ghost_num == 1:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_PURPLE)
        elif ghost_num == 2:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_RED)
        elif ghost_num == 3:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_GREEN)
        elif ghost_num == 4:
            self.ghost_sprite = pygame.image.load(GameConstants.GHOST_BLUE)

    def render(self, surface):
        ghost_rect = pygame.rect.Rect(self.pos, (SIZE, SIZE))
        ghost_image = self.ghost_sprite

        surface.blit(ghost_image, ghost_rect)

    def tick(self, game_board, pac_loc, game):
        if self.state == 'idle':
            if self.ready():
                self.state = 'searching'
            elif self.at_home():
                self.state = 'wiggle'
        elif self.state == 'wiggle':
            self.wiggle()
        elif self.state == 'searching':
            if self.vel == (0, 0) or Cell.is_centered(self.pos):
                move_direction = game.path_find([(x - SIZE / 2) / SIZE for x in pac_loc], [x/SIZE for x in self.pos])
                if move_direction == GameConstants.DIR_UP:
                    self.vel = [0, -self.speed]
                elif move_direction == GameConstants.DIR_DOWN:
                    self.vel = [0, self.speed]
                elif move_direction == GameConstants.DIR_RIGHT:
                    self.vel = [self.speed, 0]
                elif move_direction == GameConstants.DIR_LEFT:
                    self.vel = [-self.speed, 0]
                elif move_direction == GameConstants.DIR_NONE:
                    self.vel = [0, 0]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def ready(self):
        if self.num * GameConstants.GHOST_ACTIVATION_TIME < pygame.time.get_ticks() - self.start_time:
            return True
        return False

    def wiggle(self):
        estimate_col = self.pos[0] / SIZE

        at_left = self.left_home[0] == estimate_col
        at_right = self.left_home[0] + self.home_width == estimate_col

        if self.vel == [0, 0]:
            self.vel = [self.speed, 0]
        elif at_left:
            self.vel = [0, 0]
            self.state = 'idle'
        elif at_right:
            self.vel = [-self.speed, 0]

    def at_home(self):
        estimate_col = self.pos[0] / SIZE
        estimate_row = self.pos[1] / SIZE

        center_row = (estimate_row - int(estimate_row)) == 0

        if center_row and estimate_row == self.left_home[1]:
            if self.left_home[0] == estimate_col:
                return True

        return False

