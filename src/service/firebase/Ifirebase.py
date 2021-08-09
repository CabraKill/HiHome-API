from google.cloud.firestore import Client
from google.cloud.firestore_v1.document import DocumentReference
from abc import ABC, abstractmethod
from typing import Callable


class IFirebase(ABC):
    def __init__(self) -> None:
        self.init()

    def init(self):
        pass

    @abstractmethod
    def getDb(self) -> Client:
        pass

    @abstractmethod
    def getDocument(self, path: str) -> DocumentReference:
        pass

    @abstractmethod
    def getCollection(self, path: str):
        pass

    @abstractmethod
    def setActionForDocumentChange(self, path: str, function: Callable):
        pass
