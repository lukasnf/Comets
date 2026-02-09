

class Flying_Object:
    """
    This is a general object in space.

    Attributes:
        pos (pygame.math.Vector2): The position of the object in space.
        direction (pygame.math.Vector2): The direction of motion in space.
        speed (int): The speed of the object.
    """


    def __init__(self, pos, direction, speed):
        self.pos = pos
        self.direction = direction
        self.speed = speed

    def move(self):
        """
        Move the Object based on its direction and speed. It is moved in a direction scaled by speed.
        """
        self.pos = self.pos + self.direction * self.speed