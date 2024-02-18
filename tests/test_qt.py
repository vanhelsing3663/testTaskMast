from unittest.mock import Mock, patch
from PyQt6.QtWidgets import QApplication
from src.api import ServerAPI
from qt import MyMainWindow

app = QApplication([])


def test_update_list_view():
    server_api = Mock(spec=ServerAPI)
    window = MyMainWindow(server_api)
    data = [[1, "текст", "2024-02-18", "18:00:45"]]
    window.update_list_view(data)
    model = window.list_view.model()
    assert model.rowCount() == 1
    assert (
        model.item(0).text()
        == "номер клика - 1: введенный текст - текст: дата отправки - 2024-02-18: время отправки - 18:00:45 "
    )


@patch("src.api.ServerAPI.get_all_data")
def test_fetch_and_update_data(mock_get_all_data):
    mock_get_all_data.return_value = [[1, "текст", "2024-02-18", "18:00:45"]]
    server_api = ServerAPI()
    window = MyMainWindow(server_api)
    window.fetch_and_update_data()
    model = window.list_view.model()
    assert model.rowCount() == 1
    assert (
        model.item(0).text()
        == "номер клика - 1: введенный текст - текст: дата отправки - 2024-02-18: время отправки - 18:00:45 "
    )


@patch("src.api.ServerAPI.post_data")
def test_send_data_to_server(mock_post_data):
    mock_post_data.return_value = 200
    server_api = ServerAPI()
    window = MyMainWindow(server_api)
    window.line_edit.setText("тестовый текст")
    response = window.send_data_to_server()
    assert response == 200
