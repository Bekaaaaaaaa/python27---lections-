"=======================mixins=========================="
"""
1) Миксины - это классы которые используеются для наследование, но от миксинов не создаются обьекты

2) Миксины - классы примеси которые служат для расширения функционала

"""
#ОТ миксинов нельзя созжаввать обьекты, поскольку миксины несамостоятельные классы 
#При анследовании миксины должны идти в первую очередь 

class walkMixin:
    def walk(self):
        print("я могу ходить")

class SwimMixin:
    def swim(self):
        print("я могу плавать")

class FlyMixin:
    def fly(self):
        print("я могу летать")

class Human(walkMixin):
    name = "Человек"

    def talk(self):
        print("я могу говорить")

class Fish(SwimMixin):
    name = "алтын балык"

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'fly fish'

class Duck(walkMixin, FlyMixin, SwimMixin):
    name = "ордок"

# objects = [Human(), Fish(), Duck(), Exocoetidae()]
# for obj in objects:
#     attrs = ['flt', "swim", "walk", "talk"]
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()

obj = Human()
setattr(obj, 'new_attribute', 'hello world')
# print(dir(obj))
print(obj.new_attribute)

# obj = Human()
# print(hasattr(obj, 'fly')) -> True
# method = (getattr(obj, 'walk'))
# print(method) -> <bound method walkMixin.walk of <__main__.Human object at 0x7fa61c157fd0>>
# obj.swim()
# obj.fly()
# obj.walk()

#hasattr - функция, которая принимает обьект и название аттрибута.Возвращает Treu. если у обьекта есть такой аттрибут

#gettatr - функция которая принимает обьект и название аттрибута. Возвращает значение аттрибута

#setattr - функция которая принимает обьект, название аттрибута и значение аттрибута. Добавляет в обьект новый аттрибут или перезапишет одноименнный аттрибут

