class Mobil:
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model
    
    def move(self):
        print(f"{self.merek} {self.model} bergerak di jalan.")

class Pesawat:
    def __init__(self, maskapai, tipe):
        self.maskapai = maskapai
        self.tipe = tipe
    
    def move(self):
        print(f"{self.maskapai} {self.tipe} terbang di udara.")

class Kapal:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    def move(self):
        print(f"Kapal {self.nama} {self.jenis} berlayar di laut.")

# Membuat objek dari kelas Mobil, Pesawat, dan Kapal
mobil1 = Mobil("Toyota", "Avanza")
pesawat1 = Pesawat("Garuda", "Boeing 737")
kapal1 = Kapal("Nusantara", "Ferry")

# Memanggil metode move dari masing-masing objek
mobil1.move()
pesawat1.move()
kapal1.move()
