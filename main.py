import pygame
import sys
from pygame.locals import *


class Square:
    """ The squares containing the symbols """

    def __init__(self, x, y, length):
        self.x, self.y = x, y
        self.length = length
        self.symbol = None

    def collide_point(self, x, y):
        """ Returns True if an x, y coord lies within the square, otherwise False """
        if self.x <= x <= self.x + self.length and self.y <= y <= self.y + self.length:
            return True
        else:
            return False


def check_winner():  # Check whether there is a winner, exits the program if there is a winner
    if (squares[0].symbol == 'X' and squares[1].symbol == 'X' and squares[2].symbol == 'X') or \
            (squares[3].symbol == 'X' and squares[4].symbol == 'X' and squares[5].symbol == 'X') or \
            (squares[6].symbol == 'X' and squares[7].symbol == 'X' and squares[8].symbol == 'X') or \
            (squares[0].symbol == 'X' and squares[3].symbol == 'X' and squares[6].symbol == 'X') or \
            (squares[1].symbol == 'X' and squares[4].symbol == 'X' and squares[7].symbol == 'X') or \
            (squares[2].symbol == 'X' and squares[5].symbol == 'X' and squares[8].symbol == 'X') or \
            (squares[0].symbol == 'X' and squares[4].symbol == 'X' and squares[8].symbol == 'X') or \
            (squares[2].symbol == 'X' and squares[4].symbol == 'X' and squares[6].symbol == 'X'):
        pygame.quit()
        sys.exit()
    elif (squares[0].symbol == 'O' and squares[1].symbol == 'O' and squares[2].symbol == 'O') or \
            (squares[3].symbol == 'O' and squares[4].symbol == 'O' and squares[5].symbol == 'O') or \
            (squares[6].symbol == 'O' and squares[7].symbol == 'O' and squares[8].symbol == 'O') or \
            (squares[0].symbol == 'O' and squares[3].symbol == 'O' and squares[6].symbol == 'O') or \
            (squares[1].symbol == 'O' and squares[4].symbol == 'O' and squares[7].symbol == 'O') or \
            (squares[2].symbol == 'O' and squares[5].symbol == 'O' and squares[8].symbol == 'O') or \
            (squares[0].symbol == 'O' and squares[4].symbol == 'O' and squares[8].symbol == 'O') or \
            (squares[2].symbol == 'O' and squares[4].symbol == 'O' and squares[6].symbol == 'O'):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    root_window = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    squares = []
    player_turn = 1

    cross = pygame.Surface((80, 80))  # Creating the cross picture
    pygame.draw.line(cross, (250, 0, 0), (0, 0), (80, 80), 3)
    pygame.draw.line(cross, (250, 0, 0), (0, 80), (80, 0), 3)

    nought = pygame.Surface((80, 80))  # Creating the nought picture
    pygame.draw.circle(nought, (0, 0, 250), (40, 40), 40, 3)

    # Setting up the grid
    for i in range(3):
        for j in range(3):
            squares.append(Square(200 + j * 100, 200 + i * 100, 100))

    for i in range(4):
        pygame.draw.line(root_window, (150, 150, 150), (200 + i * 100, 200), (200 + i * 100, 500))

    for i in range(4):
        pygame.draw.line(root_window, (150, 150, 150), (200, 200 + i * 100), (500, 200 + i * 100))

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for square in squares:
                    if square.symbol:  # Cannot mark a square that has already been marked
                        continue
                    if square.collide_point(mouse_x, mouse_y):
                        if player_turn % 2 == 0:
                            root_window.blit(nought, (square.x + 10, square.y + 10))
                            square.symbol = 'O'
                        else:
                            root_window.blit(cross, (square.x + 10, square.y + 10))
                            square.symbol = 'X'
                        player_turn += 1
                check_winner()

        pygame.display.update()
        clock.tick(60)
