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

    def sort_by_state(self):
        CensusAnalyser.__data_list.sort_values(by=[IndiaCensusCSV().state], inplace=True)
        return CensusAnalyser.__data_list.to_json(orient='records')

    def sort_by_stateCode(self):
        CensusAnalyser.__data_list.sort_values(by=StateCodeCSV().state_code, inplace=True)
        return CensusAnalyser.__data_list.to_json(orient='records')

    def sort_by_population(self):
        CensusAnalyser.__data_list.sort_values(by=[IndiaCensusCSV().population], inplace=True, ascending=False)
        return CensusAnalyser.__data_list.to_json(orient='records')

    def sort_by_density(self):
        CensusAnalyser.__data_list.sort_values(by=[IndiaCensusCSV().density], inplace=True, ascending=False)
        return CensusAnalyser.__data_list.to_json(orient="records")

    def sort_by_area(self):
        CensusAnalyser.__data_list.sort_values(by=[IndiaCensusCSV().area], inplace=True, ascending=False)
        return CensusAnalyser.__data_list.to_json(orient="records")
