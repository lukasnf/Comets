import pygame
import math


class Spaceship(pygame.Rect):
    """
    class to create the spaceship inheriting from pygame.Rect
    The spaceship is represented as a rectangle for simplicity and defined by its width, height, and position.

    Attributes:
        width (int): The width of the spaceship.
        height (int): The height of the spaceship.
        x (int): The left position of the spaceship.
        y (int): The top position of the spaceship.
        dx (int): The x component of the spaceship's direction vector.
        dy (int): The y component of the spaceship's direction vector.
        color (str): The color of the spaceship.
        speed (int): The speed of the spaceship.

    """

    def __init__(self, width, height, x, y, dx=0, dy=-1, color="white", speed=1):
        """
        Initialize the spaceship with its dimensions, position, direction, color, and speed.

        Parameters:
            width (int): The width of the spaceship.
            height (int): The height of the spaceship.
            x (int): The left position of the spaceship.
            y (int): The top position of the spaceship.
            dx (int): The x component of the spaceship's direction vector. Default is 0.
            dy (int): The y component of the spaceship's direction vector. Default is -1 (upwards).
            color (str): The color of the spaceship. Default is "white".
            speed (int): The speed of the spaceship. Default is 1.
        """
        self.width = width
        self.height = height
        self.x = x  # left position
        self.y = y  # top position
        self.dx = dx
        self.dy = dy
        self.color = color
        self.speed = speed

        # Normalize direction vector to ensure movement per frame
        direction_length = math.sqrt(self.dx**2 + self.dy**2)
        if direction_length != 0:
            self.dx /= direction_length
            self.dy /= direction_length

        super().__init__(
            self.x, self.y, self.width, self.height
        )  # pygame.Rect wants the coordinates in (left, top, width, height)

    def move(self):
        """
        Move the spaceship based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        self.x = self.x + self.dx * self.speed
        self.y = self.y + self.dy * self.speed

    def draw(self, surface):
        """
        Draw the spaceship on the given surface.
        Parameters:
            surface (pygame.Surface): The surface to draw the spaceship on.
        """
        pygame.draw.rect(surface, pygame.Color(self.color), self, 1)

    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, height, position, direction, color, and speed.
        """
        return f"Spaceship(width={self.width}, height={self.height}, x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}, color={self.color}, speed={self.speed})"
