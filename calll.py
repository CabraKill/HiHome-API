import requests
response = requests.get("https://firestore.googleapis.com/v1beta1/projects/home-dbb7e/databases/(default)/documents/configs/last",
                        headers={ "Accept": "text/event-stream"
                                 })
print(response.json())
