import pygame, sys
from pygame.locals import *
from textinput import TextInput


class Button:
    """ This template will be used to create buttons """
    def __init__(self, super_surface, x, y, length, height, path_unclicked, path_clicked, on_click_func):
        self.super_surf = super_surface
        self.x, self.y = x, y
        self.length, self.height = length, height
        self.path_unclicked = path_unclicked
        self.path_clicked = path_clicked
        self.on_click_func = on_click_func
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
                    if self.on_click_func is not None:
                        self.on_click_func()
            else:
                self.surf.blit(pygame.image.load(self.path_unclicked), (0, 0))
                self.super_surf.blit(self.surf, (self.x, self.y))


def show_window1():
    window1 = pygame.Surface((700, 700))
    window1.fill((50, 0, 0))
    button1 = Button(root, 10, 10, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png', show_window2)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)

        pygame.display.update()


def show_window2():
    window1 = pygame.Surface((700, 700))
    window1.fill((50, 0, 100))
    button1 = Button(root, 100, 350, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png', None)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        pygame.display.update()


def main():
    pygame.init()
    show_window1()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()


if __name__ == '__main__':
    root = pygame.display.set_mode((700, 700))
    main()
