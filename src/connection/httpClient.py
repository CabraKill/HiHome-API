from src.connection.models.responseModel import ResponseModel
from src.connection.client import Client
from requests import get


class HttpClient(Client):

    def get(self, url: str):
        response = get(url, timeout=20)
        responseModel = ResponseModel(
            response.status_code, response.content.decode('utf-8'))
        return responseModel
