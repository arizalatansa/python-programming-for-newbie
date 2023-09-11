# GrandParent Class bahkan bisa dibuat
# Parent Class
class Animal:

    def __init__(self):
        self.tipe = "Mamalia" # tipe parent
        self.kecepatan = "Cukup cepat"

    def grow(self):
        print("Mamalia berutmbuh selayaknya manusia")

# Child Class 1
class Cat(Animal): # disini fungsi pewarisannya

    def __init__(self, nama, tipe):

        super().__init__() # super init untuk mewariskan attribute dan method parent class nya

        self.nama = nama
        self.tipe = tipe # tipe child

    def run(self):
        print(f"Kucing {self.nama} berlari kencang sekali")

# Objek

kinako = Cat('Kinako', 'Anggora')
minto = Cat('Minto', 'Persia')

# command dari parent
print(minto.kecepatan)
print(kinako.tipe) # overriding # hasil anggora bukan mamalia
kinako.grow()

# command dari child
kinako.run()
minto.run()

# Child Class 2

class Dog(Animal):
    
    def __init__(self, nama, tipe):

        super().__init__() # super init untuk mewariskan attribute dan method parent class nya

        self.nama = nama
        self.tipe = tipe # tipe child

    def run(self):
        print(f"Anjing {self.nama} berlari kencang sekali")

# Objek
doggy = Dog('Doggy', 'Siberian')
gukguk = Dog('Gukguk', 'Husky')

# command dari parent
print(doggy.kecepatan)
print(gukguk.tipe) # overriding # hasil anggora bukan mamalia
doggy.grow()

# command dari child
gukguk.run()
doggy.run()

# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki parent class bernama Kendaraan
# Pastikan parent class tersebut memiliki setidaknya 2 attributes dan 2 methods yang akan diturunkan ke child class
# Jangan lupa menggunakan super() pada child class

# Parent Class
class Kendaraan:
    def __init__(self):
        self.roda = "Kendaraan bisa beroda 2, 3, 4 bahkan lebih"
        self.seat = "Kendaraan mempunyai seat untuk penumpangnya"
    
    def fungsi(self):
        print("Kendaraan berfungsi untuk mengantarkan orang atau barang dari satu tempat ke tempat lain")

# Child Class

class Mobil(Kendaraan):
    '''
    Ini adalah kelas Mobil yang dibuat untuk uji coba
    '''
    type = 'SUV'

    def __init__(self, nama):
        
        super().__init__()

        self.nama = nama
        self.__tahun_buat = "2020"
        self.__bensin = "Diesel"
    
    def run(self, speed):
        print(f'{self.nama} mampu melaju hingga kecepatan {speed} km/h')
    
    def service(self, per_bulan):
        print(f'{self.nama} perlu setidaknya dilakukan service per {per_bulan} bulan sekali')

    def on(self, day):
        print(f'Normalnya {self.nama} harus dipanasi tiap per {day} hari sekali')

    # getter
    def lihatTahunBuat(self):
        print(f'{self.nama} dibuat pada tahun {self.__tahun_buat}')
    
    def lihatBensin(self):
        print(f'{self.nama} harus diisi bensin dengan jenis {self.__bensin}')

    #setter
    def aturTahunBuat(self, tahun_buat):
        self.__tahun_buat = tahun_buat
    
    def aturBensin(self, bensin):
        self.__bensin = bensin

# objek
fortuner = Mobil('Fortuner')

print(fortuner.roda)
print(fortuner.seat)

fortuner.fungsi()

# command parent