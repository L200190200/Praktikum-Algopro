Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Fatmawati Ersa Putri"
>>> NIM = 200
>>> Tinggi = 1.62
>>> Berat = 52
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena data "Aku" ditulis dengan menggunakan tanda kurung biasa dan item di dalamnya tidak dapat diubah
>>> Aku[0]
2001
>>> #Karena item pertama dari data "Aku" adalah "TahunLahir", dan nilai dari "TahunLahir" adalah 2001
>>> a = NIM % 4; Aku[a]
2001
>>> #Karena sisa hasil bagi dari 200 dibagi 4 adalah 0, jadi hasil dari Aku[0] adalah 2001
>>> type(Aku[a])
<class 'int'>
>>> #Karena Aku[0] adalah "TahunLahir" dan nilainya 2001, 2001 adalah tipe data integer
>>> Aku[a:4]
(2001, 52, 1.62, 200)
>>> #Karena 4 item pertama dari data "Aku" adalah "TahunLahir", "Berat", "Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena item kelima dari data "Aku" adalah "Nama", dan nilai dari "Nama" adalah "Fatmawati Ersa Putri" yang termasuk kedalam tipe data string
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Karena isi tuple tidak dapat diubah (immutable) sehingga terjadi error
>>> type(Data)
<class 'list'>
>>> #Karena data "Data" ditulis dengan menggunakan kurung siku dan koleksi item di dalamnya dapat berubah, bertambah, dan berkurang secara dinamis
>>> type(Data[4])
<class 'str'>
>>> #Karena item kelima dari data "Data" adalah "Nama", dan nilai dari "Nama" adalah "Fatmawati Ersa Putri"
>>> Data[4][5]
'w'
>>> #Karena Data[4] atau objek kelima dari "Data" adalah "Nama" dan indeks 5 dari "Nama" adalah "w"
>>> Data[4][a:6]
'Fatmaw'
>>> #Karena Data[4] adalah "Nama" dan Nama[0:6] adalah objek pertama sampai objek keenam dari data "Nama" yaitu "Fatmaw"
>>> Data[0] = "ok"; Data
['ok', 52, 1.62, 200, 'Fatmawati Ersa Putri']
>>> #Karena list merupakan tipe data koleksi dimana objeknya dapat berubah (mutable)
>>> Data[-a]
'ok'
>>> #Karena a adalah 0, jadi indeks 0 dari "Data" adalah objek pertama yaitu "ok"
>>> range(a)
range(0, 0)
>>> #Karena a adalah 0, jadi range(0) menghasilkan range 0 sampai 0
