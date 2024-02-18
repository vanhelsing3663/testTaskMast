import sys
import pytest
import requests
import requests_mock
from src.api import ServerAPI


class TestApi:
    @pytest.fixture
    def mock_req(self):
        with requests_mock.Mocker() as m:
            yield m

    @pytest.mark.parametrize(
        "expected_result", [([1, 2, 3]), ("123456"), (123456), ({"1": 2})]
    )
    def test_get_all_data(self, mock_req, expected_result):
        mock_req.get("http://127.0.0.1:5000/get", json=expected_result)
        server_api = ServerAPI()
        response = server_api.get_all_data()
        assert response == expected_result

    @pytest.mark.parametrize(
        "expected_result", [([1, 2, 3]), ("123456"), (123456), ({"1": 2})]
    )
    def test_post_data(self, mock_req, expected_result):
        mock_req.post("http://127.0.0.1:5000/add", status_code=200)
        server_api = ServerAPI()
        response = server_api.post_data(expected_result)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "data_size", [100, 1000, 10000, 100000]
    )
    def test_get_all_data_large_response(self, mock_req, data_size):
        mock_req.get("http://127.0.0.1:5000/get", json=list(range(data_size)))
        server_api = ServerAPI()
        response = server_api.get_all_data()
        assert response == list(range(data_size))
