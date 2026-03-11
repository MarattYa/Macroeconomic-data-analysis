import csv

from models import CountryRow


def load_data(files: list[str]) -> list[CountryRow]:
    rows: list[CountryRow] = []

    for file in files:
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for r in reader:
                row: CountryRow = {
                    "country": r["country"],
                    "year": r["year"],
                    "gdp": float(r["gdp"]),
                    "gdp_growth": r["gdp_growth"],
                    "inflation": r["inflation"],
                    "unemployment": r["unemployment"],
                    "population": r["population"],
                    "continent": r["continent"],
                }

                rows.append(row)

    return rows
