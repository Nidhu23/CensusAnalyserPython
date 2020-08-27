class IndiaCensusCSV:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.density + "," + self.area


class StateCodeCSV:
    def __init__(self):
        self.state = "State"
        self.state_code = "StateCode"

    def __repr__(self):
        return self.state + "," + self.state_code


class USCensusCSV:
    def __init__(self):
        self.state = "State"
        self.state_code = "State Id"
        self.area = "Total area"
        self.population = "Population"
        self.density = "Population Density"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.density + "," + self.area + "," + self.state_code
