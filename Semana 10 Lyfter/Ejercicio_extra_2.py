class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return 'Make a sound'
    
class Dog(Animal):
    def speak(self):
        return 'Guau'
    
class Cat(Animal):
    def speak(self):
        return 'Miau'
    

dog=Dog('Kronos')
cat=Cat('Bruno')

print(f'{dog.name} dice: {dog.speak()}')
print(f'{cat.name} dice: {cat.speak()}')

        
        