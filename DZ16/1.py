# Задание 1
# Создайте родительский класс Animal, у которого есть 3 атрибута:
# color - цвет
# name - кличка
# age - возраст
# и абстрактный метод:
# say - издать звук.
# Создайте два класса потомка - Cat и Dog, в которых будет переопределен метод say:
# для класса Cat - Meow!, для Dog - Woof!

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass

class Cat(Animal):
    def say(self):
        return 'Meow!'

class Dog(Animal):
    def say(self):
        return 'Woof!'

Ajax = Cat('Угольный', 'Аякс', 3)
Bars = Dog('Черно-оранжевый', 'Барс', 6)

print('Характеристика моей кошки :')
print('1) Кличка:',Ajax.name)
print('2) Возраст:',Ajax.age)
print('3) Окрас:',Ajax.color)
print('Люмибый  звук кота:',Ajax.say())
print ('------------------------------')
print('Характеристика моей собаки :')
print('1) Кличка:',Bars.name)
print('2) Возраст:',Bars.age)
print('3) Окрас:',Bars.color)
print('Люмибый  звук собаки:',Bars.say())