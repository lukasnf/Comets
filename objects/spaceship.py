import pygame
from objects.text import Text

class Spaceship:
    """

    """
    friction = .98

    def __init__(self, color, width=0):
        self.coordinates = [(440,770),(455,765),(470,770),(455,730)]
        self.center()
        self.direction = (self.coordinates[-1] - self.midpoint).normalize()
        self.color = color
        self.velocity = pygame.math.Vector2(0,0)
        self.width = width
        self.alive = True

    def move(self):
        """
        """
        for i in range(len(self.coordinates)):
            self.coordinates[i] += self.velocity

    def decelerate(self):
        self.velocity *= Spaceship.friction
        if self.velocity.length() < .3:
            self.velocity = pygame.math.Vector2(0,0)
        
    def check_health(self, health):
        if health <= 0:
            self.alive = False

    def draw(self, surface):
        if self.alive:
            pygame.draw.polygon(surface, self.color, self.coordinates, self.width)
        
    
    def center(self):
        """
        calculates the center of the spaceship for other calculations
        
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
            self.midpoint += shift
            for i in range(len(self.coordinates)):
                self.coordinates[i] += shift

    def check_collision(self, asteroid_list, bullets):
        self.center()
        #if (any((pos - aster.pos).length() < aster.radius for pos in self.coordinates + [self.midpoint] for aster in asteroid_list) or
        #     any((pos - bullet.pos).length() < 20 and bullet.source != "ship" for pos in self.coordinates + [self.midpoint] for bullet in bullets)):
        #    return True 
        if (any((pos - aster.pos).length() < aster.radius for pos in self.coordinates + [self.midpoint] for aster in asteroid_list) or
            any(self.proof_bullet_collision(bullet) and bullet.source != "ship" for bullet in bullets)):
            return True 
        
    def proof_bullet_collision(self, bullet):
        for index in range(len(self.coordinates)):
            if (index < len(self.coordinates) - 1 and self.do_intersect(self.coordinates[index], self.coordinates[index + 1], bullet.pos, bullet.pos + bullet.direction * bullet.speed) 
                or index >= len(self.coordinates) - 1 and self.do_intersect(self.coordinates[index], self.coordinates[0], bullet.pos, bullet.pos + bullet.direction * bullet.speed)):
                return True
        return False

    def do_intersect(self, line1_start, line1_end, line2_start, line2_end):
        """
        This methode proofs if 2 lines has a intersection point.
        
        :param self: Description
        :param line1_start: Description
        :param line1_end: Description
        :param line2_start: Description
        :param line2_end: Description
        """
        m1 = (line1_start.y - line1_end.y) / (line1_start.x - line1_end.x)
        b1 = line1_start.y - m1 * line1_start.x
        m2 = (line2_start.y - line2_end.y) / (line2_start.x - line2_end.x)
        b2 = line2_start.y - m2 * line2_start.x

        intersection_x = (b2 - b1) / (m1 - m2)

        is_in_line1 = (intersection_x >= line1_start.x and intersection_x <= line1_end.x) or (intersection_x <= line1_start.x and intersection_x >= line1_end.x)
        is_in_line2 = (intersection_x >= line2_start.x and intersection_x <= line2_end.x) or (intersection_x <= line2_start.x and intersection_x >= line2_end.x)

        return is_in_line1 and is_in_line2

    def __str__(self):
        """
        String representation of the spaceship's current state, including position and velocity.

        Returns:
            str: A string describing the spaceship's attributes with width, coordinates, and color.
        """
        return f"Spaceship: coordinates: {self.coordinates}, color: {self.color}, width: {self.width}"
    

class Healthbar:

    def __init__(self, pos, height, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp
        self.height = height
        self.pos = pos

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.pos[0], self.pos[1], self.max_hp, self.height))
        pygame.draw.rect(surface, "green", (self.pos[0], self.pos[1], self.max_hp * ratio, self.height))
        
