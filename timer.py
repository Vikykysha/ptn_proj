""" Контекстный менеджер, который высчитывает время, проведенное внутри файла """

import time

class Timer:
    def __init__(self):
        self.start_time = time.time()
    def __enter__(self):
        return
    def __exit__(self, *args):
        print('Elasped {}'.format(time.time() - self.start_time))

with Timer() as t:
    time.sleep(1)