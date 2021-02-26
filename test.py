import pygame
import sys
from textinput import TextInput
from pygame.locals import *
from constants import *

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


def launch_main_menu(super_surf):
    main_menu = pygame.Surface((700, 700))

    button1 = Button(main_menu, 150, 500, 427, 113, 'Assets/b1u.png', 'Assets/b1c.png')

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)

        main_menu.blit(super_surf, (0, 0))
        pygame.display.update()


def main():
    pygame.init()
    root = pygame.display.set_mode((700, 700))

    launch_main_menu(root)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button1.update(events)
        pygame.display.update()

if __name__ == '__main__':
    main()
