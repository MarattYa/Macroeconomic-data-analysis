from typing import TypedDict


class CountryRow(TypedDict):
    country: str
    year: str
    gdp: float
    gdp_growth: str
    inflation: str
    unemployment: str
    population: str
    continent: str
