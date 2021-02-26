import pygame
import sys
from textinput import TextInput
from pygame.locals import *
from constants import *


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


class Button:
    """ This template will be used to create buttons """
    def __init__(self, super_surface, x, y, length, height, path_unclicked, path_clicked):
        self.super_surf = super_surface
        self.x, self.y = x, y
        self.length, self.height = length, height
        self.path_unclicked = path_unclicked
        self.path_clicked = path_clicked
        self.surf = pygame.Surface((self.length, self.height))

    def collide_point(self, x, y):
        if self.x <= x <= self.x + self.length and self.y <= y <= self.y + self.height:
            return True
        else:
            return False

    def update(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if self.collide_point(mouse_x, mouse_y):
                    self.surf.blit(pygame.image.load(self.path_clicked), (0, 0))
                    self.super_surf.blit(self.surf, (self.x, self.y))
            elif event.type == MOUSEBUTTONUP:
                if self.collide_point(mouse_x, mouse_y):
                    self.surf.blit(pygame.image.load(self.path_unclicked), (0, 0))
                    self.super_surf.blit(self.surf, (self.x, self.y))
            else:
                self.surf.blit(pygame.image.load(self.path_unclicked), (0, 0))
                self.super_surf.blit(self.surf, (self.x, self.y))


def check_for_winner():  # Check whether there is a winner, exits the program if there is a winner
    global can_mark, player1_score, player2_score

    # Check if crosses win
    if squares[0].symbol == 'X' and squares[1].symbol == 'X' and squares[2].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x - 50, squares[0].y + 50),
                         (squares[2].x + 150, squares[2].y + 50), 4)
    elif squares[3].symbol == 'X' and squares[4].symbol == 'X' and squares[5].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[3].x - 50, squares[3].y + 50),
                         (squares[5].x + 150, squares[5].y + 50), 4)
    elif squares[6].symbol == 'X' and squares[7].symbol == 'X' and squares[8].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[6].x - 50, squares[6].y + 50),
                         (squares[8].x + 150, squares[8].y + 50), 4)
    elif squares[0].symbol == 'X' and squares[3].symbol == 'X' and squares[6].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x + 50, squares[0].y - 50),
                         (squares[6].x + 50, squares[6].y + 150), 4)
    elif squares[1].symbol == 'X' and squares[4].symbol == 'X' and squares[7].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                         (squares[7].x + 50, squares[7].y + 150), 4)
    elif squares[1].symbol == 'X' and squares[4].symbol == 'X' and squares[7].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                         (squares[7].x + 50, squares[7].y + 150), 4)
    elif squares[2].symbol == 'X' and squares[5].symbol == 'X' and squares[8].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[2].x + 50, squares[2].y - 50),
                         (squares[8].x + 50, squares[8].y + 150), 4)
    elif squares[0].symbol == 'X' and squares[4].symbol == 'X' and squares[8].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x - 25, squares[0].y - 25),
                         (squares[8].x + 125, squares[8].y + 125), 4)
    elif squares[2].symbol == 'X' and squares[4].symbol == 'X' and squares[6].symbol == 'X':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[2].x + 125, squares[2].y - 25),
                         (squares[6].x - 25, squares[6].y + 125), 4)

    # Checking if noughts win
    elif squares[0].symbol == 'O' and squares[1].symbol == 'O' and squares[2].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x - 50, squares[0].y + 50),
                         (squares[2].x + 150, squares[2].y + 50), 4)
    elif squares[3].symbol == 'O' and squares[4].symbol == 'O' and squares[5].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[3].x - 50, squares[3].y + 50),
                         (squares[5].x + 150, squares[5].y + 50), 4)
    elif squares[6].symbol == 'O' and squares[7].symbol == 'O' and squares[8].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[6].x - 50, squares[6].y + 50),
                         (squares[8].x + 150, squares[8].y + 50), 4)
    elif squares[0].symbol == 'O' and squares[3].symbol == 'O' and squares[6].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x + 50, squares[0].y - 50),
                         (squares[6].x + 50, squares[6].y + 150), 4)
    elif squares[1].symbol == 'O' and squares[4].symbol == 'O' and squares[7].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                         (squares[7].x + 50, squares[7].y + 150), 4)
    elif squares[1].symbol == 'O' and squares[4].symbol == 'O' and squares[7].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                         (squares[7].x + 50, squares[7].y + 150), 4)
    elif squares[2].symbol == 'O' and squares[5].symbol == 'O' and squares[8].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[2].x + 50, squares[2].y - 50),
                         (squares[8].x + 50, squares[8].y + 150), 4)
    elif squares[0].symbol == 'O' and squares[4].symbol == 'O' and squares[8].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[0].x - 25, squares[0].y - 25),
                         (squares[8].x + 125, squares[8].y + 125), 4)
    elif squares[2].symbol == 'O' and squares[4].symbol == 'O' and squares[6].symbol == 'O':
        can_mark = False
        pygame.time.wait(250)
        pygame.draw.line(root_window, YELLOW, (squares[2].x + 125, squares[2].y - 25),
                         (squares[6].x - 25, squares[6].y + 125), 4)


def print_results():
    global player1_score, player2_score
    print(f"Player 1 score - {player1_score}  ;  Player 2 score - {player2_score}")


if __name__ == '__main__':
    root_window = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    squares = []
    player_turn = 1
    player1_score, player2_score = 0, 0
    can_mark = False  # The game has not began yet

    cross = pygame.Surface((80, 80))  # Creating the cross picture
    pygame.draw.line(cross, RED, (0, 0), (80, 80), 12)
    pygame.draw.line(cross, RED, (0, 80), (80, 0), 12)

    nought = pygame.Surface((80, 80))  # Creating the nought picture
    pygame.draw.circle(nought, BLUE, (40, 40), 40, 6)

    # Creating the squares of the grid
    for i in range(3):
        for j in range(3):
            squares.append(Square(200 + j * 100, 200 + i * 100, 100))

    grid = pygame.Surface((301, 301))  # Setting up the empty grid

    for i in range(4):
        pygame.draw.line(grid, (150, 150, 150), (i * 100, 0), (i * 100, 300))

    for i in range(4):
        pygame.draw.line(grid, (150, 150, 150), (0, i * 100), (300, i * 100))

    root_window.blit(grid, (200, 200))  # TODO this should be moved forward

     # Creating the main menu
    main_menu = pygame.Surface((700, 700))
    main_menu.blit(pygame.image.load('Assets/tictactoe.png'), (224, 80))
    main_menu.blit(pygame.image.load('Assets/enterp1.png'), (120, 200))
    button1 = Button(main_menu, 150, 500, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')
    root_window.blit(main_menu, (0, 0))
    textbox_surf = pygame.Surface((400, 100))
    textbox = TextInput(max_string_length=18)

    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if can_mark:
                    for square in squares:
                        if square.symbol:  # Checks if a square already has been marked with an X or O
                            continue
                        if square.collide_point(mouse_x, mouse_y):
                            if player_turn % 2 == 0:
                                root_window.blit(nought, (square.x + 10, square.y + 10))
                                square.symbol = 'O'
                                pygame.display.update()
                            else:
                                root_window.blit(cross, (square.x + 10, square.y + 10))
                                square.symbol = 'X'
                                pygame.display.update()
                            player_turn += 1
                            check_for_winner()
            elif event.type == KEYDOWN:
                if event.key == K_0:
                    print_results()

        textbox.update(events)

        textbox_surf.fill((220, 200, 220))
        textbox_surf.blit(textbox.get_surface(), (10, 10))

        main_menu.blit(textbox_surf, (150, 300))
        button1.update(events)
        root_window.blit(main_menu, (0, 0))


        pygame.display.update()
        clock.tick(60)
