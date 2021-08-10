from src import app
from src.service.device.deviceService import DevicesService
from src.controllers.devicesController.devicesController import DevicesController
from src.devices.lamp.lampIO import LampIO
from src.service.firebase.firebaseService import FirebaseAPIService


firebaseAPIService = FirebaseAPIService(project_name='home-dbb7e')

deviceService = DevicesService(firebaseAPIService)
devicesController = DevicesController()

print('Press Ctrl+C to exit <3')
