from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy -= self.power
            days += 1
            print(f'{self.name}, сражается {days} день(дня)..., осталось {self.enemy} воинов.')
            sleep(1)
            if self.enemy == 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!\n')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
