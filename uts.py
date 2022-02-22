print('penjualan tiket')
nama_ =input('masukkan nama pembeli\t: ')
JumlahTiket =int(input('masukkan jumlah tike\t :'))
NoHP =int(input('masukkan Nomor HP\t :'))
jurusan = input('masukkan kode jurusan <SBY/BL/LMP>\t :')

if jurusan == 'SBY':
    tujuan = 'Surabaya'
    harga = 300000
elif jurusan == 'BL':
    tujuan = 'Bali'
    harga = 350000
elif jurusan == 'LMP':
    tujuan = 'Lampung'
    harga = 500000
else:
    tujuan = 'jurusan tidak terdaftar'
print(tujuan, harga)

total = harga * JumlahTiket
if JumlahTiket >= 3:
    diskon = total / 10
else:
    diskon = 0

total_bayar = total - diskon
print(total)
print(diskon)
print(total_bayar)
