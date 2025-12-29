import pygame
from objects import flying_object

class Projectile(flying_object.Flying_Object):

    def __init__(self, pos, direction, speed, radius, color):
        self.radius = radius
        self.color = color
        self.hit = False # True if the bullet has hit something
        flying_object.Flying_Object.__init__(self, pos.copy(), direction.copy(), speed)
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


        