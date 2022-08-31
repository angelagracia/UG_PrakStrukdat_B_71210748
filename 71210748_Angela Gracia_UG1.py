#menambahkan dua bilangan
def penambahan(a, b):
    return a + b
#mengurangi dua bilangan
def pengurangan(a, b):
    return a - b
#mengali dua bilangan
def perkalian(a, b):
    return a * b
#membagi dua bilangan
def pembagian(a, b):
    return a / b

print("Memilih Oprasi")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    #input user
    pilih = input("Masukkan pilihan(1/2/3/4): ")

    #chek pilihannya antara 1-4 atau bukan
    if pilih in ("1", "2", "3", "4"):
        nomor1 = float(input("Masukkan bilangan pertama: "))
        nomor2 = float(input("Masukkan bilangan kedua: "))

        if pilih == "1":
            print(nomor1, "+", nomor2, "=", penambahan(nomor1, nomor2))
        elif pilih == "2":
            print(nomor1, "-", nomor2, "=", pengurangan(nomor1, nomor2))
        elif pilih == "3":
            print(nomor1, "*", nomor2, "=", perkalian(nomor1, nomor2))
        elif pilih == "4":
            print(nomor1, "/", nomor2, "=", pembagian(nomor1, nomor2))
        elif pilih == "Q":
            print("Program dihentikan")
            break
        else:
            print("Pilihan tidak tersedia")
