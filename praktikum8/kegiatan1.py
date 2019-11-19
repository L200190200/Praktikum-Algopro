Data = {"NIM":"L200190200", "Nama":"Fatmawati Ersa Putri", "Tempat/Tanggal_lahir":"Wonogiri, 30 Maret 2001", "Jenis Kelamin":"Perempuan", "Agama":"Islam",
        "Pekerjaan":"Mahasiswa", "Alamat":"jatisrono, Wonogiri, Jawa Tengah"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilTTL():
    print(Data["Tempat/Tanggal_lahir"])
def TampilJK():
    print(Data["Jenis Kelamin"])
def TampilAgama():
    print(Data["Agama"])
def TampilAlamat():
    print(Data["Alamat"])
def TampilPekerjaan():
    print(Data["Pekerjaan"])

print("Pilihan Yang Tersedia:")
print("a menampilakan bantuaan ini")
print("b menampilakan NIM")
print("c menampilakan Nama")
print("d menampilakan Tempat/Tanggal_lahir")
print("e menampilakan Jenis Kelamin")
print("f menampilakan Agama")
print("g menampilakan Alamat")
print("h menampilakan Pekerjaan")
print("i untuk keluar")
print(" ")

a = """Pilihan Yang Tersededia:
a menampilakan bantuaan ini
b menampilakan NIM
c menampilakan Nama
d menampilakan Tempat/Tanggal_lahir
e menampilakan Jenis Kelamin
f menampilakan Agama
g menampilakan Alamat
h menampilakan Pekerjaan
i untuk keluar"""

i = "Terima Kasih"
x = input("Masukkan huruf:")
while x != "i":
    if x == "a":
        print(a)
        print(" ")
        x = input("Masukkan huruf:")
    elif x == "b":
        TampilNIM()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "c":
        TampilNama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "d":
        TampilTTL()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "e":
        TampilJK()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "f":
        TampilAgama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "g":
        TampilAlamat()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "h":
        TampilPekerjaan()
        print(" ")
        x = input("Masukkan huruf")
print(i)
