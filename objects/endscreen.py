import pygame
from objects.text import Text

class Endscreen:
    """
    Class representing the endscreen: shows "GAME OVER", score and allows player to give a name 
        Attributes:
            width: width of the screen
            height: height of the screen
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.game_over = Text("GAME OVER", 45, "white", width*.5, height*.25)
        self.enter_name = Text("Enter your NAME:", 40, "white", width*.5, height*.38)
        self.player_name = Text("", 50, "white", width*.5, height*.5)
        


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "leaderboard"
        
        self.player_name.input_text(event)
        
        return None
        
    
    def draw(self, surface):
        self.game_over.draw(surface)
        self.enter_name.draw(surface)
        self.player_name.draw(surface)
        