nilai = int(input('masukkan nilai anda :'))

if nilai >= 80 and nilai <= 100:
    predikat = 'A'
elif nilai >= 75 and nilai <= 79:
    predikat = 'B'
elif nilai >= 60 and nilai <= 74:
    predikat = 'C'
elif nilai < 60:
    predikat = 'E'
print('nilai anda\t :',nilai)
print('predikat anda\t :',predikat)
