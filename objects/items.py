import pygame
import random



class Item:

    def __init__(self,png):
        image = pygame.image.load(f"images/{png}").convert_alpha()
        self.image = pygame.transform.scale(image,(30,30))

    def draw(self, surface, aster_pos):
        item_rect = self.image.get_rect(center= aster_pos)
        surface.blit(self.image, item_rect)

    
    def move(self, aster_pos):
        pass

        





