import pickle
import socket
import threading
from datetime import datetime

import dao

PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class Server(object):
    clients = {}

    def __init__(self):
        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)

        # start server
        self.tcp_server.bind(ADDR)
        self.tcp_server.listen(5)

        print("[INFO] Server running on {}:{}".format(SERVER, PORT))

        while True:
            conn, addr = self.tcp_server.accept()
            print(f"[NEW CONNECTION] {addr} connected.")
            threading.Thread(target=self.receive_message, args=(conn, addr), daemon=True).start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def receive_message(self, conn, addr):
        conn.send("[Welcome to the chatroom!]".encode(FORMAT))
        connected = True
        while connected:
            temp = conn.recv(2046)
            data = pickle.loads(temp)
            id = data[0]
            username = data[1]
            msg = data[2]
            self.clients[username] = conn

            now = datetime.now().strftime('%H:%M:%S')
            message_to_send = f"{username}: {msg} ({now})"
            print(message_to_send)

            dao.insert_log_info(id, msg, datetime.now())
            self.broadcast(message_to_send.encode(FORMAT), conn, username)

        conn.close()

    def broadcast(self, message, connection, username):
        for name, client in self.clients.items():
            if client != connection:
                try:
                    client.send(message)
                except:
                    del self.clients[username]


if __name__ == "__main__":
    chat_server = Server()
