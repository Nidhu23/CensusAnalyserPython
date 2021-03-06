import json

import pytest

from com.censusanalyser.CensusAnalyser import CensusAnalyser
from com.censusanalyser.CensusAnalyserError import CensusAnalyserError
from com.censusanalyser.CsvEnum import *

CENSUS_CSV_FILE_PATH = r"resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testing\resources\IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"resources\IndiaStateCensusData.txt"
CENSUS_CSV_FILE_WRONG_DELIMITER = r"resources\IndianCensusWrongDelimeter.csv"
STATE_CODE_CSV_FILE_PATH = r"resources\IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_PATH = r"com.censusanalyser.testingresources\IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_TYPE = r"resources\IndiaStateCode.gif"
STATE_CODE_CSV_FILE_WRONG_DELIMITER = r"resources\IndiaStateCodeWrongDelimiter.csv"
US_CENSUS_CSV_FILE_PATH = r"resources\USCensusData.csv"


def test_givenIndiaCensusCSVFile_WhenCounted_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser()
    assert census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH) == 29


def test_givenIndiaCensusAndStateCodeCSVFile_WhenWrongPath_ShouldRaiseException():
    census_analyser = CensusAnalyser()
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.record_counter(CENSUS_CSV_FILE_WRONG_PATH, STATE_CODE_CSV_FILE_WRONG_TYPE)


def test_givenIndiaCensusCSVFile_WhenWrongFileType_ShouldRaiseException():
    census_analyser = CensusAnalyser()
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.record_counter(CENSUS_CSV_FILE_WRONG_TYPE, STATE_CODE_CSV_FILE_WRONG_TYPE)


def test_givenIndiaCensusCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser()
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.record_counter(CENSUS_CSV_FILE_WRONG_DELIMITER, STATE_CODE_CSV_FILE_WRONG_DELIMITER)


def test_givenIndiaCensusCSVFile_WhenHeadersWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser()
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.record_counter(STATE_CODE_CSV_FILE_PATH, CENSUS_CSV_FILE_PATH)


def test_givenStateCodeCSVFile_WhenLoaded_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser()
    assert census_analyser.state_code_record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH) == 29


def test_givenCensusCSVFile_WhenSortedByState_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_state()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["State"] == "Andhra Pradesh"


def test_givenStateCodeCSVFile_WhenSortedByStateCode_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.state_code_record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_state_code()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["StateCode"] == "AP"


def test_givenCensusCSVFile_WhenSortedByPopulation_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_population()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["Population"] == 199812341


def test_givenCensusCSVFile_WhenSortedByDensity_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_density()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["DensityPerSqKm"] == 1102


def test_givenCensusCSVFile_WhenSortedByArea_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_area()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["AreaInSqKm"] == 342239


def test_givenUSCensusCSVFile_WhenLoaded_ShouldReturnRecordCount():
    census_analyser = CensusAnalyser()
    assert census_analyser.record_counter(US_CENSUS_CSV_FILE_PATH) == 51


def test_givenUSCensusCSVFile_WhenSortedByPopulation_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(US_CENSUS_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_population()
    sorted_dict = json.loads(sorted_json)
    assert sorted_dict[0]["Population"] == 37253956


def test_givenUSCensusCSVFile_WhenSortedByDensity_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(US_CENSUS_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_density()
    sorted_dict = json.loads(sorted_json)
    assert sorted_dict[0]["Population Density"] == 3805.61


def test_givenUSCensusCSVFile_WhenSortedByArea_ShouldReturnSortedResult():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(US_CENSUS_CSV_FILE_PATH)
    sorted_json = census_analyser.sort_by_area()
    json_dict = json.loads(sorted_json)
    assert json_dict[0]["Total area"] == 1723338.01


def test_givenCensusCSVFile_WhenSorted_ShouldReturnStateWithMaxDensity():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH)
    state = census_analyser.max_density_finder()
    assert state == "Bihar"


def test_givenUSCensusCSVFile_WhenSorted_ShouldReturnStateWithMaxDensity():
    census_analyser = CensusAnalyser()
    census_analyser.record_counter(US_CENSUS_CSV_FILE_PATH)
    state = census_analyser.max_density_finder()
    assert state == "District of Columbia"
