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
        """
        :param super_surface: The surface on which the button will be blit on
        :param x: the x-coord of the top-left corner of the button
        :param y: the y-coord of the top-left corner of the button
        :param length: The length of the button in pixels
        :param height: The height of the button in pixels
        :param path_unclicked: The path to the image of the button in its normal state
        :param path_clicked:  The path to the image of the button when is clicked
        """
        self.super_surf = super_surface
        self.x, self.y = x, y
        self.length, self.height = length, height
        self.path_unclicked = path_unclicked
        self.path_clicked = path_clicked
        self.surf = pygame.Surface((self.length, self.height))
        self.clicked = False
        self.surf.blit(pygame.image.load(self.path_unclicked), (0, 0))
        self.super_surf.blit(self.surf, (self.x, self.y))


    def collide_point(self, x, y):
        if self.x <= x <= self.x + self.length and self.y <= y <= self.y + self.height:
            return True
        else:
            return False

    def update(self, events):
        self.clicked = False
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
                    self.clicked = True
            elif True:
                self.surf.blit(pygame.image.load(self.path_unclicked), (0, 0))
                self.super_surf.blit(self.surf, (self.x, self.y))


def render_text(super_surf, text, x, y):
    my_font = pygame.font.SysFont('calibri', 30)
    text_surf = my_font.render(text, True, (250, 250, 250), (0, 0, 0))
    super_surf.blit(text_surf, (x, y))


def enter_player1():
    global player1_name
    menu_surf = pygame.Surface((700, 700))
    menu_surf.blit(pygame.image.load('Assets/tictactoe.png'), (224, 80))
    menu_surf.blit(pygame.image.load('Assets/enterp1.png'), (120, 200))
    button1 = Button(menu_surf, 150, 500, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')
    textbox1 = TextInput(menu_surf, 150, 300, 400, 100, (220, 200, 220), max_string_length=12)
    screen.blit(menu_surf, (0, 0))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        textbox1.update(events)
        screen.blit(menu_surf, (0, 0))
        if button1.clicked:
            player1_name = textbox1.get_text()
            return
        pygame.display.update()


def enter_player2():
    global player2_name
    menu_surf = pygame.Surface((700, 700))
    menu_surf.blit(pygame.image.load('Assets/tictactoe.png'), (224, 80))
    menu_surf.blit(pygame.image.load('Assets/enterp2.png'), (120, 200))
    button1 = Button(menu_surf, 150, 500, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')
    textbox1 = TextInput(menu_surf, 150, 300, 400, 100, (220, 200, 220), max_string_length=12)
    screen.blit(menu_surf, (0, 0))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        textbox1.update(events)
        screen.blit(menu_surf, (0, 0))
        if button1.clicked:
            player2_name = textbox1.get_text()
            return
        pygame.display.update()


def play():
    window = pygame.Surface((700, 700))
    squares = []
    player_turn = 1
    can_mark = True
    player1_score, player2_score = 0, 0
    my_font = pygame.font.SysFont('calibri', 25)

    player1_name_surf = my_font.render(f"{player1_name}: {player1_score}", True, (250, 250, 250), (0, 0, 0))
    window.blit(player1_name_surf, (5, 5))

    player2_name_surf = my_font.render(f"{player2_name}: {player2_score}", True, (250, 250, 250), (0, 0, 0))
    window.blit(player2_name_surf, (695 - player2_name_surf.get_width(), 5))

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

    window.blit(grid, (200, 200))
    screen.blit(window, (0, 0))

    def check_for_winner():  # Check whether there is a winner, exits the program if there is a winner
        nonlocal can_mark, player1_score, player2_score

        # Check if crosses win
        if squares[0].symbol == 'X' and squares[1].symbol == 'X' and squares[2].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x - 50, squares[0].y + 50),
                             (squares[2].x + 150, squares[2].y + 50), 4)
        elif squares[3].symbol == 'X' and squares[4].symbol == 'X' and squares[5].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[3].x - 50, squares[3].y + 50),
                             (squares[5].x + 150, squares[5].y + 50), 4)
        elif squares[6].symbol == 'X' and squares[7].symbol == 'X' and squares[8].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[6].x - 50, squares[6].y + 50),
                             (squares[8].x + 150, squares[8].y + 50), 4)
        elif squares[0].symbol == 'X' and squares[3].symbol == 'X' and squares[6].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x + 50, squares[0].y - 50),
                             (squares[6].x + 50, squares[6].y + 150), 4)
        elif squares[1].symbol == 'X' and squares[4].symbol == 'X' and squares[7].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                             (squares[7].x + 50, squares[7].y + 150), 4)
        elif squares[1].symbol == 'X' and squares[4].symbol == 'X' and squares[7].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                             (squares[7].x + 50, squares[7].y + 150), 4)
        elif squares[2].symbol == 'X' and squares[5].symbol == 'X' and squares[8].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[2].x + 50, squares[2].y - 50),
                             (squares[8].x + 50, squares[8].y + 150), 4)
        elif squares[0].symbol == 'X' and squares[4].symbol == 'X' and squares[8].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x - 25, squares[0].y - 25),
                             (squares[8].x + 125, squares[8].y + 125), 4)
        elif squares[2].symbol == 'X' and squares[4].symbol == 'X' and squares[6].symbol == 'X':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[2].x + 125, squares[2].y - 25),
                             (squares[6].x - 25, squares[6].y + 125), 4)

        # Checking if noughts win

        elif squares[0].symbol == 'O' and squares[1].symbol == 'O' and squares[2].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x - 50, squares[0].y + 50),
                             (squares[2].x + 150, squares[2].y + 50), 4)
        elif squares[3].symbol == 'O' and squares[4].symbol == 'O' and squares[5].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[3].x - 50, squares[3].y + 50),
                             (squares[5].x + 150, squares[5].y + 50), 4)
        elif squares[6].symbol == 'O' and squares[7].symbol == 'O' and squares[8].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[6].x - 50, squares[6].y + 50),
                             (squares[8].x + 150, squares[8].y + 50), 4)
        elif squares[0].symbol == 'O' and squares[3].symbol == 'O' and squares[6].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x + 50, squares[0].y - 50),
                             (squares[6].x + 50, squares[6].y + 150), 4)
        elif squares[1].symbol == 'O' and squares[4].symbol == 'O' and squares[7].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                             (squares[7].x + 50, squares[7].y + 150), 4)
        elif squares[1].symbol == 'O' and squares[4].symbol == 'O' and squares[7].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[1].x + 50, squares[1].y - 50),
                             (squares[7].x + 50, squares[7].y + 150), 4)
        elif squares[2].symbol == 'O' and squares[5].symbol == 'O' and squares[8].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[2].x + 50, squares[2].y - 50),
                             (squares[8].x + 50, squares[8].y + 150), 4)
        elif squares[0].symbol == 'O' and squares[4].symbol == 'O' and squares[8].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[0].x - 25, squares[0].y - 25),
                             (squares[8].x + 125, squares[8].y + 125), 4)
        elif squares[2].symbol == 'O' and squares[4].symbol == 'O' and squares[6].symbol == 'O':
            can_mark = False
            pygame.time.wait(250)
            pygame.draw.line(screen, YELLOW, (squares[2].x + 125, squares[2].y - 25),
                             (squares[6].x - 25, squares[6].y + 125), 4)

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
                                window.blit(nought, (square.x + 10, square.y + 10))
                                screen.blit(window, (0, 0))
                                square.symbol = 'O'
                                pygame.display.update()
                            else:
                                window.blit(cross, (square.x + 10, square.y + 10))
                                screen.blit(window, (0, 0))
                                square.symbol = 'X'
                                pygame.display.update()
                            player_turn += 1
                            check_for_winner()

        player1_name_surf = my_font.render(f"{player1_name}: {player1_score}", True, (250, 250, 250), (0, 0, 0))
        window.blit(player1_name_surf, (5, 5))
        player2_name_surf = my_font.render(f"{player2_name}: {player2_score}", True, (250, 250, 250), (0, 0, 0))
        window.blit(player2_name_surf, (700 - player2_name_surf.get_width(), 5))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    player1_name, player2_name = "", ""

    enter_player1()
    enter_player2()
    play()

    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
