from com.censusanalyser.CensusAnalyser import CsvLoader

CENSUS_CSV_FILE_PATH = r"C:\Users\USER\IdeaProjects\CensusAnalyserPython\com.censusanalyser.testing\resources\IndiaStateCensusData.csv"


def test_record_counter():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29
