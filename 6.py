a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Mencari nilai terbesar dari ketiga bilangan
max_num = max(a, b, c)

# Cek apakah bilangan tripel Pythagoras
if max_num == a:
    is_tripel = a ** 2 == b ** 2 + c ** 2
elif max_num == b:
    is_tripel = b ** 2 == a ** 2 + c ** 2
else:
    is_tripel = c ** 2 == a ** 2 + b ** 2

# Tampilkan hasil
if is_tripel:
    print("Bilangan yang dimasukkan adalah bilangan tripel Pythagoras.")
else:
    print("Bilangan yang dimasukkan bukan bilangan tripel Pythagoras.")
