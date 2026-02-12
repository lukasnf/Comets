import pygame
from objects import flying_object

class Spaceship(flying_object.Flying_Object):
    """
    Represents the players controlled model.
    Polygon based.
    """
    friction = .98

    def __init__(self, color, width=0):
        """
        Initializes the spaceship whth it's shape, color and starting position.

         Attributes:
            friction (float): Constant factor multiplied with the ships velocity to simulate drag.
            coordinates (list): List of the spaceship's coordinates, which are used to update position and draw the polygon.
            midpoint (pygame.Vector2): center of the ship.
            direction (pygame.Vector2): direction vector pointing the nose of the ship.
            color (str): color of the polygon.
            velocity (pygame.Vector2): velocity vector of the spaceship.
            width (int): Line thickness for drawing the polygon. Default: 0
            alive (bool): Boolean indicating if spaceship's health > 0.
        """
        self.coordinates = [(440,770),(455,765),(470,770),(455,730)]
        self.center()
        self.direction = (self.coordinates[-1] - self.midpoint).normalize()
        self.color = color
        self.velocity = pygame.math.Vector2(0,0)
        self.width = width
        self.alive = True

    def move(self):
        """
        Loops through all coordinates and updates them by multiplying with the velocity.
        """
        for i in range(len(self.coordinates)):
            self.coordinates[i] += self.velocity

    def decelerate(self):
        """
        Decelerates the spaceship by applying frition.
        Sets velocity to 0 below a certain value (0.3)
        """
        self.velocity *= Spaceship.friction
        if self.velocity.length() < .3:
            self.velocity = pygame.math.Vector2(0,0)
        
    def check_health(self, health):
        """
        Checks whether the ship's health is positive.
         Attributes:
            health (int): Current life points of the spaceship.
        """
        if health <= 0:
            self.alive = False

    def draw(self, surface):
        """
        Draws the ship as the pygame polygon and displays it if the ship is alive.
        """
        if self.alive:
            pygame.draw.polygon(surface, self.color, self.coordinates, self.width)
        
    
    def center(self):
        """
        Calculates the center of the spaceship for other calculations.

         Returns:
            midpoint (pygame.Vector2): center of the spaceship.
        """
        if len(self.coordinates) == 0:
            return None
        else:
            mid = pygame.math.Vector2(0,0)
            for vec in self.coordinates:
                mid += vec
            self.midpoint = mid / len(self.coordinates)
        return self.midpoint
    
    def rotate(self,angle= -1):
        """
        Rotates the the origin vectors of the coordinates to rotate them around the origin and move them back to their position on the screen.
         
         Args: 
            angle (int): Rotationangle "-" inidcates counterclockwise rotation. Default: -1 
        """
        origin_vec = [self.coordinates[i] - self.midpoint for i in range(len(self.coordinates))]
        for o_vec in origin_vec:
            o_vec.rotate_ip(angle)
        for i in range(len(self.coordinates)):
            self.coordinates[i] = origin_vec[i] + self.midpoint
        self.direction.rotate_ip(angle)
        
    def check_window(self, width, height):
        """
        Realizes cyclic boundary condition on the spaceship. Warps it to the cooresponding side if the ship left the game window.
         
         Args:
            width (int): pygame window witdh.
            height (height): pygame window height.

        """
        shift = pygame.math.Vector2(0,0)
        width_out = False
        height_out = False

        if self.midpoint.x > width:
            shift.x = -width
            width_out = True
        elif self.midpoint.x < 0:
            shift.x = width
            width_out = True

        if self.midpoint.y > height:
            shift.y = -height
            height_out = True
        elif self.midpoint.y < 0:
            shift.y = height
            height_out = True
        
        if height_out or width_out:
            self.midpoint += shift
            for i in range(len(self.coordinates)):
                self.coordinates[i] += shift

    def check_collision(self, asteroid_list, bullets):
        """
        Checks if a entity collides with the spaceship.

         Args:
            asteroid_list (list): List of all currently existing asteroids and ther corresponding attributes.
            bullets (list): List of all currently existing bullets and their corrensponding attributes.
        
         Returns:
          bool: True on impact with an entity.
        """
        self.center()
        #if (any((pos - aster.pos).length() < aster.radius for pos in self.coordinates + [self.midpoint] for aster in asteroid_list) or
        #     any((pos - bullet.pos).length() < 20 and bullet.source != "ship" for pos in self.coordinates + [self.midpoint] for bullet in bullets)):
        #    return True 
        if (any((pos - aster.pos).length() < aster.radius for pos in self.coordinates + [self.midpoint] for aster in asteroid_list) or
            any(self.proof_bullet_collision(bullet) for bullet in list(filter(lambda x : x.source != "ship", bullets)))):
            return True 
        
    def proof_bullet_collision(self, bullet):
        for index in range(len(self.coordinates)):
            if (index < len(self.coordinates) - 1 and self.do_intersect(self.coordinates[index], self.coordinates[index + 1], bullet.pos, bullet.pos + bullet.direction * bullet.speed) 
                or index >= len(self.coordinates) - 1 and self.do_intersect(self.coordinates[index], self.coordinates[0], bullet.pos, bullet.pos + bullet.direction * bullet.speed)):
                return True
        return False

    
    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, coordinates, and color.
        """
        return f"Spaceship: coordinates: {self.coordinates}, color: {self.color}, width: {self.width}"
    

class Healthbar:
    """
    Class handeling the healthbar, which displays the ship's current health and current health loss.
    """
    def __init__(self, pos, height, max_hp):
        """
        Initializes healthbar.
        
         Attributes:
            hp (int) = current healthpoints of the ship.
            max_hp (int) = maximum healthpoints.
            height (int) = height of the rects representing the healthbar.
            pos (tuple) = topleft cooridnates of the healthbar.
        """
        self.hp = max_hp
        self.max_hp = max_hp
        self.height = height
        self.pos = pos

    def draw(self, surface):
        """
        Draws the healthbar, consititing of 2 pygame rects filled whith green to show healthpoints and a red one for health-loss.
        """
        pygame.draw.rect(surface, "red", (self.pos[0], self.pos[1], self.max_hp, self.height))
        pygame.draw.rect(surface, "green", (self.pos[0], self.pos[1], self.hp,  self.height))
        
