# Struktur syntax - fungsi non parameter

def halo_dunia(): # def untuk mendefinisikan fungsi
    var = 'Halo python, akhirnya bisa python' # blok kode
    print(var)

# pemanggilan fungsi
halo_dunia()

# struktur syntax - fungsi parameter

def nama_siswa(nama, asal):
    var2 = f'Halo, selamat datang {nama} yang berasal dari {asal}'
    print(var2)

# pemanggilan fungsi
nama_siswa('Ijat', 'Kampung')
nama_siswa(asal = 'Jababeka', nama = 'Supri')

## fungsi parameter untuk banyak variable dalam sekali eksekusi
def selamat_datang(*daftar_nama): # harus pake *

    var = 'Halo '
    for nama in daftar_nama:
        var += nama + ', '

    var += ' welcome!' # var = var + ' welcome'
    print(var)

selamat_datang('nurul', 'ajib', 'anjay')


# fungsi anonim - fungsi tanpa nama dengan keyword (lambda)
triple = lambda x: x * 3
print(triple(5))

# DOCSTRING 

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk docstring
    paham sekarang?
    '''
    var = f'Halo {nama}, selamat datang'
    print(var)

selamat_datang('kamu')
print(selamat_datang.__doc__)

# SCOPE and RETURN 
a=5 #scope berarti adalah ruang aktif walau sama sama nama variable a 

def matematika(a,b,c=2): # c didefinisikan tetap
    angka1 = a + b
    angka2 = angka1 // c
    
    print('angka di dalam funtion:', a) 

    return angka2 #mengembalikkan angka 

hasil = matematika(a=10, b=5) #scope berarti adalah ruang aktif walau sama sama nama variable a 
print(hasil)

print(a)
print('Angka diluar function: ', a)

# apabila ada variable dari scope terluar maka kalo di print di scope dalam akan terdeteksi, namun tidak sebaliknya



# tugas
# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut
angka1 = 12
angka2 = 8

def cek_modulus(a, b):
    angka1 = a * b
    angka2 = angka1 % a
    return angka2

hasil = cek_modulus(a=12, b=8)
print(hasil)