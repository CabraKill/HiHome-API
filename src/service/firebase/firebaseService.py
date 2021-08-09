from typing import Callable
from src.service.firebase.models.documentAPIModel import DocumentFirebaseAPIModel
from src.service.firebase.models.documentEntity import DocumentFirebaseEntity
from src.service.firebase.Ifirebase import IFirebase
from google.cloud.firestore import Client


class FirebaseAPIService(IFirebase):
    def __init__(self, project_name: str):
        self.project_name = project_name
        super().__init__()

    def init(self):
        print("FirebaseService initiated.")
        self.db = Client(project=self.project_name)

    def getDb(self) -> Client:
        return super().getDb()

    def getCollection(self, path: str):
        return super().getCollection(path)

    def getDocument(self, path: str) -> DocumentFirebaseEntity:
        documentReference = self.db.document(path)
        document = DocumentFirebaseAPIModel(
            documentReference=documentReference)
        return document

    def setActionForDocumentChange(self, path: str, function: Callable):
        document = self.db.document(path)  # .where(u'state', u'==', u'CA')
        query_watch = document.on_snapshot(function)
