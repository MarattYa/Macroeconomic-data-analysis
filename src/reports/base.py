from abc import ABC, abstractmethod

from models import CountryRow


class BaseReport(ABC):

    @abstractmethod
    def build(self, rows: list[CountryRow]) -> list[dict]:
        pass
