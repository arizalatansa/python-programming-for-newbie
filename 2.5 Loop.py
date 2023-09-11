# WHILE LOOP : LOOP (kemampuan mengulang) dimana akan terus berjalan bila kondisi adalah TRUE
count = 0
while (count < 100):
    print("Nilai count: ", count)
    count = count +1

print("Selamat tinggal")

# FOR LOOP : LOOP dimana untuk mengulangi item di dalam urutan seperti list atau string

list_angka = [1,2,3,4,5]

for x in list_angka:
    print(x)

# FOR ELSE 
daftar_murid = ['Angga', 'Jono', 'Tukiyem']

nama_murid = 'Angga'

for nama in daftar_murid:
    if nama == nama_murid:
        print(nama)
        break

else:
    print('Nama tidak ditemukan')

# Bonus : pass 

for nama in daftar_murid:
    pass # pass ini digunakan biasanya kalo mau tulis rumus banyak biar ga error kedetect merah
    if daftar_murid(3) == 'Angga':
        pass
    

# NESTED LOOP : LOOP untuk melakukan pengulangan di dalam LOOP

i = 90

while (i < 100):
    j = 2
    print(i/j)

    while (j <= (i/j)):
        print('Loop dalam loop!')
        j = j + 1
        i = i + 1

print('Selamat datang!')



# BREAK atau CONTINUE
# BREAK mengakhiri proses LOOP lanjut pada perintah berikutnya
# CONTINUE melewatkan proses 1 LOPP dan lanjut pada perintah yang sama sebelum lanjut ke perintah berikutnya

for val in "string":
    if val == "i":
        break

    print("sudah sudah cukup")

## hasilnya akan berhenti sebelum i menghasilkan 3 print

for val in "string":
    if val == "i":
        continue

    print("belum belum cukup")

print("Loop sudah capek")

## hasilnya akan berhenti pada 1 saja selanjutnya tetap lanjut menghasilkan 5 print

# latian belajar
# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
list_angka = list(range(1,120))
print(list_angka)

for x in list_angka:
    if x % 2 == 0:  
        print(x)

# membuat variable dengan range ditambah variabel 
a = range(100)
print(a)

a2 = list(range(100))
print(a2)

a3 = list(range(50,100))
print(a3)

a4 = list(range(2,100,2))
print(a4)

# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
list_angka = range(1,120)

for x in list_angka:
    if x == 12 or x == 56 or x == 78:
        continue
    print(x)

# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100

list_angka = range(1,120)

for x in list_angka:
    if x > 100 :
        break
    print(x)

# note : kalo LOOPing forever pencet saja di terminal ctrl + c 