from com.censusanalyser.CsvLoader import *


class CensusAnalyser:
    def __init__(self):
        self.__data_list = pd.DataFrame()

    def census_record_counter(self, path):
        self.__data_list = CsvLoader.load_census_data(path)
        return len(self.__data_list)

    def state_code_record_counter(self, path_one, path_two):
        self.__data_list = CsvLoader.load_state_data(path_one, path_two)
        return len(self.__data_list)

    def sort_by_state(self):
        self.__data_list.sort_values(by=[IndiaCensusCSV().state], inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_state_code(self):
        self.__data_list.sort_values(by=StateCodeCSV().state_code, inplace=True)
        return self.__data_list.to_json(orient='records')

    def sort_by_population(self):
        self.__data_list.sort_values(by=[IndiaCensusCSV().population], inplace=True, ascending=False)
        return self.__data_list.to_json(orient='records')

    def sort_by_density(self):
        self.__data_list.sort_values(by=[IndiaCensusCSV().density], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")

    def sort_by_area(self):
        self.__data_list.sort_values(by=[IndiaCensusCSV().area], inplace=True, ascending=False)
        return self.__data_list.to_json(orient="records")

