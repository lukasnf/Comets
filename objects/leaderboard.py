import pygame
import objects.highscore as hs
import text as Text



class Leaderboard:
    """
    Class representing a screen for the leaderboard. Screen contains text and top 5 scores

        Class Attributes:
            width: width of the gamescreen
            height: height of the gamescreen
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.top_scores = Text("Top scores:", 50, "white", width*.5, height*.1)
        self.press_key = Text("Press ENTER to return", 50, "white", width*.5, height*.73)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "return to title"
        return None
    
    def draw(self, surface):
        self.top_scores.draw(surface)
        self.press_key.draw(surface)
        