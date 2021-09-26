import socket
from threading import Thread


PORT = 9090


def handler(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)


def _main():
    with socket.socket() as sock:
        sock.bind(('', PORT))
        sock.listen()
        while True:
            conn, address = sock.accept()
            Thread(target=handler, args=[conn]).start()


if __name__ == '__main__':
    _main()
