import pygame
from objects import flying_object
from objects import projectile


class Ufo_Handler:
    """
    Manages spawning, movement, and collision of the UFO.

    Attributes:
        window_width (int): width of the window
        window_height (int):  height of the window
        time (int): timestamp of the last UFO spawn in milliseconds
        period (int): Cooldown duration between UFO spawns in milliseconds
        ufo (Ufo): active UFO instance
        max_speed (int): Base speed value used for new UFO instances.
    """

    def __init__(self, window_width, window_height, period_s):
        """
        Initializes the UFO handler with screen dimensions and spawn timing.

        Parameters:
            window_width (int): width of the window
            window_height (int): height of the window
            period_s (int): Wait time between UFO appearances in seconds
        """
        self.window_width = window_width
        self.window_height = window_height
        self.time = pygame.time.get_ticks()
        self.period = period_s * 1000 # in ms
        self.ufo = None
        self.max_speed = 3
        self.generate_ufo()

    def check_period(self):
        """
        Spawns a new UFO after the cooldown perios.
        
        Parameters:
            None

        Return:
            None
        """
        if self.ufo == None and pygame.time.get_ticks() - self.time > self.period:
            self.generate_ufo()
            self.time = pygame.time.get_ticks()

    def move_ufo(self):
        """
        Updates UFO position and removes it if it is outside the window.

        Parameters:
            None

        Retrun:
            None
        """
        if ((self.ufo.pos[0] <= -Ufo.width and self.ufo.direction[0] < 0) 
            or (self.ufo.pos[0] >= self.window_width and self.ufo.direction[0] > 0)
            or (self.ufo.pos[1] <= -Ufo.height and self.ufo.direction[1] < 0)
            or (self.ufo.pos[1] >= self.window_height and self.ufo.direction[1] > 0)):
            self.ufo = None
            self.time = pygame.time.get_ticks()
        else:
            self.ufo.move()

    def draw_ufo(self, surface):
        """
        Draws the ufo on the surface.

        Parameter:
            surface (pygame surface): the surface of the window

        Return:
            None
        """
        self.ufo.draw(surface)

    def ufo_down_shooting(self, bullets):
        """
        Proofs if a bullet hits the ufo

        Parameter:
            bullets (list of projectile): list of all flying bullets in the current window

        Return:
            None
        """
        if self.ufo.check_collision(bullets):
            self.ufo = None
            self.time = pygame.time.get_ticks()

    def generate_ufo(self):
        """
        generates a new ufo.

        Parameter:
            None
        Return:
            None
        """
        self.ufo = Ufo(self.window_height, self.window_width, self.max_speed) 

    def generate_projectile(self, aim):
        """
        generates a projectile, which flies form the Ufo to given aim

        Parameter:
            aim (Spaceship): the space in the game

        Return:
            the projectile
        """
        return projectile.Projectile(self.ufo.get_center(), pygame.math.Vector2.normalize(aim.center() - self.ufo.pos), self.ufo.speed * 2, "ufo", color="green")



class Ufo(flying_object.Flying_Object):

    """
    The ufo in the game, which shoots the spaceship.

    heritage: Flying_Object

    Attributes:
        color_metal (string): name of the color which covers the shield
        color_glass (string): name of the color of the glass dome
        time (int): the last moment of a shoot
        cooldown_start (int): cooldown at the beginning of the game. It decreases with the score

    Classattributes:
        width (int): the width of all ufos
        height (int): the height of all ufos
    """
    
    width = 70 
    height = 30

    def __init__(self, window_width, window_height, speed, cooldown=1000):
        """
        Initializes the ufo

        Parameters:
            window_width (int): width of the window
            window_height (int): height of the window
            speed (float): the speed of the ufo

        Returns:
            None
        """
        self.color_metal = "darkgrey"
        self.color_glass = "aqua"
        self.time = pygame.time.get_ticks()
        self.cooldown_start = cooldown
        flying_object.Flying_Object.__init__(self)
        flying_object.Flying_Object.generate_random_border_startpos(self, Ufo.width, Ufo.height, window_width, window_height, speed=speed)

    def get_center(self):
        """
        gets the center of the Ufo

        Parameters:
            None
        
        Return:
            the center as a pygame.math.Vector2
        """
        return pygame.math.Vector2(self.pos.x + Ufo.width/2, self.pos.y + Ufo.height/2)

    def shoot(self, score):
        """
        Proofs if enough time has passed to shoot again. It depends on the current score.

        Parameters:
            score (int): the score of the running game

        Return
            whether enough time has passed.
        """
        if pygame.time.get_ticks() > self.time + self.cooldown_start - (score // 10) :
            self.time = pygame.time.get_ticks()
            return True
        return False
    
    def check_collision(self, bullets):
        """
        Proofs if the ship is hit by a bullet. Ufo uses a cross as a hitbox.
        
        Parameters:
            bullets (list): the list of bullets in the game

        Return:
            if the ship is hit by a bullet or not
        """
        ufo_lines = [[self.pos + pygame.math.Vector2([0, Ufo.height*(2/3)]), self.pos + pygame.math.Vector2([Ufo.width, Ufo.height*(2/3)])],[self.pos + pygame.math.Vector2([Ufo.width/2, 0]), self.pos + pygame.math.Vector2([Ufo.width/2, Ufo.height])]]
        for bullet in bullets:
            if any(self.do_intersect(ufo_line[0], ufo_line[1], bullet.pos, bullet.pos + bullet.direction * bullet.speed) for ufo_line in ufo_lines):
                return True

        
    def draw(self, surface):
        """
        draws the ufo with to ellipses on the surface.
        
        Parameter:
            surface (pygame surface): the surface on the window

        Return:
            None
        """
        rect_metal_shield = pygame.Rect(self.pos[0], self.pos[1] + int(Ufo.height / 3), Ufo.width, int(2 * Ufo.height / 3))
        rect_glass_dome = pygame.Rect(self.pos[0] + int(Ufo.width / 3), self.pos[1], int(Ufo.width / 3), int(2 * Ufo.height / 3))
        pygame.draw.ellipse(surface, pygame.Color(self.color_glass), rect_glass_dome)
        pygame.draw.ellipse(surface, pygame.Color(self.color_metal), rect_metal_shield)

