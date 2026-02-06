import pygame
from objects.flying_object import Flying_Object
from pathlib import Path



BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item(Flying_Object):

    def __init__(self, pos, direction, speed, png):
        super().__init__(pos, direction, speed)
        image_path = IMAGES_DIR / png
        self.original_image = pygame.image.load(image_path).convert_alpha()
        
        self.size = [0,0]
        self.end_size = [35,35]
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
          
    def check_collision(coordinates):
         pass
    
class Heart_Item(Item):
     
     def __init__(self, pos, direction, speed):
        heart_png = "heart pixel art 254x254.png"
        self.duration = 4000 #in ms
        super().__init__(pos, direction, speed, heart_png)

class Shield_Item(Item):
     
     def __init__(self, pos, direction, speed):
          shield_png = "shield.png"
          self.duration = 3000 #in ms 
          super().__init__(pos, direction, speed, shield_png)
        
class Rapid_Fire_Item(Item):
     
     def __init__(self, pos, direction, speed):
          fire_png = "bullet.png"
          self.duration = 3500 #in ms
          super().__init__(pos, direction, speed, fire_png)

class Extra_Point_Item(Item):
     
     def __init__(self, pos, direction, speed):
          coin_png = "coin.png"
          self.duration = 2000 #in ms
          super().__init__(pos, direction, speed, coin_png)

class Feather_Item(Item):

     def __init__(self, pos, direction, speed):
          feather_png = "feather.png"
          self.duration = 3000 #in ms

          super().__init__(pos, direction, speed, feather_png)

class Speed_Item(Item):

     def __init__(self, pos, direction, speed):
          speed_png = "speed.png"
          self.duration = 3000 #in ms
          super().__init__(pos, direction, speed, speed_png)

