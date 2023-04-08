
# #Encapsulation

# class Car:
#     def __init__(self, speed, color):
#         self.__speed = speed
#         self.__color = color
#
#     def set_speed(self, value):
#         self.__speed = value
#
#     def get_speed(self):
#         return self.__speed
#
#
# ford = Car(200, 'red')
# honda = Car(250, 'blue')
# audi = Car(300, 'black')
# # ford.speed = 300
#
# ford.set_speed(300)
# ford.__speed = 400
# print(ford.get_speed())
# # print(ford.speed)
# print(ford.color)

# private Method
class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Hello('name')
print(hello.a)
print(hello._b)
# print(hello.__c)
hello.public_method()
# hello.__private_method()