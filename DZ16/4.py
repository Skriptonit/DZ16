# Задание 4
# Создайте базовый класс User с атрибутами login, password и методом:
# view - выводит сообщение "Я - User. Могу просматривать содержимое"
# Создайте дочерний класс Moderator, у которого так же будут атрибуты login и password и дополнительно - group_id, а так же два метода:
# view - выводит сообщение "Я - Moderator. Могу просматривать содержимое"
# redact - выводит сообщение "Я - Moderator. Могу редактировать содержимое"

class User ():
    def __init__(self,login,password):
        self.login=login
        self.password=password

    def view (self):
        return  ("Я-User. Могу просматривать содержимое")

class Moderator (User):
    def __init__ (self  ,login,password,id):
        self.id=id
        super().__init__(login, password)

    def view (self):
        return  ("Я - Moderator. Могу просматривать содержимое")

    def redact (self):
        return ("Я - Moderator. Могу редактировать содержимое")


user = User('LOGIN',"PASSWORD")
print(user.view())
mod=Moderator("login",'password','id')
print (mod.redact())
print (mod.view())

