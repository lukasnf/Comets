import pygame
import random
import math
from objects import flying_object

ASTEROID_SIZES = [20, 35, 50]

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
        level = random.randint(0,2)
        radius = ASTEROID_SIZES[level]
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
        return Asteroid(level, x, y, dx, dy)
    
    def cyclic_boundary_condition(self):
        """
        proofs whether a asteroid is outside the window and do not come back.
        """
        for aster in self.collection:
            if (aster.pos[0] < -aster.radius and aster.direction[0] < 0):
                aster.pos[0] = self.window_width + aster.radius
            elif (aster.pos[0] > self.window_width + aster.radius and aster.direction[0] > 0):
                aster.pos[0] = -aster.radius
            
            if (aster.pos[1] < -aster.radius and aster.direction[1] < 0):
                aster.pos[1] = self.window_height + aster.radius
            elif (aster.pos[1] > self.window_height + aster.radius and aster.direction[1] > 0):
                aster.pos[1] = -aster.radius
    
    def collision_detection(self):
        """
        proofs collsion in of the asteroids.
        """
        for asteriod1 in self.collection:
            for asteriod2 in self.collection:
                if asteriod1 == asteriod2:
                    continue
                if float((asteriod1.pos - asteriod2.pos).length()) < asteriod1.radius + asteriod2.radius:
                    self.elastic_impact(asteriod1, asteriod2)

    def elastic_impact(self, asteriod1, asteriod2):
        perpendicular = asteriod1.pos - asteriod2.pos
        angle = math.radians(pygame.math.Vector2([1, 0]).angle_to(perpendicular)) # convert degree to radiant
        v1t = pygame.math.Vector2([
            (asteriod1.pos[0] * math.sin(angle) - asteriod1.pos[1] * math.cos(angle)) * math.sin(angle),
            (-asteriod1.pos[0] * math.sin(angle) + asteriod1.pos[1] * math.cos(angle)) * math.cos(angle)
        ])
        print(angle)
        
    def calculate_new_velocity(self, angle, asteriod1, asteriod2):
        """
        calulcates the velocity for asteriod1.
        """
        v1t = pygame.math.Vector2([
            (asteriod1.velocity[0] * math.sin(angle) - asteriod1.velocity[1] * math.cos(angle)) * math.sin(angle),
            (-asteriod1.velocity[0] * math.sin(angle) + asteriod1.velocity[1] * math.cos(angle)) * math.cos(angle)
        ])
        v1n = ((asteriod1.mass - asteriod1.mass2)(asteriod1.vel))


class Asteroid(flying_object.Flying_Object, pygame.Rect):
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

    def __init__(self, level, x, y, dx=0, dy=0, color="red", speed=1):
        """
        Initialize the asteroid with its radius, position, direction, color, and speed.

        Parameters:
            #radius (int): The radius of the asteroid.
            level (int): If the astrid is hit by something the lose a level.
            x (int): The left position of the asteroid.
            y (int): The top position of the asteroid.
            dx (int): The x component of the asteroid's direction vector. Default is 0.
            dy (int): The y component of the asteroid's direction vector. Default is 0.
            color (str): The color of the asteroid. Default is "white".
            speed (int): The speed of the asteroid. Default is 1.
        """

        self.level = level
        self.radius = ASTEROID_SIZES[level]
        self.mass = self.radius
        self.x = x  # left position
        self.y = y  # top position
        #self.pos = np.array([x, y])
        self.color = color
        self.dx = dx
        self.dy = dy

        flying_object.Flying_Object.__init__(
            self, pygame.math.Vector2([x, y]), pygame.math.Vector2([dx, dy]), speed)
        pygame.Rect.__init__(self,
            self.x, self.y, 2 * self.radius, 2 * self.radius
        )  # pygame.Rect wants the coordinates in (left, top, width, height)
        

    def draw(self, surface):
        """
        Draw the asteroid as a circle on the given surface.
        To draw the circle, we need to calculate its center position.

        Parameters:
            surface (pygame.Surface): The surface to draw the asteroid on.
        """

        center = (self.pos[0] + self.radius, self.pos[1] + self.radius)
        pygame.draw.circle(
            surface, pygame.Color(self.color), center, self.radius, 3
        )  # last number if the box width


    def __str__(self):
        """
        String representation of the asteroid's current state, including position and velocity.

        Returns:
            str: A string describing the asteroid's attributes with radius, position, direction, color, and speed.
        """
        return f"Asteroid(radius={self.radius}, x={float(self.pos[0])}, y={float(self.pos[1])}, dx={float(self.velocity[0])}, dy={float(self.velocity[1])}, color={self.color}, speed={self.speed})"
