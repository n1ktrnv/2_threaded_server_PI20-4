from scanner import PortsScanner


def _main():
    hostname = input('Введите имя хоста/IP-адрес: ')
    PortsScanner(hostname).scan_ports()


if __name__ == '__main__':
    _main()


