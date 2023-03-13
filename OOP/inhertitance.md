# Насаледование 
> принцип ООП, где мы модем унаследовать, переопределять и использовать все атрибуты и методы родителского класса

```py
class A:
    def method(self):
        print('метод v класс A')

obj_a = A()
obj_a.method
# metod v classe A

class B(A):
    pass 

obj_b = B()
obj_b.method()
 # method v classe A
```
> class A - roditel`skiy
> class B - docherniy

## Переопределение
> когда мы создаем метод или атрибут с такм же названием, как и в родительских классах 

```py
class C(A):
    def method(self):
        print("Метод в классе С")

obj_c = C()
obj_c.method
# метод в классе С
```


## Виды наследование
* **одиночное** (когда один родитель)
* **множественное** (когда несколько родитедей)
* многоуровневое (когда у родителя есть  родитель)
* иерархическое (когда у каждого есть только один родитель, но у родителя может быть много детей)
* гибридное (совмещение разных видов наследование)


## Проблемы множественного наследование
1. проблема ромба (решенная с помощью MRO (с версии 2.6))
>MRO - method resolution order (простраивает порядок для поиска аттрибутов)

```py
class A: 
    pass
class B:
    pass
class C(A,B):
    pass

# до mro
[C, A, object, C, B, object]

# после mro
[C, A, B, object]
```

2. проблема перекрестного наследовние (не решенная, возникает когда не овззможно построить приоритет родителей)

```py
#перекрестное наследование
class A: 
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class E(C,D):
    pass
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
```