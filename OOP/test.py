'1'
# class Song:
#     def __init__(self, author, title, year):
#         self.author = author
#         self.title = title
#         self.year = year

#     def show_author(self):
#         return f"Автор этой песни {self.author}"

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_year(self):
#         return f"Эта песня вышла в {self.year} году"

# song = Song('Pharrell Williams','Happy', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

'2'

# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         res = self.pi * self.radius**2
#         return res


# circle = Circle(2)
# circle.color = 'синий'
# print(circle.color)
# print(circle.get_area())

'3'
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Ваш баланс: {self.balance} сом')


    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш баланс: {self.balance} сом')

account = BankAccount()        

account.deposit(1000) 
account.withdraw(500) 

'4'
class Taxi:
    def __init__(self, name, cost, cost_km):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km

    def get_total_cost(self, km):
        self.cost = self.cost_km * km + self.cost
        return f'Такси {self.name}, стоимость поездки: {self.cost} сом'
        
taxi1 = Taxi('Namba', 50, 10)
taxi2 = Taxi('jorgo', 50, 10)
taxi3 = Taxi('beka', 50, 10)

print(taxi1.get_total_cost(2))
print(taxi2.get_total_cost(2))
print(taxi3.get_total_cost(1))
'5'
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')


contact = Phone('John', 'Snow', '+996707707707')
contact.get_info()

'6'
class Salary:
    percent = 8
    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience
    def count_percent(self):
        return self.salary * self.percent/100*self.experience

    
obj = Salary(1000, 8)
print(obj.count_percent()) 

'7'
import datetime

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def get_year(self):
        a = datetime.datetime.now()
        res = a.year - self.year
        return f'выиграл {res} лет назад'
winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner)
# print(winner1.get_year())

'===========задачи инкапсулияция==========='
'1'
class A:
    def public(self):
        return 'Public method'
    def _protected(self):
        return 'Protected method'

    def __private(self):
        return 'Private method'

obj1 = A()
print(obj1.public)
print(obj1._protected)
print(obj1._A__private)

'2'
class A:
    def method1(self):
        print("Hello World")
class B(A):
    pass
    


b1 = B()
b1.method1()

'3'
class Car:
    __speed = 0

    def set_speed(self, new):
         self.__speed = new

    def show_speed(self):
        return self.__speed

car1 = Car()
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed())
 
'4'
class Car:
    __speed = 0
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, new):
         self.__speed = new


car1 = Car()
print(car1.speed) 
car1.speed = 20 
print(car1.speed)

'5'
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __сard_number = "9999 9999 9999 9999"

# john = Person()
# print(Person.name)
# print(Person._phone_number)
# print(Person._Person__card_number)

class Person:
    name = "John"
    _phone_number = "+996 557 55 17 57"
    __card_number = "9999 9999 9999 9999"

john = Person()
print(Person.name)
print(Person._phone_number)
print(Person._Person__card_number)

'6'
class Person:
    def __init__(self, name, phone_number, card_number):
        self.name = name
        self._phone_number = phone_number
        self.__card_number = card_number
        

john = Person("John", "+996 557 55 17 57",  "9999 9999 9999 9999")
print(john.name)
print(john._phone_number)
print(john._Person__card_number)
'7'
class Person:
    name = "John"
    _phone_number = "+996 557 55 17 57"
    __card_number = "9999 9999 9999 9999"

    def get_number(self):
        return self.__card_number
    def set_number(self):
        self.__card_number = None
        return self.__card_number


john = Person()
john.name = None
john._phone_number = None
print(john.name)
print(john._phone_number)
print(john.set_number())