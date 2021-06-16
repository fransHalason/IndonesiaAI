'''
1. Buatlah sebuah program yang dapat menyimpan kontak dan juga menampilkan kontak-kontak
tersebut. Setiap kontak terdiri dari nama dan nomor telepon. Saat menjalankan program,
program akan menampilkan pesan sambutan dan juga menampilkan menu. Program akan
secara otomatis kembali menu apabila user telah selesai melihat kontak ataupun menambahkan
kontak.

Selamat datang!

--- Menu ---
1. Daftar Kontak
2. Tambah Kontak
3. Keluar

Program akan meminta user untuk memilih menu yang disediakan.
Pilih menu:

Jika user memilih menu 1, maka program akan menampilkan seluruh data kontak yang telah
disimpan. Contoh apabila program memiliki 2 data:
Daftar kontak:
Nama: Farhan
No Telepon: 08123456789
Nama: Joko
No Telepon: 08987654321

Jika user memilih menu 2, maka program akan meminta user untuk memasukkan data yang
dibutuhkan untuk menambahkan kontak.
Nama:
No Telepon:

Apabila kontak sudah ditambahkan, berikan konfirmasi kepada user bahwa kontak telah berhasil
ditambahkan.
Kontak berhasil ditambahkan

Jika user memilih menu 3, maka program akan berhenti dan menampilkan pesan ke layar.
Program selesai, sampai jumpa!

Jika user memasukkan pilihan menu yang tidak tersedia, maka program akan menampilkan
pesan, kemudian kembali ke menu.
Menu tidak tersedia
'''

# Program Kontak
# List Kontak
nama_kontak = ['Farhan', 'Joko']
nomor_telepon = ['08123456789', '08987654321']

# fungsi untuk menampilkan kontak yang tersimpan di list kontak
def daftar_kontak():
    print('Daftar Kontak:')
    for i in range(len(nama_kontak)):
        print('Nama: {}'.format(nama_kontak[i]))
        print('No Telepon: {}'.format(nomor_telepon[i]))

# fungsi untuk menambahkan kontak
def tambah_kontak():
    nama_kontak.append(input('Nama: '))
    nomor_telepon.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('--- Menu ---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        daftar_kontak()
    elif menu == 2:
        tambah_kontak()
    elif menu == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia.')
