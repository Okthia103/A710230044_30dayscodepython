class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Membuat objek dari kelas Dog dan Cat
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Memanggil metode speak
print(dog1.speak())
print(cat1.speak())
