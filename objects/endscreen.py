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
        self.victory_text = Text("Well played!", 45, "white", width*.5, height*.25)
        self.enter_name = Text("Enter your NAME:", 40, "white", width*.5, height*.38)
        self.player_name = Text("", 50, "white", width*.5, height*.5)
        self.warning_text = Text("NAME is too long!", 40, "red", width*.5, height*.7 )
        


    def handle_event(self, event):
        #Method to give return if certain keys are pressed.
        #Pressed key gives return that changes state for state machine
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "leaderboard"
        
        self.player_name.input_text(event)  #will get input of user for nameinput
        
    def draw_victory_screen(self, surface):
        self.victory_text.draw(surface)
        self.enter_name.draw(surface)
        self.player_name.draw(surface)
        if self.player_name.warning:
            self.warning_text.draw(surface)
    
    def draw(self, surface):
        #Method to draw the endscreen
        self.game_over.draw(surface)
        self.enter_name.draw(surface)
        self.player_name.draw(surface)
        if self.player_name.warning:
            self.warning_text.draw(surface)
        