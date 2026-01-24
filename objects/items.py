import pygame
import random



class Item:

    def __init__(self,png):
        image = pygame.image.load(f"images/{png}").convert_alpha()
        self.image = pygame.transform.scale(image,(30,30))
        
        

    def draw(self, surface):
        item_rect = self.image.get_rect(center= self.pos)
        surface.blit(self.image, item_rect)





