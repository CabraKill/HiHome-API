from abc import ABC, abstractmethod
from src.connection.models.responseModel import ResponseModel


class Client(ABC):

    @abstractmethod
    def get(self, url: str) -> ResponseModel:
        pass
