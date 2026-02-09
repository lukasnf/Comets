import pygame
import objects.highscore as Highscore
import objects.text as Text



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

        self.hs = Highscore()
        self.hs.load_highscore()

        df_sorted = self.hs.df.sort_values(by=["Score", "Date"], ascending = False)

        self.top5 = df_sorted.head(5)

        self.lines = []
        y = 180

        for _, row in self.top5.iterrows():
            name = row["Player Name"]
            score = row["Score"]
            date = row["Date"]

            line = Text(f"{name}   -   {score}   -   {date}", 
                        40, "white", width * 0.5, y)
            self.lines.append(line)
            y += 60



    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "return_to_title"
        return None
    
    def draw(self, surface):
        self.top_scores.draw(surface)
        self.press_key.draw(surface)
        for line in self.lines:
            line.draw(surface)
        