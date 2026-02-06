import pygame
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
FONT_DIR = BASE / "fonts"

class Text:
        """
        Class representing text on the screen. Text can't interact directly with the screen.

        Class atributes:
            text_size: size of the text
            text_font: font of the text
            text_color: color of the text
            text_x: x coordinate of the text
            text_y: y coordinate of the text
        """

        def __init__(self, text_text, text_size, text_color, text_x, text_y):
            self.text_text = text_text
            self.text_size = text_size
            self.text_color = text_color
            self.text_x = text_x
            self.text_y = text_y
            text_path = FONT_DIR / "Arcade.ttf"
            self.text_font = pygame.font.Font(text_path, text_size)

            self.render()
            
            

        def render(self):
            self.surface = self.text_font.render(self.text_text, True, self.text_color)
            self.rect = self.surface.get_rect(center=(self.text_x, self.text_y))

        def set(self, new_text):
            self.text_text = new_text
            self.render()

        def draw(self, screen):
            #Method to write text on the screen
            screen.blit(self.surface, self.rect)
            
        def update_text(self):
            #Method to update text if change is needed. This is going to be used for the score and for user input
            self.surface = self.text_font.render(self.text_text, True, self.text_color) 

        def input_text(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text_text = self.text_text[:-1]     #deletes last character if backspace is pressed
                
                elif event.key == pygame.K_RETURN:
                    print("Eingabe abgeschlossen", self.text_text) #finishes user input if enter is pressed

                else: 
                    self.text_text += event.unicode

                self.update_text()              #updates the text, change will be seen on the text

