import pandas as pd
class Data:
    def __init__(self):
        self.titanic_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
        self.df = pd.read_csv(self.titanic_dataset)
    def data(self):
        return self.df
