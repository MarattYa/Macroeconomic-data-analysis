from reports.average_gdp import AverageGDPReport

def test_average_gdp_report():
    rows = [
        {"country": "A", "gdp": 10},
        {"country": "A", "gdp": 20},
        {"country": "B", "gdp": 30},
    ]

    report = AverageGDPReport()
    result = report.build(rows)

    assert result[0]["country"] == "B"
    assert result[0]["average_gdp"] == 30
    assert result[1]["country"] == "A"
    assert result[1]["average_gdp"] == 15