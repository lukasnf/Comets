import random
import pygame

class Flying_Object:
    """
    This is a general object in space.

    Attributes:
        pos (pygame.math.Vector2): The position of the object in space.
        direction (pygame.math.Vector2): The direction of motion in space.
        speed (int): The speed of the object.
    """


    def __init__(self, pos=pygame.math.Vector2(), direction=pygame.math.Vector2(), speed=1):
        """
        Docstring for __init__
        
        :param self: Description
        :param pos: Description
        :param direction: Description
        :param speed: Description
        """
        self.pos = pos
        self.direction = direction
        self.speed = speed

    def move(self):
        """
        Move the Object based on its direction and speed. It is moved in a direction scaled by speed.
        """
        self.pos = self.pos + self.direction * self.speed

    def generate_random_border_startpos(self, object_width, object_height, window_width, window_height, max_speed=None, speed=None):
        if random.randint(0, 1):
            # x is first choice
            x = random.randint(int(-object_width/2), int(window_width + object_width/2))
            is_on_the_top = random.randint(0, 1)
            y = -object_height/2 if is_on_the_top  else window_height + object_height/2
            dx = random.uniform(-1, 1)
            dy = (1 if is_on_the_top else -1) * random.uniform(0.1, 1)
        else:
            # y is first choice
            y = random.randint(int(-object_height/2), int(window_height + object_height/2))
            is_on_the_left = random.randint(0, 1)
            x = -object_height/2 if is_on_the_left  else window_height + object_width/2
            dy = random.uniform(-1, 1)
            dx = (1 if is_on_the_left else -1) * random.uniform(0.1, 1)
        self.pos = pygame.math.Vector2(x,y)
        self.direction = pygame.math.Vector2(dx, dy).normalize()
        if max_speed != None:
            self.speed = random.uniform(0.5, max_speed)
        elif speed != None:
            self.speed = speed
    
    def do_intersect(self, line1_start, line1_end, line2_start, line2_end):
        """
        This methode proofs if 2 lines has a intersection point.
        
        :param self: Description
        :param line1_start: Description
        :param line1_end: Description
        :param line2_start: Description
        :param line2_end: Description
        """
        if line1_start.x == line1_end.x:
            return (line1_start.x >= line2_start.x and line1_start.x <= line2_end.x) or (line1_start.x <= line2_start.x and line1_start.x >= line2_end.x)
        if line2_start.x == line2_end.x:
            return (line2_start.x >= line2_start.x and line2_start.x <= line2_end.x) or (line2_start.x <= line2_start.x and line2_start.x >= line2_end.x)


        m1 = (line1_start.y - line1_end.y) / (line1_start.x - line1_end.x)
        b1 = line1_start.y - m1 * line1_start.x
        m2 = (line2_start.y - line2_end.y) / (line2_start.x - line2_end.x)
        b2 = line2_start.y - m2 * line2_start.x

        if m1 == m2 :
            return b1 == b2

        intersection_x = (b2 - b1) / (m1 - m2)

        is_in_line1 = (intersection_x >= line1_start.x and intersection_x <= line1_end.x) or (intersection_x <= line1_start.x and intersection_x >= line1_end.x)
        is_in_line2 = (intersection_x >= line2_start.x and intersection_x <= line2_end.x) or (intersection_x <= line2_start.x and intersection_x >= line2_end.x)

        return is_in_line1 and is_in_line2
