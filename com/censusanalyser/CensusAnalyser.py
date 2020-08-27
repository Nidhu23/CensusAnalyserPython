import json

from com.censusanalyser.CsvLoader import *
from com.censusanalyser.CsvEnum import *


class CensusAnalyser:
    def __init__(self, dto_object):
        self.__data_list = pd.DataFrame()
        self.dto = dto_object

    def record_counter(self, path):
        self.__data_list = CsvLoader.load_census_data(path, self.dto)
        return len(self.__data_list)

    def state_code_record_counter(self, path_one, path_two):
        self.__data_list = CsvLoader.load_state_data(path_one, path_two, CsvDTOType.india_census)
        return len(self.__data_list)

    def sort_by_state(self):
        self.__data_list.sort_values(by=[self.dto.value.state], inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_state_code(self):
        self.__data_list.sort_values(by=StateCodeCSV().state_code, inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_population(self):
        self.__data_list.sort_values(by=[self.dto.value.population], inplace=True, ascending=False)
        return self.__data_list.to_json(orient='records')

    def sort_by_density(self):
        self.__data_list.sort_values(by=[self.dto.value.density], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")

    def sort_by_area(self):
        self.__data_list.sort_values(by=[self.dto.value.area], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")


