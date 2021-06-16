'''
2. Buatlah sebuah program yang dapat menghitung luas lingkaran.
    Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
    Program menghitung luas lingkaran dengan rumus phi r2

    phi = 22/7
    r = jari=jari lingkaran
    Lalu tampilkan ke layar dengan format:
    Hint: untuk menampilkan tanda kuadrat gunakan print("\u00b2")

    Luas lingkaran dengan jari-jari [jari-jari lingkaran] cm adalah [luas lingkaran] cm2.

    Contoh: 
    Luas lingkaran dengan jari-jari 7 cm adalah 154.00 cm2.
    Luas lingkaran dengan jari-jari 10 cm adalah 314.2857142857143 cm2.

    Bonus: Ubahlah format luas menjadi 2 angka dibelakang koma
    Hint: Ubah string format untuk float menjadi {:.2f}

    Luas lingkaran dengan jari-jari 10 cm adalah 314.29 cm2. 
'''

phi = 22/7
r = float(input("Masukan nilai jari-jari lingkaran yang diinginkan: "))

luas_lingkaran = phi * (r ** 2)

print(
    f"Luas lingkaran dengan jari-jari {r} cm adalah {luas_lingkaran:.2f} cm\u00b2")
