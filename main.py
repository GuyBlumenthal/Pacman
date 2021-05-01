import pygame
from Cell import *

FPS = 60

SQUARE_SIZE = 20

LAYOUT_PATH = "layout.txt"


class Game:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.game_over = False

        self.game_board = []
        self.rows, self.columns = self.read_layout_file()

        self.size = self.width, self.height = self.columns * SQUARE_SIZE, self.rows * SQUARE_SIZE
        self.display = pygame.display.set_mode(self.size)

    def read_layout_file(self):
        layout_file = open(LAYOUT_PATH, 'r').readlines()

        rows = len(layout_file)
        columns = len(layout_file[0]) - 1

        for row in range(rows):
            self.game_board.append([])
            for i in range(len(layout_file[row])):
                c = layout_file[row][i]
                cell_type = CellType.EMPTY
                if c == '#':
                    cell_type = CellType.WALL
                elif c == '.':
                    cell_type = CellType.FOOD
                self.game_board[row].append(GameCell(i, row, cell_type))

        return rows, columns

    def tick(self):
        for row in self.game_board:
            for cell in row:
                cell.draw(self.display)

    def start_game(self):
        self.game_over = False

        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.clock.tick(FPS)
            self.tick()

            pygame.display.update()


if __name__ == "__main__":
    pacman_game = Game()
    pacman_game.start_game()
