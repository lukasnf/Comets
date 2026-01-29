import pygame
from objects import flying_object

class Projectile(flying_object.Flying_Object):

    def __init__(self, pos, direction, speed, radius= 2, color= "cyan"):
        self.radius = radius
        self.color = color
        self.hit = False # True if the bullet has hit something
        super().__init__(pos.copy(), direction.copy(), speed)
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
    
    def check_window(self, width, height):
        if (self.pos.x > width or self.pos.x < 0 
            or self.pos.y > height or self.pos.y < 0):
            return True
        return False
