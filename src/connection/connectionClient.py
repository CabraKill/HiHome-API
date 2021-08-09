from requests.models import Response
from src.connection.client import Client


class ConnectionClient:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get(self, url):
        response = self.client.get(url)
        return self.handleConnectionStatus(response)
    
    def handleConnectionStatus(self, response: Response):
        if response.status_code == 200:
            return response
        if response.status_code == 404:
            raise "not found"
        if response.status_code == 500:
            raise "internal error"
        raise 'offline'

