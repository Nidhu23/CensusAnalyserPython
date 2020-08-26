from com.censusanalyser.CensusAnalyser import CsvLoader
import pytest
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError

CENSUS_CSV_FILE_PATH = r"C:\Users\USER\IdeaProjects\CensusAnalyserPython\com.censusanalyser.testing\resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testing\resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"C:\Users\USER\IdeaProjects\CensusAnalyserPython\com.censusanalyser.testing\resources\IndiaStateCensusData.txt"
CENSUS_CSV_FILE_WRONG_DELIMITER = r"C:\Users\USER\IdeaProjects\CensusAnalyserPython\com.censusanalyser.testing\resources\IndianCensusWrongDelimeter.csv"


def test_record_counter():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29


def test_record_counter_exception_given_wrong_file_path():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.record_counter()


def test_record_counter_exception_given_wrong_file_type():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.record_counter()


def test_record_counter_exception_given_file_with_wrong_delimiter():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.record_counter()
