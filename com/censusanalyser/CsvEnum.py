import enum
from com.censusanalyser.CensusCSV import *


# enum class to return instance of particular class according to user choice
class CsvDTOType(enum.Enum):
    india_census = IndiaCensusCSV()
    us_census = USCensusCSV()


"""class SortByOption(enum.Enum):
    State = "state"
    Area = "area"
    Population = "population"
    Density = "density"
    StateCode = "state_code"""
