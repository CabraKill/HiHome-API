from src.connection.connectionClient import ConnectionClient
from src.devices.models.deviceIO import DeviceIO
from src.service.firebase.models.documentEntity import DocumentFirebaseEntity
from src.service.firebase.Ifirebase import IFirebase


class LampIO(DeviceIO):
    def __init__(self, db_path: str, firebaseService: IFirebase, connectionClient: ConnectionClient):
        super().__init__(db_path, firebaseService, connectionClient)

    def turnOn(self, link: str):
        try:
            response = self.connectionClient.get(link+'/on')
            print(response)
            print('lamp turned on')
        except Exception as e:
            print(e)

    def turnOff(self, link: str):
        try:
            response = self.connectionClient.get(link+'/off')
            print(response)
            print('lamp turned off')
        except Exception as e:
            print(e)
            
    def onChanged(self, col_snapshot, changes, read_time):
        current_state = self.getStateFromDocument(
            col_snapshot, changes, read_time)
        if current_state == 'ON':
            self.turnOn(col_snapshot[0].get('ip'))
        else:
            self.turnOff(col_snapshot[0].get('ip'))

    def getStateFromDocument(self, col_snapshot, changes, read_time):
        current_state = col_snapshot[0].get('state')
        return current_state
