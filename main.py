from src import app
from src.service.device.deviceService import DevicesService
from src.controllers.devicesController.devicesController import DevicesController
from src.devices.lamp.lampIO import LampIO
from src.service.firebase.firebaseService import FirebaseAPIService

HOME_NAME = 'home-dbb7e'


firebaseAPIService = FirebaseAPIService(project_name=HOME_NAME)

deviceService = DevicesService(firebaseAPIService)
devicesController = DevicesController(home_name=HOME_NAME,firebaseService=firebaseAPIService)

@app.route('/')
def home():
  return 'oi'

print('Press Ctrl+C to exit <3')
