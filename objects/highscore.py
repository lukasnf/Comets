import pandas as pd
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
HIGHSCORE_DIR = BASE / "highscores"

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

        self.highscore_path = HIGHSCORE_DIR / "highscores.csv"

    def load_highscore(self):
        #Method to read the csv
        try:
            self.df = pd.read_csv(self.highscore_path)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=self.columns)
            print(FileNotFoundError)

    def save_highscore(self):
        #saves new score on the csv
        self.df.to_csv(self.highscore_path, index=False)

    def write_highscore(self, player_name, player_score):
        #writes new score on the csv
        current_date = date.today()
        length_of_df = len(self.df)
        self.df.loc[length_of_df] = [player_name, player_score, current_date]
        self.save_highscore()

    def show_highscores(self):
        print(self.df.sort_values(by=["Score", "Date"], ascending=False))


if __name__ == "__main__":
    highscore = Highscore()
    highscore.load_highscore()
    highscore.write_highscore("Mustermann", 235092)
    highscore.write_highscore("Max", 100)
    highscore.write_highscore("Unbekannt", 50)
    highscore.show_highscores()
    #print(highscore.df)
    #highscore.save_highscore()