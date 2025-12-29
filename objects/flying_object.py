

class Flying_Object:
    """
    This is a generall object in space.

    Attributes:
        pos (pygame.math.Vector2): The position of the object in space.
        direction (pygame.math.Vector2): The dircetion of motion in space.
        speed (int): The speed  of the object.
    """


    def __init__(self, pos, direction, speed):
        self.pos = pos
        self.direction = direction
        self.speed = speed

    def move(self):
        """
        Move the asteroid based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        self.pos = self.pos + self.direction * self.speed