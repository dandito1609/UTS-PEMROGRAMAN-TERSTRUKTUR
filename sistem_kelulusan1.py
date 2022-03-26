indonesia = input("Masukan Nilai Bahasa Indonesia    :")
ipa = input("Masukan Nilai Ipa   :")
mtk = input("Masukan Nilai Matematika   :")

print  ('nilai Bahasa Indonesia :  ',indonesia)
print  ('nilai Ipa :  ',ipa)
print  ('nilai Matematika :  ',mtk)

nilai = (float(indonesia)+float(ipa)+float(mtk))/3
print  ('Nilai Akhir :  ',nilai)

if nilai >= 80 and nilai < 100:
    print('Nilai Huruf : A')
    print('Keterangan : LULUS')

elif nilai >= 70 and nilai < 80:
    print('Nilai Huruf : B')
    print('Keterangan : LULUS')
    
elif nilai >= 50 and nilai < 70:
    print('Nilai Huruf : C')
    print('Keterangan : Tidak lulus')

elif nilai >= 40 and nilai < 50:
    print('Nilai Huruf : D')
    print('Keterangan : Tidak lulus')

elif nilai >= 0 and nilai < 40:
    print('Nilai Huruf : E')
    print('Keterangan : Tidak lulus')
    