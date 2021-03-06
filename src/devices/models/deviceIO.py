from abc import ABC, abstractmethod
from src.connection.connectionClient import ConnectionClient
from src.service.firebase.Ifirebase import IFirebase


class DeviceIO(ABC):
    def __init__(self, db_path: str, firebaseService: IFirebase, connectionClient: ConnectionClient):
        self.db_path = db_path
        self.firebaseService = firebaseService
        self.connectionClient = connectionClient
        self.configureFireBase()

    def configureFireBase(self):
        self.firebaseService.setActionForDocumentChange(
            self.db_path, self.onChanged)

    @abstractmethod
    def onChanged(self, col_snapshot, changes, read_time):
        pass

    @abstractmethod
    def getStateFromDocument(self, col_snapshot, changes, read_time):
        pass
