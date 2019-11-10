## Program Akun
## Dibuat oleh Fatmawati Ersa Putri L200190200
import random
angka = random.randint(0,1000)

Nama = "Fatmawati Ersa Putri"
TanggalLahir = "30 Maret 2001"
NamaSingkat = Nama[0] + "." + Nama[10] + "." + Nama[15:20]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[9:13]
Password = Nama[0:3] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)


