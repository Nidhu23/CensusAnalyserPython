import json

from com.censusanalyser.CsvLoader import *
from com.censusanalyser.CsvEnum import *


# Class with method returns object of different Dto's based on the number of files
class ObjectCreator:
    def object_creator(*path):
        if len(path) == 1:
            return CsvDTOType.us_census
        if len(path) > 1:
            return CsvDTOType.india_census


# Class that performs operation on the data frame and returns corresponding result

class CensusAnalyser:
    dto_object = None

    def __init__(self):
        self.__data_list = pd.DataFrame()

    def record_counter(self, *path):
        CensusAnalyser.dto_object = ObjectCreator.object_creator(*path)
        self.__data_list = CsvLoader.load_census_data(CensusAnalyser.dto_object, *path)
        return len(self.__data_list)

    def state_code_record_counter(self, *path):
        CensusAnalyser.dto_object = ObjectCreator.object_creator(*path)
        self.__data_list = CsvLoader.load_state_data(CensusAnalyser.dto_object, *path)
        return len(self.__data_list)

    def sort_by_state(self):
        self.__data_list.sort_values(by=[CensusAnalyser.dto_object.value.state], inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_state_code(self):
        self.__data_list.sort_values(by=StateCodeCSV().state_code, inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_population(self):
        self.__data_list.sort_values(by=[CensusAnalyser.dto_object.value.population], inplace=True, ascending=False)
        return self.__data_list.to_json(orient='records')

    def sort_by_density(self):
        self.__data_list.sort_values(by=[CensusAnalyser.dto_object.value.density], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")

    def sort_by_area(self):
        self.__data_list.sort_values(by=[CensusAnalyser.dto_object.value.area], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")

    def max_density_finder(self):
        state_names = self.sort_by_density()
        states_dict = json.loads(state_names)
        return states_dict[0][CensusAnalyser.dto_object.value.state]
