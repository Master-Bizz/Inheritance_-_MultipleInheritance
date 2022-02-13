'''
inheritance 
'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"My name is {self.name}"
    
class Dog(Animal): # (Animal) - the inheritance link
    def __init__(self, name, age):
        super().__init__(name, age) # Better way of writing it.
    
    def speak(self):
        return "whoof whoof!" # Can create own 'speak' in class that overides default 'speak' in main Animal class.

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        