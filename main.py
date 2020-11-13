import pygame
import sys
from pygame.locals import *


class Square:
    """ The squares containing the symbols """
    def __init__(self, x, y, length):
        self.x, self.y = x, y
        self.length = length

    def collide_point(self, x, y):
        """ Returns True if an x, y coord lies within the square, otherwise False """
        if self.x <= x <= self.x + self.length and self.y <= y <= self.y + self.length:
            return True
        else:
            return False


if __name__ == '__main__':
    root_window = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    squares = []

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
                    if square.collide_point(mouse_x, mouse_y):
                        print(f"Clicked square {squares.index(square)}")
        pygame.display.update()
        clock.tick(60)
