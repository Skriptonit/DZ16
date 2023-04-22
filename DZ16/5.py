# Задание 5
# Создайте класс Clock со статичным методом Say_time, который будет выводить на экран текущее время.
# from time import time, localtime
# # time выводит количество секунд, прошедших с 1 января 1970, 00:00:00
# print(time()) # 1668680736.59019
# # localtime преобразует секунды в кортеж struct_time
# print(localtime(time())) # time.struct_time(tm_year=2022, tm_mon=11, tm_mday=17, tm_hour=10, tm_min=26, tm_sec=8, tm_wday=3, tm_yday=321, tm_isdst=0)
# # Чтобы привести его в красивый вид, можно воспользоваться f-строкой
# rez = localtime(time())
# print(f'{rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}') # 10:29:45
# Подсказка: для этого можете воспользоваться стандартной библиотекой time.
from time import time, localtime
class Clock ():
    @staticmethod
    def Say_time():
        rez = localtime(time())
        print (f' {rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}')
print('Московское время:')
Clock.Say_time()