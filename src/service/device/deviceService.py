from src.devices.lamp.lampIO import LampIO
from src.service.firebase.Ifirebase import IFirebase


class DevicesService:
    def __init__(self, firebaseService: IFirebase):
        self.firebaseService = firebaseService
        self.initDevices()

    def initDevices(self):
        self.homeList = self.firebaseService.getCollection('houses')
        for home in self.homeList:
            for device in home.collection('devices').list_documents():
                device_fields = device.get(['type'])
                device_type = device_fields.get('type')
                if device_type == 'lamp':
                    LampIO(device.path,self.firebaseService)

    def listDevices(self):
        pass
