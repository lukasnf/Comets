import pygame
import numpy as np


class Spaceship:
    """
    class to create the spaceship inheriting from pygame.Rect
    The spaceship is represented as a rectangle for simplicity and defined by its width, height, and position

    """
    friction = .96

    def __init__(self, coordinates, color, width=0):
        self.coordinates = [pygame.math.Vector2(vec) for vec in coordinates]
        self.center()
        self.direction = (self.coordinates[-1] - self.midpoint).normalize()
        self.color = color
        self.velocity = pygame.math.Vector2(0,0)
        self.width = width

    def move(self):
        """
        Move the spaceship based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        for i in range(len(self.coordinates)):
            self.coordinates[i] += self.velocity
            
    
    def deaccelerate(self):
        self.velocity *= Spaceship.friction
        if self.velocity.length() < .3:
            self.velocity = pygame.math.Vector2(0,0)
        

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.coordinates, self.width)
    
    def center(self):
        if len(self.coordinates) == 0:
            return None
        else:
            mid = pygame.math.Vector2(0,0)
            for vec in self.coordinates:
                mid += vec
            self.midpoint = mid / len(self.coordinates)
        return self.midpoint
    
    def rotate(self,angle= -1):
        origin_vec = [self.coordinates[i] - self.midpoint for i in range(len(self.coordinates))]
        for o_vec in origin_vec:
            o_vec.rotate_ip(angle)
        for i in range(len(self.coordinates)):
            self.coordinates[i] = origin_vec[i] + self.midpoint
        self.direction.rotate_ip(angle)
        
    def check_window(self, width, height):

        for i in range(len(self.coordinates)):
            if self.coordinates[i].x >= width:
                self.coordinates[i].x = 0
            elif self.coordinates[i].x <= 0:
                self.coordinates[i].x = width

            if self.coordinates[i].y >= height:
                self.coordinates[i].y = 0
            elif self.coordinates[i].y <= 0:
                self.coordinates[i].y = height
            




    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, height, position, direction, color, and speed.
        """
        return f"Spaceship: coordinates: {self.coordinates}, color: {self.color}, speed: {self.speed}, width: {self.width}"