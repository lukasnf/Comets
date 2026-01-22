import pygame
import random

class Item:

    def __init__(self,png):
        self.image = pygame.image.load(f"images/{png}").convert_alpha()
        self.pos = pygame.math.Vector2(100,100)

    def draw(self,screen):
        item_image = self.image.get_rect(center= self.pos)
        screen.blit(self.image, item_image)