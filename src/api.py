import requests
from src.exception import handle_exceptions


class ServerAPI:
    @handle_exceptions
    def get_all_data(self):
        response = requests.get("http://127.0.0.1:5000/get")
        response.raise_for_status()
        return response.json()

    @handle_exceptions
    def post_data(self, text_to_send):
        response = requests.post(
            "http://127.0.0.1:5000/add", json={"data": text_to_send}
        )
        response.raise_for_status()
        return response
