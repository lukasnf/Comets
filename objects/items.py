import pygame
from objects.flying_object import Flying_Object
from pathlib import Path



BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item(Flying_Object):

    def __init__(self, pos, direction, speed, image_path):
        super().__init__(pos, direction, speed)
        self.original_image = pygame.image.load(image_path).convert_alpha()
        
        self.size = [0,0]
        self.end_size = [30,30]
        self.grow_speed= 2
        self.image = pygame.transform.scale(self.original_image, self.size)
        self.hit = False
        self.spawn_time = pygame.time.get_ticks()

    def increase_size(self):
        if self.size[0] < self.end_size[0]:
             self.size[0] += self.grow_speed
             self.size[1] += self.grow_speed
             if self.size[0] > self.end_size[0]:
                  self.size[0] = self.end_size[0]
                  self.size[1] = self.end_size[1]
             self.image = pygame.transform.scale(self.original_image, self.size)
         
    def draw(self, surface):
            self.increase_size()
            item_rect = self.image.get_rect(center= self.pos)
            surface.blit(self.image, item_rect)
    
class Heart_Item(Item):
     
     def __init__(self, pos, direction, speed):
        heart_png= "heart pixel art 254x254.png"
        path =  IMAGES_DIR / heart_png
        self.duration = 4000 #in ms
        super().__init__(pos, direction, speed, path)

class Shield_Item(Item):
     
     def __init__(self, pos, direction, speed):
          shield_png = "shield.png"
          path = IMAGES_DIR / shield_png
          self.duration = 1000 #in ms 
          super().__init__(pos, direction, speed, path)
        
class Rapid_Fire_Item(Item):
     
     def __init__(self, pos, direction, speed):
          fire_png = "rapid_fire.png"
          path = IMAGES_DIR / fire_png
          self.duration = 3500 #in ms
          super().__init__(pos, direction, speed, path)





