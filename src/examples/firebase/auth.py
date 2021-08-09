from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import google

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
response = authed_session.get(
    "https://firestore.googleapis.com/v1beta1/projects/home-dbb7e/databases/(default)/documents/configs/last",
    headers={"Authorization": f"Bearer {credentials.token}",
             "Accept": "application/json"
             })
jsonText = response.json()

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)
request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token
print(access_token)
