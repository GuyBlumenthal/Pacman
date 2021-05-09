import pygame

import Cell
import CellType
import GameConstants
from PacmanPlayer import Pacman
from GhostPlayer import Ghost
from Cell import GameCell
from GameConstants import SQUARE_SIZE
from GameConstants import FPS
from GameConstants import LAYOUT_PATH


def h_function(start, target):
    return pow(pow(start[0] - target[0], 2) + pow(start[1] - target[1], 2), 0.5)


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


class Game:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.game_over = False
        self.score = 0

        self.start_time = pygame.time.get_ticks()

        self.game_board = []
        self.player_start = 0, 0
        self.ghosts = []
        self.tunnels = []
        self.rows, self.columns = self.read_layout_file()

        self.size = self.width, self.height = self.columns * SQUARE_SIZE, self.rows * SQUARE_SIZE
        self.display = pygame.display.set_mode(self.size)

        self.pacman = Pacman(self.player_start)

    def read_layout_file(self):
        layout_file = open(LAYOUT_PATH, 'r').readlines()

        rows = len(layout_file)
        columns = len(layout_file[0]) - 1

        for row in range(rows):
            self.game_board.append([])
            for col in range(len(layout_file[row])):
                c = layout_file[row][col]
                cell_type = CellType.EMPTY
                if c == '#':
                    cell_type = CellType.WALL
                elif c == '.':
                    cell_type = CellType.FOOD
                elif c == '|' or c == '-':
                    cell_type = CellType.GHOST_CAGE_WALL
                elif c == '~':
                    cell_type = CellType.GHOST_CAGE_INNER
                elif c == 'P':
                    self.player_start = col, row
                elif c == 'X':
                    cell_type = CellType.POWER_FOOD
                elif c == 'G':
                    self.ghosts.append(Ghost((col, row), len(self.ghosts) + 1, self.start_time))
                elif c == 'T':
                    cell_type = CellType.TUNNEL
                    self.tunnels.append((row, col))
                self.game_board[row].append(GameCell(col, row, cell_type))

        return rows, columns

    def render(self):
        self.display.fill([0] * 3)
        self.pacman.render(self.display)
        for row in self.game_board:
            for cell in row:
                cell.render(self.display)
        for ghost in self.ghosts:
            ghost.render(self.display)

    def start_game(self):
        self.game_over = False
        self.game_loop()

    def game_loop(self):
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.pacman.handle_event(event)

            self.clock.tick(FPS)
            self.render()
            self.pacman.tick(self.game_board, self)
            for ghost in self.ghosts:
                ghost.tick(self.game_board, self.pacman.center_loc, self)

            pygame.display.update()

    def eat_food(self, row, col):
        score, power_up = self.game_board[row][col].eat()

        if power_up:
            self.pacman.power_up()
        self.increase_score(score)

    def increase_score(self, increment):
        self.score += increment
        print(self.score)

    def path_find(self, target_loc, start_loc):

        start_loc = int(start_loc[1]), int(start_loc[0])
        target_loc = int(target_loc[1]), int(target_loc[0])

        open_set = [start_loc]

        came_from = {}

        g_score = {
            (open_set[0]): 0
        }

        h_score = {
            (open_set[0]): h_function(open_set[0], target_loc)
        }

        while len(open_set) > 0:
            c_cell = open_set[0]
            c_f = g_score[c_cell] + h_score[c_cell]
            for cell in open_set:
                f_score = g_score[cell] + h_score[cell]
                if f_score < c_f:
                    c_cell = cell
                    c_f = f_score

            if c_cell == target_loc:
                path = reconstruct_path(came_from, c_cell)
                if len(path) == 1:
                    return GameConstants.DIR_NONE
                if path[0][0] < path[1][0]:
                    return GameConstants.DIR_DOWN
                elif path[0][0] > path[1][0]:
                    return GameConstants.DIR_UP
                elif path[0][1] < path[1][1]:
                    return GameConstants.DIR_RIGHT
                elif path[0][1] > path[1][1]:
                    return GameConstants.DIR_LEFT
                return GameConstants.DIR_NONE

            open_set.remove(c_cell)

            for neighbour in Cell.get_neighbours(c_cell):
                board_cell = self.game_board[neighbour[0]][neighbour[1]]
                if board_cell.cell_type in GameConstants.PASSABLE_CELLS:
                    tentative_g_score = g_score[c_cell] + 1
                    if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                        came_from[neighbour] = c_cell
                        g_score[neighbour] = tentative_g_score
                        h_score[neighbour] = h_function(neighbour, target_loc)
                        if neighbour not in open_set:
                            open_set.append(neighbour)

        return GameConstants.DIR_NONE


if __name__ == "__main__":
    pacman_game = Game()
    pacman_game.start_game()
