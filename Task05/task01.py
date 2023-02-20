"""Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод."""


from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ('red', 'yellow', 'green')
    __default_timers = {'red': 7, 'yellow': 2, 'green': 10}

    def __init__(self, **kwargs):
        self.__times = TrafficLight.__default_timers.copy()
        self.apply_times(**kwargs)
        self.__color = cycle(TrafficLight.__colors)

    @staticmethod
    def get_colors():
        return TrafficLight.__colors

    def set_default_timers(self):
        self.__times = TrafficLight.__default_timers.copy()

    def apply_times(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.__times.keys():
                raise KeyError(f"параметры должны быть одним из этих: {', '.join(self.__times.keys())}")
            v = int(v)
            if v <= 0:
                raise ValueError("неподдерживаемое значение времени")
            self.__times[k] = v

    def running(self):
        while True:
            light = next(self.__color)
            t = self.__times[light]
            print(f'{light} горит {t} сек')
            for s in range(t, 0, -1):
                print(int(s))
                sleep(1)


if __name__ == '__main__':
    tl = TrafficLight(green=10)
    tl.running()