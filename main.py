import pygame
from PacmanPlayer import Pacman
from GhostPlayer import Ghost
from Cell import *
from GameConstants import SQUARE_SIZE
from GameConstants import FPS
from GameConstants import LAYOUT_PATH


class Game:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.game_over = False
        self.score = 0

        self.game_board = []
        self.player_start = 0, 0
        self.ghosts = []
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
                    self.ghosts.append(Ghost((col, row), len(self.ghosts) + 1))
                self.game_board[row].append(GameCell(col, row, cell_type))

        return rows, columns

    def render(self):
        self.display.fill([0] * 3)
        for row in self.game_board:
            for cell in row:
                cell.render(self.display)
        for ghost in self.ghosts:
            ghost.render(self.display)
        self.pacman.render(self.display)

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
                ghost.tick()

            pygame.display.update()

    def eat_food(self, row, col):
        score, power_up = self.game_board[row][col].eat()

        if power_up:
            self.pacman.power_up()
        self.increase_score(score)

    def increase_score(self, increment):
        self.score += increment
        print(self.score)


if __name__ == "__main__":
    pacman_game = Game()
    pacman_game.start_game()
