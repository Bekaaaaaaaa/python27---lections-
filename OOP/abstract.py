from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak():
        pass

class Dog(AbstractAnimal):
    pass

obj = Dog()
#    obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract method speak

class Dog(AbstractAnimal):
    def speak(self):
        print('gav-gav')

obj = Dog()
obj.speak