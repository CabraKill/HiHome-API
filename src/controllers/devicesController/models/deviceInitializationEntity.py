class DeviceInitializationEntity:
    def __init__(self, name: str = None, state: str = None, device_type: str = None, mac: str = None, ip: str = None):
        self.name = name
        self.state = state
        self.type = device_type
        self.mac = mac
        self.ip = ip

    @classmethod
    def fromJson(json: dict) -> DeviceInitializationEntity:
        deviceInitializationEntity = DeviceInitializationEntity(
            name=json['name'],
            state=json['state'],
            device_type=json['device_type'],
            mac=json['mac'], ip=json['ip']
        )
        return deviceInitializationEntity
