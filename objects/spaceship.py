import pygame
import math


class Spaceship():
    """
    class to create the spaceship inheriting from pygame.Rect
    The spaceship is represented as a rectangle for simplicity and defined by its width, height, and position

    """

    def __init__(self, coordinates, color, speed, width=0):
        self.coordinates = coordinates
        self.color = color
        self.speed = speed
        self.width = width
        self.height = coordinates[0][0]

    def move(self):
        """
        Move the spaceship based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        self.x = self.x + self.dx * self.speed
        self.y = self.y + self.dy * self.speed

    def draw(self, surface):

        pygame.draw.polygon(surface, self.color, self.coordinates, self.width)



    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, height, position, direction, color, and speed.
        """
        return f"Spaceship(width={self.width}, height={self.height}, x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}, color={self.color}, speed={self.speed})"
