import numpy as np

# fungsi untuk menampilkan array dan rata-rata elemen
def display_array(array):
    print("Tampilan Array >>")
    print(array)
    print("Rata-rata elemen: ", np.mean(array))

# input dimensi array
dimensi = int(input("Masukkan banyak dimensi array [2/3]: "))

if dimensi == 2:
    # input baris dan kolom array
    baris = int(input("Masukkan banyak baris array: "))
    kolom = int(input("Masukkan banyak kolom array: "))

    # input elemen array
    array = np.zeros((baris, kolom))
    for i in range(baris):
        for j in range(kolom):
            array[i][j] = float(input(f"Masukkan elemen pada baris ke-{i+1}, kolom ke-{j+1}: "))

    # tampilkan array dan rata-rata elemen
    display_array(array)

elif dimensi == 3:
    # input baris, kolom, dan sisi array
    baris = int(input("Masukkan banyak baris array: "))
    kolom = int(input("Masukkan banyak kolom array: "))
    sisi = int(input("Masukkan banyak sisi array: "))

    # input elemen array
    array = np.zeros((baris, kolom, sisi))
    for i in range(baris):
        for j in range(kolom):
            for k in range(sisi):
                array[i][j][k] = float(input(f"Masukkan elemen pada baris ke-{i+1}, kolom ke-{j+1}, sisi ke-{k+1}: "))

    # tampilkan array dan rata-rata elemen
    display_array(array)
    
else:
    print("Dimensi array tidak valid.")
