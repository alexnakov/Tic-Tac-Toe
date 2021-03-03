import pygame, sys
from pygame.locals import *


class Text:
    def __init__(self, super_surf, text, x, y, text_color=(200, 200, 0), bg_color=(0, 0, 0), font='calibri'):
        self.super_surf = super_surf
        self.text = text
        self.x, self.y = x, y
        self.text_color = text_color
        self.bg_color = bg_color
        self.font = self.font

        self.render()

    def render(self):
        my_font = pygame.font.SysFont(self.font, 20)
        text_surf = my_font.render(self.text, True, self.text_color, self.bg_color)
        self.super_surf.blit(text_surf, (self.x, self.y))




def main():
    root.fill((100, 100, 0))
    score = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                score += 1

        render_text(root, f"score {score}", 10, 10)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    root = pygame.display.set_mode((700, 700))
    main()
