import pygame
import math


class Spaceship():
    """
    class to create the spaceship inheriting from pygame.Rect
    The spaceship is represented as a rectangle for simplicity and defined by its width, height, and position

    """

    def __init__(self, coordinates, direction, color, speed, width=0):
        self.coordinates = [pygame.math.Vector2(vec) for vec in coordinates]
        self.direction = pygame.math.Vector2(direction)
        self.color = color
        self.speed = speed
        self.width = width

    def move(self):
        """
        Move the spaceship based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        for i in range(len(self.coordinates)):
            self.coordinates[i] += self.direction * self.speed

    def draw(self, surface):

        pygame.draw.polygon(surface, self.color, self.coordinates, self.width)



    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, height, position, direction, color, and speed.
        """
        return f"Spaceship: coordinates: {self.coordinates}, color: {self.color}, speed: {self.speed}, width: {self.width}"