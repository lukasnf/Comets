import pygame
import random
from pathlib import Path



BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item:

    def __init__(self,png,pos):
        self.pos = pos
        path = IMAGES_DIR / png
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        
        image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(image,(30,30))

    def draw(self, surface):
            item_rect = self.image.get_rect(center= self.pos)
            surface.blit(self.image, item_rect)

    
    def move(self, aster_pos):
        pass

        





