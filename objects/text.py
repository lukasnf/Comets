import pygame


class text():
    """
    Class representing text on the screen. Text can't interact directly with the screen.

    Class atributes:
        text_size: size of the text
        text_font: font of the text
        text_color: color of the text
        text_x: x coordinate of the text
        text_y: y coordinate of the text
    """

    def __init__(self, text_text, text_size, text_font, text_color, text_x, text_y):
        self.text_text = text_text
        self.text_size = text_size
        self.text_font = pygame.font.SysFont(text_font, text_size)
        self.text_color = text_color
        self.text_x = text_x
        self.text_y = text_y

    def render(self):
        self.surface = self.font.render(self.text_font, True, self.color)
        self.rect = self.surface.get_rect(topleft=(self.text_x, self.text_y))

    def set(self, new_text):
        self.text = new_text
        self.render()

    def draw(self, screen):
        #Method to write text on the screen
        screen.blit(self.surface, self.rect)
