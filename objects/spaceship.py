import pygame

class Spaceship:
    """

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
            
    
    def decelerate(self):
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
            for i in range(len(self.coordinates)):
                self.coordinates[i] += shift
            self.midpoint += shift

    
   


    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, height, position, direction, color, and speed.
        """
        return f"Spaceship: coordinates: {self.coordinates}, color: {self.color}, speed: {self.speed}, width: {self.width}"