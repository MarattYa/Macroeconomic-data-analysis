from collections import defaultdict

from models import CountryRow

from .base import BaseReport


class AverageGDPReport(BaseReport):

    def build(self, rows: list[CountryRow]) -> list[dict]:
        data: dict[str, list[float]] = defaultdict(list)

        for r in rows:
            data[r["country"]].append(r["gdp"])

        result: list[dict] = []

        for country, values in data.items():
            avg = sum(values) / len(values)

            result.append({"country": country, "average_gdp": round(avg, 2)})

        result.sort(key=lambda x: x["average_gdp"], reverse=True)

        return result
