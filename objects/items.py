import pygame
from objects.flying_object import Flying_Object
from pathlib import Path
from objects.spaceship import Healthbar, Spaceship



BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item(Flying_Object):

    def __init__(self, pos, direction, speed, png):
        super().__init__(pos, direction, speed)
        image_path = IMAGES_DIR / png
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = [0,0]
        self.grow_speed = 2
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
            self.item_rect = self.image.get_rect(center= self.pos)
            surface.blit(self.image, self.item_rect)
          
    def check_collision(self, coordinates):
         if any((position - self.pos).length() < (self.size[0]/2) for position in coordinates):
              self.apply_time = pygame.time.get_ticks()
              self.hit = True
              return True
         return False
    
class Heart_Item(Item):
     
     def __init__(self, pos, direction, speed):
        heart_png = "heart pixel art 254x254.png"
        self.duration = 5000 #in ms
        self.end_size = [30,30]
        super().__init__(pos, direction, speed, heart_png)
     
     def apply(self, healthbar):
          healthbar.hp = healthbar.max_hp 
          

class Shield_Item(Item):
     
     def __init__(self, pos, direction, speed):
          shield_png = "shield.png"
          self.duration = 3500 #in ms 
          self.end_size = [50,50]
          super().__init__(pos, direction, speed, shield_png)
     
     def apply(self, damage):
          dmg == damage
          if pygame.time.get_ticks() - self.apply_time < 4000:
               dmg = 0
          else:
               dmg = damage
        
class Rapid_Fire_Item(Item):
     
     def __init__(self, pos, direction, speed):
          fire_png = "bullet.png"
          self.duration = 5000 #in ms
          self.end_size = [30,30]
          super().__init__(pos, direction, speed, fire_png)

class Extra_Point_Item(Item):
     
     def __init__(self, pos, direction, speed):
          coin_png = "coin.png"
          self.duration = 5000 #in ms
          self.end_size = [40,40]
          super().__init__(pos, direction, speed, coin_png)


class Feather_Item(Item):

     def __init__(self, pos, direction, speed):
          feather_png = "bullet.png"
          self.duration = 3000 #in ms
          self.end_size = [45,45]
          super().__init__(pos, direction, speed, feather_png)

class Speed_Item(Item):

     def __init__(self, pos, direction, speed):
          speed_png = "bullet.png"
          self.duration = 3000 #in ms
          self.end_size = [40,40]
          super().__init__(pos, direction, speed, speed_png)

