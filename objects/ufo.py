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
        self.max_speed = 4
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
        if random.randint(0, 1):
            # x is first choice
            x = random.randint(int(-Ufo.width/2), int(self.window_width + Ufo.width/2))
            is_on_the_top = random.randint(0, 1)
            y = -Ufo.height/2 if is_on_the_top  else self.window_height + Ufo.height/2
            dx = random.randint(-self.max_speed, self.max_speed)
            dy = (1 if is_on_the_top else -1) * random.randint(0, self.max_speed)
        else:
            # y is first choice
            y = random.randint(int(-Ufo.height/2), int(self.window_height + Ufo.height/2))
            is_on_the_left = random.randint(0, 1)
            x = -Ufo.width/2 if is_on_the_left else self.window_width + Ufo.width/2
            dy = random.randint(-self.max_speed, self.max_speed)
            dx = (1 if is_on_the_left else -1) * random.randint(0, self.max_speed)
        self.ufo = Ufo(x, y, dx, dy) 

    def generate_projectile(self, aim):
        return projectile.Projectile(self.ufo.pos, pygame.math.Vector2.normalize(aim.center() - self.ufo.pos), self.ufo.speed * 2, "ufo", color="green")

class Ufo(flying_object.Flying_Object):
    width = 70 
    height = 30

    def __init__(self, x, y, dx, dy, speed=1, cooldown=1000):
        self.color_metal = "grey"
        self.color_glass = "aqua"
        self.time = pygame.time.get_ticks()
        self.cooldown = cooldown
        flying_object.Flying_Object.__init__(self, pygame.math.Vector2([x, y]), pygame.math.Vector2([dx, dy]), speed)

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

