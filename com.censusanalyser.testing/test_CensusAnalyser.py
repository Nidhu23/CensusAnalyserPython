from com.censusanalyser.CensusAnalyser import CensusAnalyser
import pytest
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
import json

CENSUS_CSV_FILE_PATH = r"resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testing\resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"resources\IndiaStateCensusData.txt"
CENSUS_CSV_FILE_WRONG_DELIMITER = r"resources\IndianCensusWrongDelimeter.csv"
STATE_CODE_CSV_FILE_PATH = r"resources\IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testingresources\IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_TYPE = r"resources\IndiaStateCode.gif"
STATE_CODE_CSV_FILE_WRONG_DELIMITER = r"resources\IndiaStateCodeWrongDelimiter.csv"


def test_givenIndiaCensusCSVFile_WhenCounted_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    assert census_analyser.census_record_counter() == 29


def test_givenIndiaCensusCSVFile_WhenWrongPath_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenWrongFileType_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenHeadersWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenStateCodeCSVFile_WhenLoaded_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_PATH)
    assert census_analyser.state_code_record_counter() == 37


def test_givenStateCodeCSVFile_WhenPathWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenFileTypeWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenHeadersWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenCensusCSVFile_WhenSortedByState_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    census_analyser.census_record_counter()
    sorted_json = census_analyser.sort_by_state()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["State"] == "Andhra Pradesh"


def test_givenStateCodeCSVFile_WhenSortedByStateCode_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_PATH)
    census_analyser.state_code_record_counter()
    sorted_json = census_analyser.sort_by_stateCode()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["StateCode"] == "AD"


def test_givenCensusCSVFile_WhenSortedByPopulation_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    census_analyser.census_record_counter()
    sorted_json = census_analyser.sort_by_population()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["Population"] == 199812341


def test_givenCensusCSVFile_WhenSortedByDensity_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    census_analyser.census_record_counter()
    sorted_json = census_analyser.sort_by_density()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["DensityPerSqKm"] == 1102


def test_givenCensusCSVFile_WhenSortedByArea_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    census_analyser.census_record_counter()
    sorted_json = census_analyser.sort_by_area()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["AreaInSqKm"] == 342239
