# READ
## untuk run file txt ini harus berada pada folder sesuai assign

#contoh :
## PS C:\Users\ariza> cd '.\Documents\Python Programming\Indonesia AI 
data = open("./File Handling.txt", mode = 'r', encoding='utf-8') # encoding recommended karena standar txt
print(data.read())

#ganti teks
string = data.read()
string = string.replace('adalah', 'merupakan')
print(string)

# APPEND
data = open("./File Handling.txt", mode = 'a', encoding='utf-8')
data.write("\nPemograman Python adalah salah satu yang paling menarik") # \n untuk enter pada text
data.write("\nUpskill diri dengan Python") # otomatis menambahkan teks pada txt

data.close() # ini adalah best practice karena menghilangkan memori yang terpakai

# WRITE
data = open("./File Handling.txt", mode = 'w', encoding='utf-8') # write menghapus data yang sudah ada dan menulis ulang
data.write('Yuk belajar bahasa pyhton')
data.write('\nMau jago harus sering latian')
data.write('\nBiar ga kalah sama jaman')
data.write('\ntapi inget akhirat')

data.close() # best practice

# Better Practice
try:
    data = open('./File Handling.txt', mode='w', encoding='utf-8')
finally:
    data.close()

# # Best Practice
with open('./File Handling.txt', mode='w', encoding='utf-8') as data: #otomastis ketika selesai ga perlu close()
    # bisa diisi kodingan apa saja
    data.read()
    data.write()
    pass


# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!

data = open("./File Handling.txt", mode='a', encoding='utf-8')
data.write('\nTernyata File Handling itu Mudah, Alhamdulillah')

data.close()