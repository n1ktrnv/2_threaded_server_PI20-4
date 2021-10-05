import socket
from threading import Thread


PORT = 9090


def handler(conn):
    """
    Функция-обработчик сокета подключения с клиентом. Используем менеджер
    контекста, чтобы в случае ошибок сокет был точно закрыт. Далее принимаем
    данные по 1024 кБ и отправляем их обратно клиенту до тех пор, пока они не
    закончатся.
    """
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)


def _main():
    """
    С помощью менеджера контекста, чтобы в случае ошибок сокет был точно
    закрыт, объявляем сокет. Привязываем порт. Затем слушаем порты. Далее
    сервер в бесконечном цикле принимает соеднения и для каждого соединения
    создает поток, вызывая функцию handler и передавая в нее один аргумент —
    сокет подлючения с клиентом.
    """
    with socket.socket() as sock:
        sock.bind(('', PORT))
        sock.listen()
        while True:
            conn, address = sock.accept()
            Thread(target=handler, args=[conn]).start()


if __name__ == '__main__':
    _main()
