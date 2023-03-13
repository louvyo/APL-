print("Program Menampilkan Matriks Segitiga Atas dan Bawah")
print("---------------------------------------------------\n")

a = []

x = int(input("Masukkan angka segitiga atas  : "))
y = int(input("Masukkan angka segitiga bawah : "))
print(f"\nMatriks segitiga atas & bawah ordo {5}x{5} >>\n")

for i in range(5):
    a.append([])

for i in range(5):
    for j in range(5):
        if i == j:
            a[i].append(0)
        elif i < j:
            a[i].append(x)
        elif i > j:
            a[i].append(y)

for i in range(5):
    print(a[i])