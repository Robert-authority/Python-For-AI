def tebak_angka(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

angka = int(input("Masukkan angka: "))
hasil = tebak_angka(angka)
print(f"Angka {angka} adalah {hasil}")
