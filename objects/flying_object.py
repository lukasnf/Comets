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
        Initialize the object's physical properties.
        
        Parameters:
            pos (pygame.math.Vector2): The position of the object in space.
            direction (pygame.math.Vector2): The direction of motion in space.
            speed (int): The speed of the object.
        """
        self.pos = pos
        self.direction = direction
        self.speed = speed

    def move(self):
        """
        Move the Object based on its direction and speed. It is moved in a direction scaled by speed.

        Parameter:
            None

        Return:
            None
        """
        self.pos = self.pos + self.direction * self.speed

    def generate_random_border_startpos(self, object_width, object_height, window_width, window_height, max_speed=None, speed=None):
        """
        Spawn the object at a random window border with an inward trajectory.

        Parameters:
            object_width (float): 
            object_height (float):
            window_width (int): the size of the window
            window_height (int): the size of the window
            max_speed (float): if the speed is not given, the speed is a will be a random value between 0.5 and max_speed
            speed (float): the speed of the new object
        
        Retrun:
            None
        """
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
    

    def do_intersect(self, p1, p2, p3, p4):
        """
        Check if line1 (p1, p2) intersects with segment (p3, p4) using cross products.

        Parameters:
            p1 (float): The startposition of line1.
            p2 (float): The endposition of line1.
            p3 (float): The startposition of line2.
            p4 (float): The endposition of the line2.

        Return:
            Ture if line1 and line2 intersect.
        """
        def cross_product(A, B, C):
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
    
        return (cross_product(p1, p3, p4) != cross_product(p2, p3, p4) and 
                cross_product(p1, p2, p3) != cross_product(p1, p2, p4))

