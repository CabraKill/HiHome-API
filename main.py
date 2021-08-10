from src.controllers.devicesController.devicesController import DevicesController
from src.devices.lamp.lampIO import LampIO
from src.service.firebase.firebaseService import FirebaseAPIService

firebaseAPIService = FirebaseAPIService(project_name='home-dbb7e')

devicesController = DevicesController(firebaseAPIService)

print('Press Ctrl+C to exit <3')
while True:
    pass

print("Done")
