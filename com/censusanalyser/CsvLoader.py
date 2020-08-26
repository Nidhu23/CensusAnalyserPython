import pandas as pd
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
from com.censusanalyser.IndiaCensusCSV import IndiaCensusCSV, StateCodeCSV


class CsvLoader:
    def __init__(self, path):
        self.path = path

    def load_census_data(self):
        try:
            census_col_list = repr(IndiaCensusCSV()).split(",")
            census_list = pd.read_csv(self.path, usecols=census_col_list)
            return len(census_list)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")

    def load_state_data(self):
        try:
            state_col_list = repr(StateCodeCSV()).split(",")
            state_list = pd.read_csv(self.path, usecols=state_col_list)
            return len(state_list)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")
