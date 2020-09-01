import pandas as pd
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
from com.censusanalyser.CsvEnum import *


# Class that loads data from CSV file to data frame
class CsvLoader:
    @staticmethod
    def load_census_data(census_object, *path):
        try:
            if isinstance(census_object, CsvDTOType):
                census_col_list = repr(census_object.value).split(",")
                census_list = pd.read_csv(path[0], sep=",", usecols=census_col_list)
                return census_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")
        except TypeError:
            raise CensusAnalyserError("The class object given is wrong")

    @staticmethod
    def load_state_data(census_object, *path):
        try:
            census_list = CsvLoader.load_census_data(census_object, path[0])
            state_col_list = repr(StateCodeCSV()).split(",")
            state_list = pd.read_csv(path[1], usecols=state_col_list)
            combined_list = census_list.merge(state_list, on="State")
            return combined_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")
