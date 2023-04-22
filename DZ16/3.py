# Задание 3
# А) Реализовать класс Stationery (канцелярия):
# определить в нём атрибут title (название) и абстрактный метод draw (отрисовка);
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в классу Pen добавьте атрибут color = 'blue';
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение, например: "Ручка пишет";
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# Б)Добавьте в класс Stationary метод класса set_color, который присваивает атрибут класса Stationary color;
# Вызовете метод set_color и установите color='yellow';
# Вызовете атрибуты color у классов Pen, Pencil, Handle. Что вы наблюдаете?
from abc import ABC, abstractmethod
class Stationery(ABC):
    def __init__(self,title):
        self.title=title

    @classmethod
    def set_color(cls, color):
        cls.color = color

    @abstractmethod
    def draw (self):
        pass

class Pen (Stationery ):
    def draw (self):
        return("Ручка пишет")
    color ="blue"

class Pencil (Stationery):
    def draw (self):
        return  ("Карандаш пишет")

class Handle (Stationery):
    def draw(self):
        return ("Маркер пишет ")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

print (pen.draw())
print (pencil.draw())
print (handle.draw())

Stationery.set_color('yellow')
print('Цвет ручки:')
print(pen.color)
print('Цвет карандаша:')
print(pencil.color)
print('Цвет маркера:')
print(handle.color)
#Мы наблюдаем ,что у Ручки цвет синий , у Карандаша-желтый,у Маркера-тоже желтый.
#Связано это тем ,что у ручки был обьявлен свой собственный атрибут-Синий, а у карандаша и маркера
#не было собственного атрибута,мы им передали один цвет-Желтый .

