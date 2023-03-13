Matriks = []

for i in range(2):
    a = []
    for j in range(2):
        a.append(int(input(f"Masukkan baris ke-{i+1} kolom ke-{j+1} : ")))
    Matriks.append(a)

print("\nMatriks : ")
for v in Matriks:
    print(v)

# determinan
deter = Matriks[0][0]*Matriks[1][1] - (Matriks[0][1]*Matriks[1][0])

# adjoin
Matriks_adjoin = []

Matriks_adjoin.append([Matriks[1][1], -Matriks[0][1]])
Matriks_adjoin.append([-Matriks[1][0], Matriks[0][0]])

if deter == 0:
    print("Matriks tidak memiliki invers")
else:
    hasil_matriks = []

    hasil_matriks.append([deter * Matriks_adjoin[0][0], deter * Matriks_adjoin[0][1]])
    hasil_matriks.append([deter * Matriks_adjoin[1][0], deter * Matriks_adjoin[1][1]])


    print("\n\n Invers matriks :")
    print(f"[{hasil_matriks[0][0]} {hasil_matriks[0][1]}]" )
    print(f"[{hasil_matriks[1][0]} {hasil_matriks[1][1]}]" )