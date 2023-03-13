# Membuat Matriks
M = int(input("Masukkan banyak Baris : "))
N = int(input("Masukkan banyak kolom : "))
Matriks = []

for i in range(M):
    a = []
    for j in range(N):
        a.append(int(input(f"Masukkan baris ke-{i+1} kolom ke-{j+1} : ")))
    Matriks.append(a)
# Menampilkan Nilai Matriks
for v in Matriks:
    print(v)

jml = 0
ordo = M * N
maks = max(Matriks)
minimal = min(Matriks)
for i in range(len(Matriks)):
    for j in range(len(Matriks[i])):
        jml = jml + Matriks[i][j]
rata_rata = jml/ordo
print("Nilai Maks.nya adalah ", max(maks))
print("Nilai Min. nya adalah ", min(minimal))
print("Nilai Rata-rata nya adalah ", rata_rata)
