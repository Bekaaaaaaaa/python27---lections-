class Person:
    arms = 2
    legs = 2
    name = 'Beka'

    def __init__(self, name):
        # __init__ - dunder метод, который добавляет в обьект self аттрибуты которые отличаются у разных обьектов
        self.name = name


    def walk(self):
        #self - ссылка на обьект, у которого мы вызываем данный метод
        # print(self)
        print(f"{self.name} walk")

person1 = Person('Bektur')
person2 = Person('Maksat')
person1.walk()
person2.walk()


# person1 = Person()
# print(person1.walk()) #2

# person1 = Person()
# Person.walk(person1)
# person1.walk

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)
# print(dir(Person))
# print(dir(object))

# person1 = Person('Beka')
# person2 = Person('krasavchik')
# print(person1.name, person2.name)

# Аттрибуты класса и аттрибутты обькта класса 

# class A:
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная обьекта'

# print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

# obj = A()
# print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']##
#### ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']


# print(obj.var1) # 'переменная класса'
# print(obj.var2) # 'переменная обьекта'
