"""
projectile.py is a module handeling all kinds of projectiles (bullets) for the Asteroid game.
"""
import pygame
from objects import flying_object

class Projectile(flying_object.Flying_Object):
    """
    Represents a single projecitle fired by the player.
    Inherits from Flying_Object to manage movement.
    """
    def __init__(self, pos, direction, speed, source, radius= 2, color= "cyan"):
        """
        Initializes a new projectile.
        
         Attributes:
            pos (pygame.Vector2): position vector a the projectile.
            direction (pygame.Vector2): direction vector of the projectile.
            speed (float): float, which scales the direction vector.
            source (obj): object, which fires the projectile.
            radius (int): radius of the projectile. Default: 2.
            color (str): projectile's color. Default: cyan 
        """
        self.radius = radius
        self.color = color
        self.hit = False # True if the bullet has hit something
        self.source = source
        super().__init__(pos.copy(), direction.copy(), speed)
    
    def draw(self, surface):
        """
        Draws the projectile as a pygame.circle.

         Attrubutes:
            surface (pygame.window): surface on which should be drawn.
        """
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
    
    def check_window(self, width, height):
        """
        Checks, if the projectile left the game window.
        
         Attributes: 
            width (int): width of the game window
            height (int): height of the game window
         Returns:
            bool: True if the projectile elft the window.
        """

        if (self.pos.x > width or self.pos.x < 0 
            or self.pos.y > height or self.pos.y < 0):
            return True
        return False
