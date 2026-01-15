import pandas as pd
from datetime import date

class Highscore():
    """
    Class to implement the highscore for asteroids
    """

    def __init__(self, highscore_path="./highscores/highscores.csv", columns = ["Player Name", "Score", "Date"]):
        """
        highscore_path: Path to save the highscores file
        columns: columns of the highscore file
        """
        self.highscore_path = highscore_path
        self.columns = columns

    def load_highscore(self):
        try:
            self.df = pd.read_csv(self.highscore_path)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=self.columns)

    def write_highscore(self, player_name, player_score):
        current_date = date.today()
        length_of_df = len(self.df)
        self.df.loc[length_of_df] = [player_name, player_score, current_date]

    def show_highscores(self):
        print(self.df.sort_values(by=["Score", "Date"], ascending=False))

    def save_highscore(self):
        self.df.to_csv(self.highscore_path, index=False)

highscore = Highscore()
highscore.load_highscore()
highscore.write_highscore("Mustermann", 235092)
highscore.write_highscore("Max", 100)
highscore.write_highscore("Unbekannt", 50)
highscore.show_highscores()
#print(highscore.df)
highscore.save_highscore()