import pygame


class Asteroid(pygame.Rect):
    """
    class to create the asteroids inheriting from pygame.Rect
    The asteroid is represented as a circle for simplicity and defined by its radius and position.

    Attributes:
        radius (int): The radius of the asteroid.
        mass (int): The mass of the asteroid, set equal to its radius.
        x (int): The left position of the asteroid.
        y (int): The top position of the asteroid.
        dx (int): The x component of the asteroid's direction vector.
        dy (int): The y component of the asteroid's direction vector.
        color (str): The color of the asteroid.
        speed (int): The speed of the asteroid.
    """

    def __init__(self, radius, x, y, dx=0, dy=0, color="red", speed=1):
        """
        Initialize the asteroid with its radius, position, direction, color, and speed.

        Parameters:
            radius (int): The radius of the asteroid.
            x (int): The left position of the asteroid.
            y (int): The top position of the asteroid.
            dx (int): The x component of the asteroid's direction vector. Default is 0.
            dy (int): The y component of the asteroid's direction vector. Default is 0.
            color (str): The color of the asteroid. Default is "white".
            speed (int): The speed of the asteroid. Default is 1.
        """

        self.radius = radius
        self.mass = radius
        self.x = x  # left position
        self.y = y  # top position
        self.color = color
        self.speed = speed
        self.dx = dx
        self.dy = dy

        super().__init__(
            self.x, self.y, 2 * self.radius, 2 * self.radius
        )  # pygame.Rect wants the coordinates in (left, top, width, height)

    def draw(self, surface):
        """
        Draw the asteroid as a circle on the given surface.
        To draw the circle, we need to calculate its center position.

        Parameters:
            surface (pygame.Surface): The surface to draw the asteroid on.
        """

        center = (self.x + self.radius, self.y + self.radius)
        pygame.draw.circle(
            surface, pygame.Color(self.color), center, self.radius, 3
        )  # last number if the box width

    def move(self):
        """
        Move the asteroid based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        self.x = self.x + self.dx * self.speed
        self.y = self.y + self.dy * self.speed

    def __str__(self):
        """
        String representation of the asteroid's current state, including position and velocity.

        Returns:
            str: A string describing the asteroid's attributes with radius, position, direction, color, and speed.
        """
        return f"Asteroid(radius={self.radius}, x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}, color={self.color}, speed={self.speed})"
