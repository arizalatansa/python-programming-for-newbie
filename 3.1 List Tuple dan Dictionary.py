# List

list1 = ['Apple','Watermelon','Banana']
list2 =[1,5,3,2,4,9]
list2a =[1,1,2,2,3,3]
list3 = [True,False,True,False,False]
list4 = ["abc",123,True]
list5 = [list1, list2, list3, list4] # bikin list dalam list
print(list5)
print(list2+list2a)

# sort ASC 
list2.sort() #sorting ASC
print(list2)

list1.sort()
print(list1)

# sort DESC 
list2.reverse()
print(list2)

list1.reverse()
print(list1)

# COPY
list6 = list4.copy()
print(list6)

# COUNT 
print(list3.count(True))

# INDEXING 
fruit_list = ['Jeruk','Mangga','Pir','Semangka','Anggur','Manggis','Pepaya','Alpukat']
print(fruit_list[1])
print(fruit_list[1:4])
print(fruit_list[-2])
print(fruit_list[-4:])

# EDIT ELEMENT
(fruit_list[1]) = 'Ceri'
print(fruit_list)

# MEMBERSHIP TEST 
print('Mangga' in fruit_list)
print('Ceri' in fruit_list)
print('Pepaya' not in fruit_list)

# ADDITION ELEMENT
fruit_list = ['Jeruk','Mangga','Pir']
fruit_list.append('Kelapa') # pake append() - nambah dipaling kanan
print(fruit_list)

fruit_list = ['Jeruk','Mangga','Pir']
fruit_list.insert(2, 'Pisang') # pake insert() - sisihkan di urutan tertentu
print(fruit_list)

fruit_list1 = ['Jeruk','Mangga']
fruit_list2 = ['Kates','Pir']
fruit_list1.extend(fruit_list2) # pake extend() - gabung 2 list
print(fruit_list1)

# REMOVE ELEMENT 
fruit_list = ['Jeruk','Mangga','Pir','Semangka','Anggur','Manggis','Pepaya','Alpukat']
fruit_list.remove('Jeruk') # pake remove() - hapus berdasar element
print(fruit_list)

fruit_list = ['Jeruk','Mangga','Pir','Semangka','Anggur','Manggis','Pepaya','Alpukat']
fruit_list.pop(4) # pake pop() - hapus berdasar urutan
print(fruit_list)

fruit_list = ['Jeruk','Mangga','Pir','Semangka','Anggur','Manggis','Pepaya','Alpukat']
del fruit_list[2:5] # pake del - bisa sampe hapus list
print(fruit_list)

fruit_list.clear() # pake clear() - membuat list kosong
print(fruit_list)

# TUPLE
tuple1 = ('Apple','Watermelon','Banana')
tuple2 = (1,5,3,2,4,9)
tuple2a =(1,1,2,2,3,3)
tuple3 = (True,False,True,False,False)
tuple4 = ("abc",123,True)
tuple5 = (tuple1, tuple2, tuple3, tuple4) # bikin list dalam list
print(tuple5)
print(tuple2+tuple2a)

# INDEXING sama dengan list
# Beda dengan list adalah tuple tidak bisa di ADD, EDIT, REMOVE (bersifat immutable alias permanen)
# secara kecepatan proses tuple lebih cepat daripada list

# tuple1[1] = 4
# print(tuple1) #TypeError: 'tuple' object does not support item assignment
# del tuple1[1:5]
# print(tuple1)

# bisa pake loop for atau while
for tuple in tuple1:
    print('Buah yang kamu suka: ', tuple)

# DICTIONARY
fruit_dict = {'nama' : 'pisang',
              'jenis' : 'ambon',
              'kode' : 771,
              'harga' : 17000}
print(fruit_dict)
print(fruit_dict['nama'])

fruit_dict['nama'] = 'jeruk' # ga bisa pake koma terus ganti jenis
fruit_dict['jenis'] = 'Bali'
fruit_dict['harga'] = 1000
print(fruit_dict)

# LOOP DICTIONARY 
for key, value in fruit_dict.items(): # untuk loop key dan value
    print(key, value)

for key in fruit_dict.keys(): # untuk loop key saja
    print(key)

for key in fruit_dict.keys(): # untuk loop key dan value 
    print(key, fruit_dict[key]) 

# DICTIONARY tidak bisa di dalam dictionary, bila ada lebih dari 2 dictionary, akan ditampung di dalam list atau tuple

fruit_dict = [{'nama' : 'pisang',
              'jenis' : 'ambon',
              'kode' : 771,
              'harga' : 17000},
                {'nama' : 'jeruk',
              'jenis' : 'bali',
              'kode' : 721,
              'harga' : 15000}]
print(fruit_dict)

# SET - seperti himpunan pada matematika
A = {1,2,3,4,5,6}
B = {6,7,8,9,10,11}

# UNION - seperti full join
print(A | B)

# INTERSECTION - seperti inner join 
print(A & B)

# DIFFERENCE - seperti right atau left join tapi ga pake inner
print(A - B)
print(B - A)

# SIMETRIC DIFFERENCE - seperti full join tapi ga pake inner
print(A ^ B) 



# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = {"nama" : "Arizal",
              "status" : "aktif",
              "nilai IPK" : 3.59,
              "universitas" : "UT",
              }
dict_karyawan = {"nama" : "Arif",
              "status" : "pensiun",
              "grade" : "B",
              "kantor" : "Pajak"}

print(dict_murid["status"])
print(dict_karyawan["status"])

print(dict_karyawan['kantor'])
print(dict_murid['nilai IPK'])

for murid in dict_murid:
    print(murid)

for karyawan in dict_karyawan:
    print(karyawan)