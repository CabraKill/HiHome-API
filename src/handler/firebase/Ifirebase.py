class IFirebase:
    def __init__(self) -> None:
        pass

    def getToken(self):
        raise NotImplementedError()

    def getTestDocument(self):
        raise NotImplementedError()
