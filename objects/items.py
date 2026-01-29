import pygame
import random
from pathlib import Path



BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item:

    def __init__(self,png):
        path = IMAGES_DIR / png
        image = pygame.image.load(path).convert_alpha()
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        self.image = pygame.transform.scale(image,(30,30))

    def draw(self, surface, aster_pos):
        rand_int = random.randint(0,5)
        if rand_int == 5:
            item_rect = self.image.get_rect(center= aster_pos)
            surface.blit(self.image, item_rect)

    
    def move(self, aster_pos):
        pass

        





