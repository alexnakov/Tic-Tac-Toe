import pygame, sys
from pygame.locals import *


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


def show_window1():
    window1 = pygame.Surface((700, 700))
    window1.fill((0, 0, 200))
    button1 = Button(window1, 10, 10, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        root.blit(window1, (0, 0))
        if button1.clicked:
            return

        pygame.display.update()


def show_window2():
    window1 = pygame.Surface((700, 700))
    window1.fill((250, 0, 1))
    button1 = Button(window1, 100, 300, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')
    root.blit(window1, (0, 0))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        root.blit(window1, (0, 0))
        if button1.clicked:
            return

        pygame.display.update()


def main():
    show_window1()
    show_window2()
    root.fill((100, 100, 0))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    root = pygame.display.set_mode((700, 700))
    main()
