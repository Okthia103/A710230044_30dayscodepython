class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")

    def make_sound(self):
        return "Woof!"

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

    def make_sound(self):
        return "Meow!"

# Membuat objek dari kelas Dog dan Cat
dog1 = Dog("Buddy", 3, "Golden Retriever")
cat1 = Cat("Whiskers", 2, "Gray")

# Menampilkan informasi hewan peliharaan
dog1.display_info()
print(f"Sound: {dog1.make_sound()}\n")
cat1.display_info()
print(f"Sound: {cat1.make_sound()}\n")

# Menggunakan polymorphism
pets = [
    Dog("Rex", 5, "German Shepherd"),
    Cat("Mittens", 1, "Black"),
    Dog("Fido", 4, "Labrador"),
    Cat("Snowball", 3, "White")
]

for pet in pets:
    pet.display_info()
    print(f"Sound: {pet.make_sound()}\n")
