from src.controllers.devicesController.models.deviceInitializationEntity import DeviceInitializationEntity
from src.devices.lamp.lampIO import LampIO
from src.service.firebase.Ifirebase import IFirebase
from src import app
from flask import request


class DevicesController:
    def __init__(self, home_name: str, firebaseService: IFirebase) -> None:
        self.home_name = home_name
        self.firebaseService = firebaseService
        self.setEndpoints()

    def deviceInitialization(self):
        body_json = request.json
        deviceInitializationEntity = DeviceInitializationEntity.fromJson(
            body_json)
        device = self.firebaseService.getCollection(
            f'houses/{self.home_name}/devices').where('mac', '==', deviceInitializationEntity.mac)

        return 'OK'

    def setEndpoints(self):
        app.add_url_rule(
            '/init', view_func=self.deviceInitialization, methods=['POST'])
