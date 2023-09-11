# Encapsulation atau pengkapsulan : agar Class tidak mudah dirubah oleh pihak luar

class Motor:

    def __init__(self, plat):

        self.plat = plat
        self.tipe = "Fazzio"
        self.bensin = 4.5 # liter
    
    # getter / lihat

    # setter / atur

fazzio = Motor(plat="B 1234 ARZ")


print(fazzio.bensin)

# mudah dirubah langsung

fazzio.bensin = 2
print(fazzio.bensin)


# PROTEKSI ENCAPSULATION
class Motor:

    def __init__(self, plat):

        self.__plat = plat # '__' adalah proteksi
        self.__tipe = "Fazzio" # '__' adalah proteksi
        self.__bensin = 4.5 # liter # '__' adalah proteksi
    
    # getter / lihat # utk akses yang terproteksi
    def lihatMaksimumBensin(self):
        print(f'Maksimum bensin untk {self.__tipe} adalah {self.__bensin} liter')
    
    # setter / atur # utk akses yang terproteksi
    def aturMaksimumBensin(self, bensin):
        self.__bensin = bensin

fazzio = Motor(plat="B 1234 ARZ")

# print(fazzio.__plat) # tidak bisa di akses langsung pasti gagal
# print(fazzio.__bensin) # tidak bisa diakse langsung pasti gagal

# mudah dirubah langsung

fazzio.__bensin = 2
print(fazzio.__bensin) # tidak akses class tapi akses variabel di atas

# command getter
fazzio.lihatMaksimumBensin()

# command Setter
fazzio.aturMaksimumBensin(5)
fazzio.lihatMaksimumBensin()


# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki fungsi setter & getter
# Pastikan fungsi tersebut memungkinkan kita untuk memodifikasi semua attributes yang dimiliki oleh class tersebut

# buat class
class Mobil:
    '''
    Ini adalah kelas Mobil yang dibuat untuk uji coba
    '''
    type = 'SUV'

    def __init__(self, nama):
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
    

# buat objek
fortuner = Mobil('Fortuner')

# getter
fortuner.lihatBensin()
fortuner.lihatTahunBuat()

# setter
fortuner.aturBensin("Pertamax Plus")
fortuner.aturTahunBuat("2010")

fortuner.lihatBensin()
fortuner.lihatTahunBuat()