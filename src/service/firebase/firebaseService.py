from typing import Any, Callable, Generator
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference
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

    def getCollection(self, path: str) -> CollectionReference:
        collection = self.db.collection(path)
        return collection
    
    def getDocumentCollection(self, path: str) -> Generator[Any, Any, None]:
        documents = self.db.collection(path).list_documents()
        print(type(documents))
        return documents

    def getDocument(self, path: str) -> DocumentFirebaseEntity:
        documentReference = self.db.document(path)
        document = DocumentFirebaseAPIModel(
            documentReference=documentReference)
        return document

    def setActionForDocumentChange(self, path: str, function: Callable):
        document = self.db.document(path)  # .where(u'state', u'==', u'CA')
        query_watch = document.on_snapshot(function)
    
    def updateDocument(self, house_name:str, id:str, document: DocumentFirebaseEntity):
        document_dict = document.toDict()
        print(document_dict)
        # self.db.collection(f'{house_name}/devices').add(document_dict)
