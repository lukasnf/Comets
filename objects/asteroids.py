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
        level = random.randint(0, 2)
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
            if (aster.pos[0] < -ASTEROID_SIZES[2] and aster.direction[0] < 0):
                aster.pos[0] = self.window_width + ASTEROID_SIZES[2]
            elif (aster.pos[0] > self.window_width + ASTEROID_SIZES[2] and aster.direction[0] > 0):
                aster.pos[0] = -ASTEROID_SIZES[2]
            
            if (aster.pos[1] < -ASTEROID_SIZES[2] and aster.direction[1] < 0):
                aster.pos[1] = self.window_height + ASTEROID_SIZES[2]
            elif (aster.pos[1] > self.window_height + ASTEROID_SIZES[2] and aster.direction[1] > 0):
                aster.pos[1] = -ASTEROID_SIZES[2]
    
    def collision_detection(self):
        """
        proofs collsion in of the asteroids.
        """
        for asteriod1 in self.collection:
            for asteriod2 in self.collection:
                if asteriod1 == asteriod2:
                    continue
                if (asteriod1.pos - asteriod2.pos).length() <= asteriod1.radius + asteriod2.radius:
                    self.elastic_impact(asteriod1, asteriod2)
                    self.seperate_asteriods(asteriod1, asteriod2)

    def elastic_impact(self, asteriod1, asteriod2):
        connecting_line = asteriod1.pos - asteriod2.pos
        angle = math.radians(pygame.math.Vector2([1, 0]).angle_to(connecting_line)) # convert degree to radiant
        asteriod1.direction = self.calculate_new_velocity(angle, asteriod1, asteriod2)
        asteriod2.direction = self.calculate_new_velocity(angle, asteriod2, asteriod1)

    def calculate_new_velocity(self, angle, asteriod1, asteriod2):
        """
        Calulcates the velocity for asteriod1. 
        """
        rotate_vector = pygame.math.Vector2([math.cos(angle), math.sin(angle)])
        v1t = pygame.math.Vector2([
            (asteriod1.direction[0] * math.sin(angle) - asteriod1.direction[1] * math.cos(angle)) * math.sin(angle),
            (-asteriod1.direction[0] * math.sin(angle) + asteriod1.direction[1] * math.cos(angle)) * math.cos(angle)
        ])
        v1n = (((asteriod1.mass - asteriod2.mass) * (asteriod1.direction * rotate_vector) + 2 * asteriod2.mass * (asteriod2.direction * rotate_vector)) 
               / (asteriod1.mass + asteriod2.mass)) * rotate_vector
        return v1t + v1n

    def seperate_asteriods(self, asteriod1, asteriod2):
        """
        If two asteroids overlap, they have to be separated before the new velocities can be calculated.

        Parameters:
            asteriod1, asteriod2 (Asteriod)
        """
        dist = (asteriod1.pos - asteriod2.pos).length()
        overlap1 = asteriod1.radius - (asteriod1.radius**2 - asteriod2.radius**2 + dist**2) / (2 * dist)
        overlap2 = asteriod2.radius - (asteriod2.radius**2 - asteriod1.radius**2 + dist**2) / (2 * dist)
        asteriod1.pos -= ((asteriod2.pos - asteriod1.pos) / dist) * overlap1
        asteriod2.pos += ((asteriod2.pos - asteriod1.pos) / dist) * overlap2

    def hit_detection(self, bullets):
        for bullet in bullets:
            if bullet.source != "ship":
                continue
            for asteriod in self.collection:
                if (bullet.pos - asteriod.pos).length() < asteriod.radius:
                    #Falls ein asteriod getroffen
                    bullet.hit = True
                    self.collection.remove(asteriod)
                    if asteriod.level > 0:
                        self.spilt_asteriods(asteriod, bullet)
                    return        
                    
    def spilt_asteriods(self, asteriod, bullet):
        scattering_angle = random.randint(15, 50) # degrees
        bullet_direction_impact = bullet.direction / 5
        new_pos1 = asteriod.pos + (bullet.direction.rotate(90) / bullet.direction.length()) * ASTEROID_SIZES[asteriod.level - 1]
        new_pos2 = asteriod.pos + (bullet.direction.rotate(270) / bullet.direction.length()) * ASTEROID_SIZES[asteriod.level - 1]
        if asteriod.direction.angle_to(asteriod.direction) <= 180:
            new_direction1 = bullet_direction_impact + asteriod.direction.rotate(scattering_angle)
            new_direction2 = bullet_direction_impact + asteriod.direction.rotate(360 - scattering_angle)
        else:
            new_direction2 = bullet_direction_impact + asteriod.direction.rotate(scattering_angle)
            new_direction1 = bullet_direction_impact + asteriod.direction.rotate(360 - scattering_angle)
        self.collection.append(Asteroid(asteriod.level - 1, new_pos1[0], new_pos1[1], new_direction1[0], new_direction1[1]))
        self.collection.append(Asteroid(asteriod.level - 1, new_pos2[0], new_pos2[1], new_direction2[0], new_direction2[1]))
        

    

    

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
        self.color = color

        flying_object.Flying_Object.__init__(
            self, pygame.math.Vector2([x, y]), pygame.math.Vector2([dx, dy]), speed)
        pygame.Rect.__init__(self,
            self.pos[0], self.pos[1], 2 * self.radius, 2 * self.radius
        )  # pygame.Rect wants the coordinates in (left, top, width, height)
        

    def draw(self, surface):
        """
        Draw the asteroid as a circle on the given surface.
        To draw the circle, we need to calculate its center position.

        Parameters:
            surface (pygame.Surface): The surface to draw the asteroid on.
        """

        pygame.draw.circle(
            surface, pygame.Color(self.color), self.pos, self.radius, 3
        )  # last number if the box width


    def __str__(self):
        """
        String representation of the asteroid's current state, including position and velocity.

        Returns:
            str: A string describing the asteroid's attributes with radius, position, direction, color, and speed.
        """
        return f"Asteroid(radius={self.radius}, x={self.pos[0]}, y={self.pos[1]}, dx={self.direction[0]}, dy={self.direction[1]}, color={self.color}, speed={self.speed})"
