import pytest
from loader import load_data
from reports.average_gdp import AverageGDPReport


# Fixture для тестовых данных
@pytest.fixture
def sample_data():
    return [
        {
            "country": "USA",
            "year": "2023",
            "gdp": 25000,
            "gdp_growth": "2.0",
            "inflation": "3.5",
            "unemployment": "3.7",
            "population": "339",
            "continent": "North America",
        },
        {
            "country": "USA",
            "year": "2022",
            "gdp": 23000,
            "gdp_growth": "2.1",
            "inflation": "8.0",
            "unemployment": "3.6",
            "population": "338",
            "continent": "North America",
        },
        {
            "country": "China",
            "year": "2023",
            "gdp": 18000,
            "gdp_growth": "5.2",
            "inflation": "2.5",
            "unemployment": "5.2",
            "population": "1425",
            "continent": "Asia",
        },
    ]

def test_average_gdp(sample_data):
    report = AverageGDPReport()
    result = report.build(sample_data)

    assert result[0]["country"] == "USA"
    assert result[0]["average_gdp"] == 24000

@pytest.mark.parametrize(
    "rows,expected",
    [
        (
            [{"country": "A", "gdp": 10}, {"country": "A", "gdp": 20}],
            [{"country": "A", "average_gdp": 15}],
        ),
        (
            [{"country": "B", "gdp": 5}, {"country": "B", "gdp": 15}],
            [{"country": "B", "average_gdp": 10}],
        ),
    ],
)
def test_average_gdp_param(rows, expected):
    report = AverageGDPReport()
    result = report.build(rows)

    assert result[0]["average_gdp"] == expected[0]["average_gdp"]