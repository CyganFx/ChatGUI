# from PyQt5.QtWidgets import *
# from site import getsitepackages
# import sys
# import socket
# import pickle
# import sys
# import threading
#
# from dao import is_authenticated
#
# from PyQt5.uic import loadUi
#
# from client import startClient
#
# HEADER = 64
# PORT = 5050
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "q"
# SERVER = "127.0.0.1"
# ADDR = (SERVER, PORT)
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)
#
#
#
#
#
#
# # class myclass(QWidget):
# #     def __init__(self):
# #         super(myclass, self).__init__()
# #         loadUi('Form.ui', self)
# #         self.pushButton.clicked.connect(self.send)
# #
# #     def send(self):
# #         print("send func")
# #         # soc.send(bytes(self.sendtext.text() + "\n", 'utf-8'))
# #         # self.sendandrec.append('\n' + 'you: ' + self.sendtext.text() + '\n' + soc.recv(1024).decode())
#
#
# def application():
#     startClient()
#     app = QApplication(sys.argv)
#     widget = myclass()
#     widget.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     application()
#
# print(getsitepackages())
