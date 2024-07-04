class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, type_bike):
        super().__init__(brand, model, year)
        self.type_bike = type_bike

    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_bike}")

# Membuat objek dari kelas Car dan Bike
car1 = Car("Toyota", "Corolla", 2020, 4)
bike1 = Bike("Yamaha", "YZF-R3", 2019, "Sport")

# Menampilkan informasi kendaraan
car1.display_info()
print()
bike1.display_info()

# Menggunakan polymorphism
vehicles = [Car("Honda", "Civic", 2018, 4), Bike("Ducati", "Panigale V2", 2021, "Sport")]

for vehicle in vehicles:
    print()
    vehicle.display_info()
