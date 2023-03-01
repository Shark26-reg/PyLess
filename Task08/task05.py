"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

from subprocess import Popen, PIPE
from chardet import detect

sources = ['yandex.ru', 'youtube.com']
for source in sources:
    ping = Popen(['ping', source], stdout=PIPE)
    for line in ping.stdout:
        result = detect(line)
        line = line.decode(result['encoding']).encode('utf8')
        print(line.decode('utf8'))