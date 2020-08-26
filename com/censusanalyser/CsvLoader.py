import pandas as pd
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
from com.censusanalyser.IndiaCensusCSV import IndiaCensusCSV, StateCodeCSV


class CsvLoader:
    @staticmethod
    def load_census_data(path):
        try:
            census_col_list = repr(IndiaCensusCSV()).split(",")
            census_list = pd.read_csv(path, usecols=census_col_list)
            return census_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")

    @staticmethod
    def load_state_data(path):
        try:
            state_col_list = repr(StateCodeCSV()).split(",")
            state_list = pd.read_csv(path, usecols=state_col_list)
            return state_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")
