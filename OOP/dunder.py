# dunder (doebl underscore) - метода у которых 2 _ в начале и в конце
# магия в том, что мы их не вызываем напрямую

class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)
    
    def __init__(self):
        print("__INIT__")
        pass

A()
# __NEW__
# __INIT__


#__new__, __init__ - вызываются при создании обьекта 

print(dir(object))


