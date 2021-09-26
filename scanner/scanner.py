import socket
from concurrent.futures import ThreadPoolExecutor
from threading import RLock

from progressbar import ProgressBar


class PortsScanner:

    PORTS_COUNT = 2 ** 16

    def __init__(self, host):
        self._host = host
        self._progress_bar = ProgressBar(self.PORTS_COUNT, 'Выполнено')

    def scan_ports(self, threads_count=None):
        self._progress_bar.print()
        with ThreadPoolExecutor(threads_count) as executor:
            lock = RLock()
            for port in range(self.PORTS_COUNT):
                executor.submit(self._scan_port, port, lock)

    def info(self, message):
        print(message,
              end=(' ' * (len(self._progress_bar) - len(message)) + '\n'))

    def _scan_port(self, port, lock):
        with socket.socket() as sock:
            try:
                sock.connect((self._host, port))
            except socket.error:
                pass
            else:
                with lock:
                    self.info(f'Порт {port} открыт')
            finally:
                with lock:
                    self._progress_bar.update()
