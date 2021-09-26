class ProgressBar:

    def __init__(self, total, suffix='', fill='█', width=40):
        self._total = total
        self._fill = fill
        self._suffix = suffix
        self._width = width

        self._current = 0
        self._unused_part = 0

    def __str__(self):
        bar = '\r'
        if self._suffix:
            bar += self._suffix + ' '
        filled = self._fill * self._fill_count
        empty = ' ' * self._empty_count
        bar += f'[{filled}{empty}]' + ' '
        bar += f'({self._current}/{self._total})' + ' '
        bar += f'{self._percentages}%'
        bar += '\r'
        if self.completed():
            bar += '\n'
        return bar

    def __len__(self):
        return len(str(self))

    def print(self):
        print(self, end='')

    def update(self):
        self.next()
        self.print()

    def next(self):
        if not self.completed():
            self._current += 1

    def completed(self):
        return self._current == self._total

    @property
    def _completed_part(self):
        return self._current / self._total

    @property
    def _percentages(self):
        return round(self._completed_part * 100, 2)

    @property
    def _fill_count(self):
        to_fill = self._completed_part * self._width
        if self._unused_part > 0:
            fill_count = round(to_fill + self._unused_part)
        else:
            fill_count = round(to_fill)
        self.unused_part = fill_count - to_fill
        return fill_count

    @property
    def _empty_count(self):
        return self._width - self._fill_count
