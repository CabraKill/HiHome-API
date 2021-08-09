from abc import ABC, abstractmethod

class DocumentFirebaseEntity(ABC):
    def __init__(self, **kwargs):
        for key in kwargs.keys:
            setattr(self, key, kwargs[key])
    
    @abstractmethod
    def get(self, key:str):
        pass