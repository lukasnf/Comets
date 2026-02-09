import pygame
import random
from objects import flying_object
from objects import projectile


class Ufo_Handler:

    def __init__(self, window_width, window_height, period_s):
        self.window_width = window_width
        self.window_height = window_height
        self.ufo_running = False
        self.time = pygame.time.get_ticks()
        self.period = period_s * 1000 # in ms
        self.ufo = None
        self.max_speed = 3
        self.generate_ufo()

    def check_period(self):
        if self.ufo == None and pygame.time.get_ticks() - self.time > self.period:
            self.generate_ufo()
            self.time = pygame.time.get_ticks()

    def move_ufo(self):
        if (self.ufo.pos[0] <= -Ufo.width and self.ufo.direction[0] < 0) or (self.ufo.pos[0] >= self.window_width and self.ufo.direction[0] > 0):
            self.ufo = None
        else:
            self.ufo.move()

    def draw_ufo(self, surface):
        self.ufo.draw(surface)

    def generate_ufo(self):
        self.ufo = Ufo(self.window_height, self.window_width, self.max_speed) 

    def generate_projectile(self, aim):
        return projectile.Projectile(self.ufo.get_center(), pygame.math.Vector2.normalize(aim.center() - self.ufo.pos), self.ufo.speed * 2, "ufo", color="green")

class Ufo(flying_object.Flying_Object):
    width = 70 
    height = 30

    def __init__(self, window_width, window_height, max_speed, cooldown=1000):
        self.color_metal = "grey"
        self.color_glass = "aqua"
        self.time = pygame.time.get_ticks()
        self.cooldown = cooldown
        flying_object.Flying_Object.__init__(self)
        flying_object.Flying_Object.generate_random_border_startpos(self, Ufo.width, Ufo.height, window_width, window_height, speed=max_speed)

    def get_center(self):
        return pygame.math.Vector2(self.pos.x + Ufo.width/2, self.pos.y + Ufo.height/2)

    def shoot(self):
        if pygame.time.get_ticks() > self.time + self.cooldown:
            self.time = pygame.time.get_ticks()
            return True
        return False
        
    def draw(self, surface):
        rect_metal_shield = pygame.Rect(self.pos[0], self.pos[1] + int(Ufo.height / 3), Ufo.width, int(2 * Ufo.height / 3))
        rect_glass_dome = pygame.Rect(self.pos[0] + int(Ufo.width / 3), self.pos[1], int(Ufo.width / 3), int(2 * Ufo.height / 3))
        pygame.draw.ellipse(surface, pygame.Color(self.color_glass), rect_glass_dome)
        pygame.draw.ellipse(surface, pygame.Color(self.color_metal), rect_metal_shield)

