import pygame


class Projectile:

    def __init__(self, start_pos, direction, speed, color):
        self.start_pos = start_pos
        self.direction = direction
        self.speed = speed
        self.color = color
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.start_pos)
    
    def move(self):
        self.start_pos += self.direction * self.speed


        