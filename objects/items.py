import pygame
from objects.flying_object import Flying_Object
from pathlib import Path

# Setup paths for assets
BASE = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE / "images"

class Item(Flying_Object):
    """
    Base class for all collectible items, inheriting from Flying_Object.
    Handles moving, drawing and collision detection logic.
    """

    def __init__(self, pos, direction, speed, png):
        """
        Initializes an Item with its specific porperties.
        
        Attributes:
          pos (pygame.Vector2): position vector for the item.
          direction (pygame.Vector2): direction vector, which dictates further movement.
          speed (float): float, which scales the direction vector.
          png (str): Filename of the specific item stored in the images folder.
        """
        super().__init__(pos, direction, speed)
        image_path = IMAGES_DIR / png
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = [0,0]
        self.grow_speed = 2
        self.image = pygame.transform.scale(self.original_image, self.size)
        self.hit = False
        self.spawn_time = pygame.time.get_ticks()

    def increase_size(self):
        """
        Increases the items size continously until it reaches its end size
        """
        if self.size[0] < self.end_size[0]:
             self.size[0] += self.grow_speed
             self.size[1] += self.grow_speed
             if self.size[0] > self.end_size[0]:
                  self.size[0] = self.end_size[0]
                  self.size[1] = self.end_size[1]
             self.image = pygame.transform.scale(self.original_image, self.size)

    def draw(self, surface):
          """
          Draws the item by creating a pygame rect around it.
            
           Args:
               surface: pygame game window on which sould be drawn.
          """
          self.increase_size()
          self.item_rect = self.image.get_rect(center= self.pos)
          surface.blit(self.image, self.item_rect)
          
    def check_collision(self, coordinates):
         """
         Checks if the item gets obained by the spaceship. 
         
          Args:
               cooridnates (list): list of the spaceship's coordinates.

          Returns:
               bool: True if a collision is detected.
         """
         if any((position - self.pos).length() < (self.size[0]/2) for position in coordinates):
              self.apply_time = pygame.time.get_ticks()
              self.hit = True
              return True
         return False
    
class Heart_Item(Item):
     """
     Item, which restores the spaceship's health to its maximum, if obtained.
     """
     
     def __init__(self, pos, direction, speed):
        """
        Initializes specific item attributes.

          Attributes:
               duration (float): spawn duration of the heart item.
               end_size (list): maximum x,y size of the item image.
        """
        heart_png = "heart pixel art 254x254.png"
        self.duration = 5000 #in ms
        self.end_size = [45,45]
        super().__init__(pos, direction, speed, heart_png)
     
     def apply(self, game):
          """
          Sets the spaceship's health to maximum.

           Args:
               game (class): Game class in which all objects are initialized.
          """
          game.health_bar.hp = game.health_bar.max_hp 
          

class Shield_Item(Item):
     """
     Item, which grants invinciblility, if obtained.
     """
     def __init__(self, pos, direction, speed):
          """
          Initializes specific item attributes.

          Args:
               duration (float): spawn duration of the shield item.
               end_size (list): maximum x,y size of the item image.
          """
          shield_png = "shield.png"
          self.duration = 3500 #in ms 
          self.end_size = [55,55]
          super().__init__(pos, direction, speed, shield_png)
     
     def apply(self, game):
          """
          Defines how long the item should show its effect.
          """
          game.shield_time = pygame.time.get_ticks() + 4000
     
          
class Rapid_Fire_Item(Item):
     """
     Item, which allows to shoot rapidfire, if obtained.
     """
     
     def __init__(self, pos, direction, speed):
          """
          Initializes specific item attributes.

          Attributes:
               duration (float): spawn duration of the rapidfire item.
               end_size (list): maximum x,y size of the item image.
          """
          fire_png = "bullet.png"
          self.duration = 5000 #in ms
          self.end_size = [50,50]
          super().__init__(pos, direction, speed, fire_png)

     def apply(self, game):
          """
          Defines how long the item show its effect.
          """
          game.rapid_fire_time = pygame.time.get_ticks() + 2500

class Extra_Point_Item(Item):
     """
     Item, which grants extra points, if obtained.
     """
     def __init__(self, pos, direction, speed):
          """
          Initializes specific item attributes.

          Attributes:
               duration (float): spawn duration of the extra point item.
               end_size (list): maximum x,y size of the item image.
          """
          coin_png = "coin.png"
          self.duration = 5000 #in ms
          self.end_size = [50,50]
          super().__init__(pos, direction, speed, coin_png)
     
     def apply(self, game):
          """
          Increases, the game score by 100 points.
          """
          game.score += 100
          game.score_text.set(str(game.score).zfill(6))


class Feather_Item(Item):
     """
     Item, which reduces the opponents speed.
     """
     def __init__(self, pos, direction, speed):
          """
          Initializes specific item attributes.

          Attributes:
               duration (float): spawn duration of the extra point item.
               end_size (list): maximum x,y size of the item image.
          """
          feather_png = "speed.png"
          self.duration = 3000 #in ms
          self.end_size = [55,55]
          super().__init__(pos, direction, speed, feather_png)
     
     def apply(self, game):
          """
          Defines how long the item should show its effect.
          """
          game.feather_time = pygame.time.get_ticks() + 4000

class Speed_Item(Item):
     """
     Item, which increases the opponets speed.
     """

     def __init__(self, pos, direction, speed):
          """
          Initializes specific item attributes.

          Attributes:
               duration (float): spawn duration of the extra point item.
               end_size (list): maximum x,y size of the item image.
          """
          speed_png = "speed.PNG"
          self.duration = 3000 #in ms
          self.end_size = [55,55]
          super().__init__(pos, direction, speed, speed_png)
     
     def apply(self, game):
          """
          Defines how long the item should show its effect.
          """
          game.speed_time = pygame.time.get_ticks() + 5000
