# Tentukan berapa hasil dari operasi +, -, *, /, %, // dan ** dari kedua variable di bawah!
# Lalu bandingkan hasil yang ada dengan nilai 30 dengan perbandingan >, <, ==, !=, >=, <= 

v1 = 3
v2 = 20

# OPERASI ARITMATIKA
print(v2 // v1)
print(v2 + v1)
print(v2 / v1)
print(v2 * v1)
print(v2 % v1)
print(v2 ** v1)

print('''   
''')

# OPERASI PERBANDINGAN - akann menghasilkan BOOLEAN -> TRUE atau FALSE
print(v2 + v1 < 30)
print(v2 + v1 > 30)
print(v2 / v1 == 30)
print(v2 * v1 != 30)
print(v2 % v1 <= 30)
print(v2 ** v1 >= 30)
print(v2 + v1 is 30)
print(v2 + v1 is not 30)

# teknik lain
v1 = 3
v2 = 20
v1 += 2
v2 -= 5

print(v2 + v1)


# Teks String pake operator aritmatika - menghasilkan 2x str
s = "Ini adalah string "
print(s * 2)

c = '*'
print(c * 100)

# Boolean pake operator aritmatika - True = 1 False = 0
b = True
print(b/2)