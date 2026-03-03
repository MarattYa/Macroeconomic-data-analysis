from abc import ABC, abstractmethod


class BaseReport(ABC):

    @abstractmethod
    def build(self, rows):
        pass