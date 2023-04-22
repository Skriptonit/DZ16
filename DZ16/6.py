# Задание 6 * (необязательное)
# Давайте создадим свой класс Time по аналогии с Date_time выше. Реализуйте в нем классовый метод from_string(),
# который будет принимать в себя строку('00:00:00') и будет преобразовывать его в объект Time.

class Time():
  def __init__(self, hour=00, min=00, sec=00):
    self.hour = hour
    self.min = min
    self.sec = sec

  def __str__(self):
    return f'hour={self.hour}, min={self.min}, sec={self.sec}'

  @classmethod
  def from_string(cls, date_string):
    hour, min, sec = map(int, date_string.split(':'))
    my_date = cls(hour,min, sec)
    return my_date

date_obj = Time.from_string('00:00:00')
print(date_obj)
