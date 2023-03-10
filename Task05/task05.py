"""Задание 5.
1) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на 
реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. Класс-исключение должен контролировать типы 
данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, 
команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента 
необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить 
пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться."""


import traceback


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class CheckAndAdd:

    def __init__(self):
        self.__result = []
        while True:
            data = input('Число: ')
            try:
                self.__result.append(int(data))
            except ValueError as e:
                if data == 'stop':
                    break
                print('Ввели не число\n', traceback.format_exc())
            except Exception as e:
                if data == 'stop':
                    break
                raise MyException('Ошибка')

    def __str__(self):
        return ', '.join(map(str, self.__result))


if __name__ == '__main__':
    c = CheckAndAdd()
    print(f"(напишите еще раз stop для завершения работы программы)",  c)
    d = CheckAndAdd()
    print(d)
