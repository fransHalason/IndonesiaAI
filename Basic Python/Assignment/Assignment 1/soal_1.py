'''
1. Buat sebuah program yang menerima 3 input user.
    Input tersebut berupa:
    a. Nama bertipe data string
    b. Umur bertipe data integer
    c. Tinggi bertipe data float

    Lalu tampilkan ke layar dengan format:
    Nama saya [Nama], umur saya [Umur] tahun dan tinggi saya [Tinggi] cm.

    Contoh:
    Nama Saya Farhan, umur saya 23 tahun dan tinggi saya 167.5 cm.
'''

nama = str(input("Masukkan nama lengkap Anda: "))
umur = int(input("Masukkan umur Anda saat ini: "))
tinggi = float(input("Masukkan tinggi Anda: "))
print("Nama saya {}, umur saya {} dan tinggi saya {} cm.".format(nama, umur, tinggi))
# print(f"Nama saya {nama}, umur saya {umur} dan tinggi saya {tinggi} cm.")