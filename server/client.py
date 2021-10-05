import socket
from server import PORT


EXIT = 'exit'


def _main():
    """"
    Объявляем сокет. Подлючаемся к локальному хосту по порту, на котором
    работает сервер. Отправляем данные серверу до тех пор, пока от
    пользователя не поступит команда exit. И печатаем полученные данные.
    Обязательно закрываем сокет.
    """

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