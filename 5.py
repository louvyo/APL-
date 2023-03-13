# def menentukan bentuk segitiga
def bentuk_segitiga(sisi1, sisi2, sisi3):

    # Segitiga sama sisi
    if sisi1 == sisi2 and sisi1 == sisi3 and sisi2 == sisi3:
        print("Bentuk: segitiga sama sisi")

    # Segitiga sama kaki
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("Bentuk: segitiga sama kaki")

    # Segitiga siku-siku
    elif sisi1**2 + sisi2**2 == sisi3**2 or sisi1**2 + sisi3**2 == sisi2**2 or sisi2**2 + sisi3**2 == sisi1**2:
        print("Bentuk: segitiga siku-siku")

    # Segitiga sembarang
    elif (sisi1 != sisi2 and sisi1 != sisi3 and sisi2 != sisi3) and (sisi1**2 + sisi2**2 != sisi3**2 or sisi1**2 + sisi3**2 != sisi2**2 or sisi2**2 + sisi3**2 != sisi1**2):
        print("Bentuk: segitiga sembarang")

# def menentukan apakah segitiga dapat dibuat atau tidak
def cek_segitiga(sisi1, sisi2, sisi3):

    # segitiga tidak dapat terbentuk
    if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1:
        print("Ketiga sisi tersebut tidak dapat membentuk segitiga")

    # Bisa membentuk segitiga
    else:
        print("Ketiga sisi tersebut dapat membentuk segitiga")
        bentuk_segitiga(sisi1_Temp, sisi2_Temp, sisi3)

# Segitiga
sisi1_Temp = float(input("Sisi 1 = "))
sisi2_Temp = float(input("Sisi 2 = "))
sisi3_Temp = float(input("Sisi 3 = "))
cek_segitiga(sisi1_Temp, sisi2_Temp, sisi3_Temp)
