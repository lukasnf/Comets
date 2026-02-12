import pygame
from objects.text import Text

class Titlescreen:
    """
    Class representing titlescreen: shows you name of game, allows player to go to leaderboard or game
        Attributes:
            width: width of screen
            height: height of screen
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.title = Text("ASTEROIDS", 80, "white", width*0.5, height*0.35)
        self.press_key_start = Text("Press ENTER to START game", 40, "white", width*0.5, height*0.66)
        self.press_key_score = Text("Press SPACE to see HIGHSCORES", 40, "white", width*0.5, height*0.83)
   
   
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "play"
            if event.key == pygame.K_SPACE:
                return "leaderboard"

    
    def draw(self, surface):
        self.title.draw(surface)
        self.press_key_start.draw(surface)
        self.press_key_score.draw(surface)
        