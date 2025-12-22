import pygame
import random

class Asteroids:
    """
    A collection of Astroids, which are shown on the window.
    """

    def __init__(self, max_number, min_number, window_height, window_width, max_speed):
        self.max_number = max_number
        self.min_number = min_number
        self.window_height = window_height
        self.window_width = window_width
        self.max_speed = max_speed
        self.collection = [self.generate_astroid() for _ in range(max_number)]

    def generate_astroid(self):
        """
        This generates a asteroid outside the window, which then flies into the frame
        
        Parameter:
            None
        
        Retrun:
            a Asteroids
        """
        radius = random.randint(10, 50)
        if random.randint(0, 1):
            # x is first choice
            x = random.randint(-radius, self.window_width + radius)
            is_on_the_top = random.randint(0, 1)
            y = -radius if is_on_the_top  else self.window_height + radius
            dx = random.randint(-self.max_speed, self.max_speed)
            dy = (1 if is_on_the_top else -1) * random.randint(0, self.max_speed)
        else:
            # y is first choice
            y = random.randint(-radius, self.window_height + radius)
            is_on_the_left = random.randint(0, 1)
            x = -radius if is_on_the_left else self.window_width + radius
            dy = random.randint(-self.max_speed, self.max_speed)
            dx = (1 if is_on_the_left else -1) * random.randint(0, self.max_speed)
        return Asteroid(radius, x, y, dx, dy)
    
    def delete_useless_asteroids(self):
        """
        proofs whether a asteroid is outside the window and do not come back.
        deletes and generates new, if necessary.
        """
        new_collection = []
        for aster in self.collection:
            if self.is_not_in_window(aster):
                new_collection.append(self.generate_astroid())
            else:
                new_collection.append(aster)
        self.collection = new_collection

    def is_not_in_window(self, aster):
        """
        proofs whether a asteroid is outside the window and do not come back.
        """
        return ((aster.x < -aster.radius and aster.dx < 0) or 
                (aster.x > self.window_width + aster.radius and aster.dx > 0) or
                (aster.y < -aster.radius and aster.dy < 0) or 
                (aster.y > self.window_height + aster.radius and aster.dy > 0))
            



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
