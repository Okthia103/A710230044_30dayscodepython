class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def move(self):
        return f"{self.make} {self.model} with {self.doors} doors is driving."

class Plane(Vehicle):
    def __init__(self, make, model, airline):
        super().__init__(make, model)
        self.airline = airline

    def move(self):
        return f"{self.make} {self.model} operated by {self.airline} is flying."

class Boat(Vehicle):
    def __init__(self, make, model, type):
        super().__init__(make, model)
        self.type = type

    def move(self):
        return f"{self.make} {self.model} of type {self.type} is sailing."

# Membuat objek dari masing-masing kelas
car = Car("Toyota", "Corolla", 4)
plane = Plane("Boeing", "747", "Delta")
boat = Boat("Yamaha", "242X", "Speedboat")

# Polimorfisme: Menggunakan metode move pada objek yang berbeda
vehicles = [car, plane, boat]

for vehicle in vehicles:
    print(vehicle.move())
