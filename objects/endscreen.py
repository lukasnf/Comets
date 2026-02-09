import pygame
from objects.text import Text

class Endscreen:
    """"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.game_over = Text("GAME OVER", 45, "white", width*.5, height*.25)
        self.enter_name = Text("Enter your NAME:", 40, "white", width*.5, height*.38)
        self.player_name = Text("", 50, "white", width*.5, height*.5)


    def handle_event(self, event):
        
        self.player_name.input_text(event)
        
        return "endscreen"
    
    def draw(self, surface):
        self.game_over.draw(surface)
        self.enter_name.draw(surface)
        self.player_name.draw(surface)
        