

class Flying_Object:

    def __init__(self, pos, direction, speed):
        self.pos = pos
        self.direction = direction
        self.speed = speed

    def move(self):
        """
        Move the asteroid based on its direction and speed. It is moved in the direction of (dx, dy) scaled by speed.
        """
        #self.x = self.x + self.dx * self.speed
        #self.y = self.y + self.dy * self.speed
        self.pos = self.pos + self.direction * self.speed