from google.cloud.firestore import Client
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference
from abc import ABC, abstractmethod
from typing import Any, Callable, Generator
from src.service.firebase.models.documentEntity import DocumentFirebaseEntity


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
    def getCollection(self, path: str) -> CollectionReference:
        pass

    @abstractmethod
    def getDocumentCollection(self, path: str) -> Generator[Any, Any, None]:
        pass

    @abstractmethod
    def setActionForDocumentChange(self, path: str, function: Callable):
        pass

    @abstractmethod
    def updateDocument(self, id: str, document: DocumentFirebaseEntity):
        pass
