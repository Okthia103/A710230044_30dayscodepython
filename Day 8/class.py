class kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def duduk(self):
        print(f"{self.nama} sekarang duduk")
    def berdiri(self):
        print(f"{self.nama} sekarang berdiri")
my_kucing = kucing("menzi",4)
print(f"kucingku bernama {my_kucing.nama}")
print(f"kucingku berumur {my_kucing.umur} tahun")
my_kucing.duduk()
my_kucing.berdiri()