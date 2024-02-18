from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QListView,
    QWidget,
    QVBoxLayout,
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from typing import List
from src.api import ServerAPI


class MyMainWindow(QMainWindow):
    def __init__(self, server_api: ServerAPI):
        super(MyMainWindow, self).__init__()
        self.server_api = server_api

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Введите текстовую информацию")
        self.list_view = QListView(self)
        self.button_post = QPushButton("Отправить данные", self)
        self.button_get = QPushButton("Получить данные", self)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_post)
        layout.addWidget(self.button_get)
        layout.addWidget(self.list_view)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_get.clicked.connect(self.fetch_and_update_data)
        self.button_post.clicked.connect(self.send_data_to_server)

        self.setFixedSize(800, 400)

    def update_list_view(self, data: List[list]):
        model = QStandardItemModel()
        for row in data:
            formatted_string = (
                f"номер клика - {row[0]}: введенный текст - {row[1]}: "
                f"дата отправки - {row[2]}: время отправки - {row[3]} "
            )
            model.appendRow(QStandardItem(formatted_string))
        self.list_view.setModel(model)

    def fetch_and_update_data(self):
        data = self.server_api.get_all_data()
        self.update_list_view(data)

    def send_data_to_server(self):
        text_to_send = self.line_edit.text()
        if text_to_send:
            response = self.server_api.post_data(text_to_send)
            return response


if __name__ == "__main__":
    app = QApplication([])
    server_api = ServerAPI()
    window = MyMainWindow(server_api)
    window.show()
    app.exec()
