from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListView, QWidget, QVBoxLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import requests

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.lineEdit = QLineEdit(self)
        self.listView = QListView(self)
        self.buttonPost = QPushButton('Отправить данные', self)
        self.buttonGet = QPushButton('Получить данные', self)

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.buttonPost)
        layout.addWidget(self.buttonGet)
        layout.addWidget(self.listView)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.buttonGet.clicked.connect(self.fetch_and_update_data)
        self.buttonPost.clicked.connect(self.send_data_to_server)

    def request_for_all_data(self):
        response = requests.get('http://127.0.0.1:5000/get')
        return response.json()

    def fetch_and_update_data(self):
        data = self.request_for_all_data()
        self.update_list_view(data)

    def update_list_view(self, data):
        model = QStandardItemModel()
        for row in data:
            lst = [str(item) for item in row]
            model.appendRow(QStandardItem(":".join(lst)))
        self.listView.setModel(model)

    def send_data_to_server(self):
        text_to_send = self.lineEdit.text()
        if text_to_send:
            try:
                response = requests.post('http://127.0.0.1:5000/add', json={'data': text_to_send})
                return response
            except requests.exceptions.RequestException as e:
                print(f"Error sending data to server: {e}")

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
