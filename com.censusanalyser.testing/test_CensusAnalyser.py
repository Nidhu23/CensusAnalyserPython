from com.censusanalyser.CensusAnalyser import CsvLoader
import pytest
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError

CENSUS_CSV_FILE_PATH = r"resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testing\resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"resources\IndiaStateCensusData.txt"
CENSUS_CSV_FILE_WRONG_DELIMITER = r"resources\IndianCensusWrongDelimeter.csv"
StateCode_CSV_FILE_PATH = r"resources\IndiaStateCode.csv"


def test_givenIndiaCensusCSVFile_WhenCounted_ShouldReturnRecordsCount():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.load_census_data() == 29


def test_givenIndiaCensusCSVFile_WhenWrongPath_ShouldRaiseException():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.load_census_data()


def test_givenIndiaCensusCSVFile_WhenWrongFileType_ShouldRaiseException():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.load_census_data()


def test_givenIndiaCensusCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    csv_loader = CsvLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert csv_loader.load_census_data()


def test_givenStateCodeCSVFile_WhenLoaded_ShouldReturnRecordsCount():
    csv_loader = CsvLoader(StateCode_CSV_FILE_PATH)
    assert csv_loader.load_state_data() == 37
