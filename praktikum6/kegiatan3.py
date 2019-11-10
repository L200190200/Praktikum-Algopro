Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Fatmawati Ersa Putri"
>>> NIM = "L200190200"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi type data integer
>>> type(b)
<class 'int'>
>>> #Karena data "Nama" memiliki instruksi "len"
>>> a / b
60.0
>>> #Karena hasil dari 1200 dibagi dengan 20 hasilnya 60.0
>>> a // b
60
>>> #Karena arti dari "//" adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
2010
>>> #Karena nilai "a" dikurangi 999 hasilnya adalah 201, kemudian 201 dikalikan dengan 10 menghasilkan nilai 2010
>>> b ** 2
400
>>> #Karena arti dari "**" adalah perpangkatan, maka nilai "b" dipangkatkan dengan 2 menghasilkan nilai 400
>>> a % b
0
>>> #Karena arti dari "%" adalah sisa hasil bagi, maka nilai "a" dibagi nilai "b" hasilnya tidak bersisa, maka jawabannya adalah 0
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Karena 12.5 adalah bilangan desimal sehingga termasuk ke dalam type data float
>>> a / c
96.0
>>> #Karena hasil dari 1200 dibagi 12.5 adalah 96.0
>>> a // c
96.0
>>> #Karena arti dari "//" adalah pembagian dengan pembulatan ke bawah
>>> a % c
0.0
>>> #Karena arti dari "%" adalah sisa hasil bagi, dan sisa dari 1200 dibagi dengan 12.5 adalah sisanya 0.0
>>> c > b
False
>>> #Karena nilai "c" =12.5 lebih besar dari nilai "b" =20 adalah salah
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki dua kemungkinan yaitu True atau False
>>> a > b and b > c
True
>>> #Karena logika "DAN" True and True menghasilkan nilai True
>>> a > 1100 or b < 10
True
>>> #Karena logika "ATAU" True or False menghasilkan nilai True
