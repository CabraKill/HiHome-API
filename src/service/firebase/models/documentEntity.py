from abc import ABC, abstractmethod

class DocumentFirebaseEntity(ABC):
    def __init__(self, **kwargs):
        # for key in kwargs.keys:
        #     setattr(self, key, kwargs[key])
        pass
    
    @abstractmethod
    def get(self, key:str):
        pass

    def update(self, fields: dict):
        raise NotImplementedError()
    
    def toDict(self):
        instance_dict = (self.__dict__)
        return instance_dict