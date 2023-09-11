class Cat:
    def __init__(self):
        self.nama = 'Meong'
        self.tipe = "Anggora"

    def forward(self):
        print("Kucing berlari ...")


class Bird:

    def __init__(self):
        self.nama = "Erago"
        self.tipe = " Elang"

    def forward(self):
        print("Burung terbang ...")

# fungsi umum utk Polimorphism

def melaju(objek):
    objek.forward()

# Objek

meong = Cat() ; erago = Bird() # bisa horizontal pake ;

# command 
melaju(meong)
melaju(erago)



# Setelah class mobil, buatlah satu class baru bernama motor
# Terapkan konsep Polimorphism yang sudah dipelajari dengan membuat satu fungsi umum bernama menampung()

class Mobil:
    def __init__(self, nama):
       self.nama = nama
    
    def run(self):
        print('Mboil ini mampu melaju hingga kecepatan 180 km/h')

class Motor:
    def __init__(self, nama):
       self.nama = nama
    
    def run(self):
        print('Motor ini mampu melaju hingga kecepatan 90 km/h')


# function polimorphism
def melaju(objek):
    objek.run()

# objek
fortuner = Mobil('Fortuner')
fazzio =  Motor('Fazzio')

# command
melaju(fortuner)
melaju(fazzio)