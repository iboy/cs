from abc import ABC, abstractmethod

class BirdAbstractClass(ABC):

    @abstractmethod
    def MakeSound(self):
        pass
    def __init__(self, nameOfBird):
        self.Name = nameOfBird

class Duck(BirdAbstractClass):
    def MakeSound(self):
        print("Quack")

class Crow(BirdAbstractClass):
    def MakeSound(self):
        print("Squawk")

bird1 = Duck("Duck")
print(bird1.Name)
bird1.MakeSound()
bird1 = Crow("Crow")
print(bird1.Name)
bird1.MakeSound()

