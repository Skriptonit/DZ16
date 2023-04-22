# Задание 2
# Создайте базовый класса Father, у которого есть два атрибута: name (имя) и surname (фамилия);
# и дочерний класс Child, у которого будут унаследованы те же атрибуты и дополнительно атрибут patronim (отчество).
# Создайте один экземпляр класса Child.
class Father ():
    def __init__(self , name, surname):
        self.name = name
        self.surname = surname
class Child (Father):
    def __init__ (self , patronim ):
        super().__init__('Владимир','Путин')
        self.patronim=patronim

c = Child('Владимирович')
print('ФИО:')
print (c.surname,c.name,c.patronim)
