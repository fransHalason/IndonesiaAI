'''
3. Buatlah program untuk menentukan apakah seorang siswa lulus ujian atau tidak.
    Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktik minimal 70.
    Program menerima input berupa nilai ujian teori dan praktik, nilai ujian dapat berupa bilangan desimal.

    Jika nilai ujian teori dan praktik minimal 70, maka program akan menampilkan:
    "Selamat, Anda lulus!"
    Jika nilai ujian teori minimal 70 dan nilai ujian praktik kurang dari 70:
    "Anda harus mengulang ujian praktik."
    Jika nilai ujian praktik kurang dari 70 dan nilai ujian praktik minimal 70:
    "Anda harus mengulang ujian teori."
    Jika nilai ujian teori dan ujian praktik kurang dari 70:
    "Anda harus mengulang ujian teori dan praktik."
'''

nilai_teori = float(input("Masukkan nilai ujian teori: "))
nilai_praktik = float(input("Masukkan nilai ujian praktik: "))

if nilai_teori >= 70 and nilai_praktik >= 70:
    print("Selamat, Anda lulus!")
elif nilai_teori >= 70 and nilai_praktik < 70:
    print("Anda harus mengulang ujian praktik.")
elif nilai_teori < 70 and nilai_praktik >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktik.")
