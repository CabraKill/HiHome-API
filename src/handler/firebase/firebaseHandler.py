import json
from src.handler.firebase.Ifirebase import IFirebase
import requests


class FirebaseHandler(IFirebase):
    def getToken(self):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={apiKey}"
        response = requests.post(
            link, headers={'Content-Type': 'application/json'}, json={"returnSecureToken": True})
        return response.json()

