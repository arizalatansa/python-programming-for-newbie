# Buatlah satu logika kondisi yang menentukan jika harga laptop sekian maka 
# saya akan mempertimbangkan lagi jika harga handphone sekian maka saya akan beli keduanya atau tidak
# Gunakan teknik NESTED IF!

harga_laptop = 10000000
harga_handphone = 5000000
print("Saya akan beli laptopnya.")

# satu logika
if harga_laptop < 15000000:
    print("Saya akan beli laptopnya.")

# berurutan pilihan logika
if harga_laptop > 10000000:
    print('Gak Jadi beli laptop')
elif harga_handphone > 5000000:
    print('Gak jadi beli handphone')
else:
    print('ditabung aja dah duitnya')

# IF - PASS (melewati perintah)
a = 11

if a > 10:
    pass
if a < 10:
    print('di luar kondisi')

# elif
score = 78

if score > 90:
    print('mumtaz')

elif score <= 90 or score >= 70:
    print('ya mayanlah')

else:
    print

# nested if 
## budget cuma 15000000 mau beli laptop sama hape
### kalo nested if yang dibaca adalah yang paling luar dulu baru ke dalam
harga_laptop = 15000000
harga_handphone = 4000000

if harga_laptop < 10000000:

    if harga_handphone < 5000000:
        print('Saya akan beli keduanya')
    
    else:
        print('Saya cuma akan beli laptop')

else:
    if harga_handphone < 5000000:
        print('saya akan beli handpone saja')
    else:
        print("Saya tidak akan beli keduanya.")


# input pada IF
num = float(input('masukkan angka berapa saja: '))

if num  == 7:
    print('Selamat : Anda beruntung')

else:
    print('silahkan coba lagi!')