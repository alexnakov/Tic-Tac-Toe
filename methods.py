import pygame
pygame.init()


def render_text(text, font_size, letter_color=(250, 250, 250), bg_color=(0, 0, 0)):
    """ Centres the text on the super surface """
    my_font = pygame.font.SysFont('calibri', font_size)
    text_surf = my_font.render(text, True, letter_color, bg_color)
    return text_surf


def render_centered_text(super_surf, text, y, font_size ,padx=0, letter_color=(250, 250, 250),
                         bg_color=(0, 0, 0)):
    """ Centres the text on the super surface
        +ve padx values move text to the right """
    font = pygame.font.SysFont('calibri', font_size)
    text_surface = font.render(text, True,  letter_color, bg_color)
    text_surface_width = text_surface.get_width()
    super_surf_width = super_surf.get_width()
    super_surf.blit(text_surface, ((super_surf_width / 2) - (text_surface_width / 2) + padx, y))
