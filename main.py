from src.devices.lamp.lampIO import LampIO
from src.service.firebase.firebaseService import FirebaseAPIService

firebaseAPIService = FirebaseAPIService(project_name='home-dbb7e')

lampDriver = LampIO(db_path='houses/buHkimoPE1e5NMx7C4kX/devices/F5fEOy8Yzctl31UZxu7Y',
                        firebaseService=firebaseAPIService)

print('Press Ctrl+C to exit <3')
while True:
    pass

print("Done")
