from src.devices.models.deviceIO import DeviceIO
from src.service.firebase.models.documentEntity import DocumentFirebaseEntity
from src.service.firebase.Ifirebase import IFirebase


class LampIO(DeviceIO):
    def __init__(self, db_path: str, firebaseService: IFirebase):
        super().__init__(db_path, firebaseService)

    def turnOn(self):
        print('lamp turned on')

    def turnOff(self):
        print('lamp turned off')

    def onChanged(self, col_snapshot, changes, read_time):
        current_state = self.getStateFromDocument(col_snapshot, changes, read_time)
        if current_state == 'ON':
            self.turnOn()
        else:
            self.turnOff()

    def getStateFromDocument(self, col_snapshot, changes, read_time):
        current_state = col_snapshot[0].get('state')
        return current_state

