from src.service.firebase.firebaseService import FirebaseAPIService

firebaseAPIService = FirebaseAPIService(project_name='home-dbb7e')


def lamp(col_snapshot, changes, read_time):
    for doc in col_snapshot:
        print(f'{doc.id} - {doc.get("timee")}')


firebaseAPIService.setActionForDocumentChange("configs/last", lamp)
print('Press Ctrl+C to exit <3')
while True:
    pass

print("Done")
