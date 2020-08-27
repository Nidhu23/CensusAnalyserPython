import pandas as pd
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
from com.censusanalyser.IndiaCensusCSV import IndiaCensusCSV, StateCodeCSV


class CsvLoader:
    @staticmethod
    def load_census_data(path):
        try:
            census_col_list = repr(IndiaCensusCSV()).split(",")
            census_list = pd.read_csv(path, sep=",", usecols=census_col_list)
            return census_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")

    @staticmethod
    def load_state_data(path_one, path_two):
        try:
            census_list = CsvLoader.load_census_data(path_one)
            state_col_list = repr(StateCodeCSV()).split(",")
            state_list = pd.read_csv(path_two, usecols=state_col_list)
            combined_list = census_list.merge(state_list, on="State")
            return combined_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")


