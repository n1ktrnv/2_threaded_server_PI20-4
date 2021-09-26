import socket
from server import PORT


EXIT = 'exit'


def _main():
    sock = socket.socket()
    sock.connect(('localhost', PORT))

    while True:
        message = input()
        if message == EXIT:
            break
        sock.send(message.encode())
        print(sock.recv(1024).decode())

    sock.close()


if __name__ == '__main__':
    _main()