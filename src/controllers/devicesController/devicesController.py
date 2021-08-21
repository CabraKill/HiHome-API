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
        device = self.firebaseService.getDocument(
            f'houses/{self.home_name}/devices/{deviceInitializationEntity.mac}')
        json_map = device.get(['state'])
        return json_map.get('state') if device else "error"

    def getState(self, home: str, mac: str):
        print(f"endpoint: getState - home:{home} - mac:{mac}")
        device = self.firebaseService.getDocument(
            f'houses/{home}/devices/{mac}')
        json_map = device.get(['state'])
        state = json_map.get('state')
        return state if state else "off"

    def setEndpoints(self):
        app.add_url_rule(
            '/init', view_func=self.deviceInitialization, methods=['POST'])
        app.add_url_rule(
            '/homes/<string:home>/devices/<string:mac>', view_func=self.getState, methods=['GET'])
