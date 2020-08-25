import pandas as pd


class CsvLoader:
    def __init__(self, path):
        self.path = path

    def record_counter(self):
        census_list = pd.read_csv(self.path).values.tolist()
        return len(census_list)
