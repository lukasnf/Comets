import pygame
import objects.text as Text

class Titlescreen:
    """
    Docstring for Titlescreen
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.title = Text("ASTEROIDS", 80, "white", width*0.5, height*0.35)
        self.press_key = Text("Press ENTER to START game", 40, "white", width*0.5, height*0.66)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "start_game"

    
    def draw(self, surface):
        self.title.draw(surface)
        self.press_key.draw(surface)
        