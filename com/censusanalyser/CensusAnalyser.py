import pandas as pd
from com.censusanalyser.CsvLoader import *


class CensusAnalyser:
    __data_list = pd.DataFrame()

    def __init__(self, path):
        self.path = path

    def census_record_counter(self):
        CensusAnalyser.__data_list = CsvLoader.load_census_data(self.path)
        return len(CensusAnalyser.__data_list)

    def state_code_record_counter(self):
        CensusAnalyser.__data_list = CsvLoader.load_state_data(self.path)
        return len(CensusAnalyser.__data_list)
