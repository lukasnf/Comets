import pygame


class Projectile:

    def __init__(self, start_pos, direction, speed, radius, color):
        self.start_pos = start_pos.copy()
        self.direction = direction.copy()
        self.speed = speed
        self.radius = radius
        self.color = color
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.start_pos, self.radius)
    
    def move(self):
        self.start_pos += self.direction * self.speed


        