import pandas as pd
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError


class CsvLoader:
    def __init__(self, path):
        self.path = path

    def record_counter(self):
        try:
            census_list = pd.read_csv(self.path).values.tolist()
            return len(census_list)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
