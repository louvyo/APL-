def func_pangkat(bilangan, pangkat):
    if pangkat == 0:
        return 1
    else:
        return bilangan * func_pangkat(bilangan, pangkat - 1)

pokok = int(input("Masukkan bilangan : "))
pangkat = int(input("Masukkan pangkat : "))
hasil_pangkat = func_pangkat(pokok, pangkat)
print(hasil_pangkat)