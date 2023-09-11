# Definisikan Class
class Cat: # kalo pake class pake capital di depan, kalo def pake snake case
    '''
    Ini adalah class untuk membuat objek kucing
    Melalui kelas ini kita bisa medefinisikan nama dan juga tipe kucing
    '''
    # dalam class dibutuhkan attribute/sifat dan method(yang dilakukan)
    spesies = 'Kucing' # variable

    def __init__(self, nama, tipe): # function # pake __init__ utk buat attibute # __init__ sebagai constructor atau inisiator
        self.nama = nama # setting parameter
        self.tipe = tipe # setting parameter

    def run(self, speed): # km/h
        print(f'Kucing {self.nama} berlari dengan kecepatan {speed} km/h')


    def sleep(self, time): # menit
        print(f'Kucing {self.nama} tidur selama {time} menit')

    def passive(self):
        print(f'Kucing {self.nama} sukanya menyendiri')

# Objek
moka = Cat(nama='Moka', tipe='Oren') # Moka menjadi Objek Moka mendefenisikan Cat 

# Command
print(moka.__doc__) # docstring
print(moka) # menunjukan moka itu masuk class Cat
print(moka.spesies) # untuk memanggil attribute diperlukan print
print(moka.nama)
print(f'Kucing ini namanya {moka.nama}')
print(moka.tipe)
print(f'Kucing {moka.nama} merupakan salah satu jenis dari kucing {moka.tipe}')
moka.sleep(time= 30) # untuk memanggil method tidak dibutuhkan print, perlakuan seperti function
moka.run(speed= 90)
moka.passive()

# hapus attribute ataupun class bisa pake statement 'del'

# Definiskan Class
class Employee():
    '''
    Ini adalah Class untuk memanipulasi data employee
    Melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    '''

    def __init__(self, lokasi_file):

        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):

        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):

        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):

        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])

# Membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

# Abstract Object
class RandomForest():
    pass

# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

# Definisikan Class
class Mobil:
    '''
    Ini adalah kelas Mobil yang dibuat untuk uji coba
    '''
    type = 'SUV'

    def __init__(self, nama, tahun_buat, bensin):
        self.nama = nama
        self.tahun_buat = tahun_buat
        self.bensin = bensin
    
    def run(self, speed):
        print(f'{self.nama} mampu melaju hingga kecepatan {speed} km/h')
    
    def service(self, per_bulan):
        print(f'{self.nama} perlu setidaknya dilakukan service per {per_bulan} bulan sekali')

    def on(self, day):
        print(f'Normalnya {self.nama} harus dipanasi tiap per {day} hari sekali')

# buat objek
fortuner = Mobil('Fortuner','2020','Diesel')

# command
print(fortuner.__doc__)
print(fortuner.type)
print(fortuner.nama)
print(fortuner.tahun_buat)
print(fortuner.bensin)

fortuner.run(200)
fortuner.service(3)
fortuner.on(4)