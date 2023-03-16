class Dog:
    def speak(self):
        print("gav-gav")

class Cat:
    def speak(self):
        print("meow-meow")


class Frog:
    def speak(self):
        print("kva-kva")

animals = [Cat(), Frog(), Dog(), Cat(), Dog(), Frog()]
for animal in animals:
    animal.speak()
    print(animal)


list1 = [1,2,3,4,5,6]
dict1 = {1:'a', 2:'b'}

list1.pop(0) # удааление по индексу
dict1.pop('a') # удаление по ключу

1 + 3
"a" + "b"
#__add__
a = 4
b = 5
print(a + b) # 9
print(a.__add__(b))# 9

#__len__
a = 'abc'
print(len(a))
print(a.__len__())

b = [1,2,3,[1,2,3]]
print(len(b))



'==========задачки========'
'2'
# class Dog:
#     def voice(self):
#         print("Гав")

# class Cat:
#     def voice(self):
#         print("Мяу")

# def to_pet(a, b):
#     a.voice()
#     b.voice()

# barsik = Cat()
# rex = Dog()
# to_pet(barsik, rex)

'3'

class Person:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}')

class Employee(Person):
    def __init__(self,name,last_name,work,status):
        super().__init__(name,last_name)
        self.work = work
        self.status = status
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

class Student(Person):
    def __init__(self,name,last_name,university,course):
        super().__init__(name,last_name)
        self.university = university
        self.course = course
    def get_info(self):
        print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

def get_human_info(func1):
    return func1.get_info() 

person = Person('ivan', 'petrov')
employee = Employee('ivan', 'petrov', 'roga i kopyta', 'direktor')
student = Student('ivan', 'petrov', 'kgtu', 3)

get_human_info(person) 
get_human_info(employee) 
get_human_info(student)