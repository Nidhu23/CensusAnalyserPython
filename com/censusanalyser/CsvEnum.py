import enum
from com.censusanalyser.CensusCSV import *


class CsvDTOType(enum.Enum):
    india_census = IndiaCensusCSV()
    us_census = USCensusCSV()
