import socket
import sys

from config import *


class ClientSocket(socket.socket):
    def __init__(self):
        super(ClientSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        super(ClientSocket, self).connect((SERVER_IP, SERVER_PORT))

    def recv_data(self):
        return self.recv(1024).decode('utf-8')

    def send_data(self, message):
        try:
            return self.send(message.encode('utf-8'))
        except OSError:
            print("Server closed connection")

    def exit(self):
        self.close()
        sys.exit(0)
        
