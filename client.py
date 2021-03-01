import pickle
import socket
import sys
from datetime import datetime

from PyQt5 import QtCore, QtWidgets

import dao
import login_page_ui
import private_chat_ui
import public_chat_ui
from dao import is_authenticated

PORT = 5050
FORMAT = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(2046)
        print("\n", message.decode(FORMAT))
        self.signal.emit(message.decode(FORMAT))


class Client(object):
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        self.login_page_widget = QtWidgets.QWidget(self.mainWindow)
        self.public_chat_widget = QtWidgets.QWidget(self.mainWindow)
        self.private_chat_widget = QtWidgets.QWidget(self.mainWindow)

        self.public_chat_widget.setHidden(True)
        self.private_chat_widget.setHidden(True)

        self.public_chat_ui = public_chat_ui.Ui_Form()
        self.public_chat_ui.setupUi(self.public_chat_widget)

        self.private_chat_ui = private_chat_ui.Ui_Form()
        self.private_chat_ui.setupUi(self.private_chat_widget)

        self.public_chat_ui.sendButton.clicked.connect(self.send_public_message)
        self.public_chat_ui.logsButton.clicked.connect(self.show_logs)
        self.public_chat_ui.privateModeButton.clicked.connect(self.enter_private_mode)

        self.private_chat_ui.sendButton.clicked.connect(self.send_private_message)
        self.private_chat_ui.logsButton.clicked.connect(self.show_logs)
        self.private_chat_ui.publicModeButton.clicked.connect(self.enter_public_mode)

        self.login_page_ui = login_page_ui.Ui_Form()
        self.login_page_ui.setupUi(self.login_page_widget)
        self.login_page_ui.authenticateButton.clicked.connect(self.authenticate)

        self.mainWindow.setGeometry(QtCore.QRect(0, 0, 401, 658))
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def authenticate(self):
        username = self.login_page_ui.usernameField.toPlainText()
        id = is_authenticated(username)
        if id == 0:
            print("Incorrect data")
        else:
            self.username = username
            self.id = id
            print("authenticated successfuly!")
            self.tcp_client.connect(ADDR)
            self.login_page_widget.setHidden(True)
            self.public_chat_widget.setVisible(True)
            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")

    def send_public_message(self):
        message = self.public_chat_ui.textField.toPlainText()
        now = datetime.now().strftime('%H:%M:%S')
        self.public_chat_ui.textBrowser.append(f"Me: {message} ({now})")
        data = pickle.dumps([self.id, self.username, message])
        self.tcp_client.send(data)
        self.public_chat_ui.textField.clear()

    def send_private_message(self):
        # message = self.private_chat_ui.textField.toPlainText()
        # destination_username = self.private_chat_ui.destinationUsername.toPlainText()
        # now = datetime.now().strftime('%H:%M:%S')
        pass

    def show_message(self, message):
        self.public_chat_ui.textBrowser.append(message)

    def show_logs(self):
        """appending logs info;
        logs[idx + 1] = time, logs[idx] = message
        """
        logs = dao.get_log_info_by_id(self.id)
        idx = 0
        for i in range(int(len(logs) / 2)):
            self.public_chat_ui.textBrowser.append(f"({logs[idx + 1]}) - {logs[idx]}")
            idx += 2

    def enter_private_mode(self):
        self.public_chat_widget.setHidden(True)
        self.private_chat_widget.setVisible(True)

    def enter_public_mode(self):
        self.private_chat_widget.setHidden(True)
        self.public_chat_widget.setVisible(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())
