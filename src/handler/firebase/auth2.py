import json
from src.handler.firebase.sse import ClosableSSEClient
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import threading
import socket

# Define the required scopes
scopes = [
    # "https://www.googleapis.com/auth/userinfo.email",
    # "https://www.googleapis.com/auth/firebase.database"
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/datastore"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "serviceAccountKey.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)


class FireThread(threading.Thread):
    def __init__(self):
        super(FireThread, self).__init__()

    def run(self):
        try:
            self.sse = ClosableSSEClient(
                "https://firestore.googleapis.com/v1beta1/projects/home-dbb7e/databases/(default)/documents/configs.json")
            for msg in self.sse:
                if(not msg.data):
                    continue
                msg_data = json.loads(msg.data)
                if msg_data is None:    # keep-alives
                    continue
                path = msg_data['path']
                data = msg_data['data']
                if path == '/':
                    # initial update
                    if data:
                        keys = data.keys()
                        keys.sort()
                        for k in keys:
                            print(data[k])
                            # self.message_queue.put(data[k])
                else:
                    # must be a push ID
                    # self.message_queue.put(data)
                    print(data)
        except Exception as e:
            print(e)
        # except socket.error:
        #     print(socket.error)

    def close(self):
        if self.sse:
            self.sse.close()

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)

# request = google.auth.transport.requests.Request()
# credentials.refresh(request)
# access_token = credentials.token
# print(access_token)
