from src.devices.lamp.lampIO import LampIO
from src.service.firebase.Ifirebase import IFirebase
from src import app
from flask import request


class DevicesController:
    def __init__(self) -> None:
        self.setEndpoints()
    
    def deviceInitialization(self):
        body = request.json
        return 'OK'

    def setEndpoints(self):
        app.add_url_rule('/init',view_func=self.deviceInitialization, methods=['POST'])
