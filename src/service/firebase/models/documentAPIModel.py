from src.service.firebase.models.documentEntity import DocumentFirebaseEntity
from google.cloud.firestore_v1.document import DocumentReference


class DocumentFirebaseAPIModel(DocumentFirebaseEntity):
    def __init__(self, documentReference: DocumentReference) -> None:
        super().__init__(document=documentReference)

    def get(self, key: str):
        value = self.document.get(key)
        return value
