print("Merhaba, Dünya!")

#Değişken Tanımlama Kuralları
#Değişken isimleri harf veya _ ile başlamalıdır.
#DEğişken sayı ile başlamaz
#Türkçe karakter kullanılmaz yaş DEğil yas
#Büyük Küçük harfe duyarlıdır (Ad ile ad farklıdır)
#Boşluk içeremez boşluk yerlerinde _ kullanılır (soyadim, soy adim, soy_adim)

isim = "Ahmet"
yas = 25
boy = 1.80
ogrenci_mi = True

print(isim, "adlı kullanıcın yaşı:", yas)

ad = input("Adınızı girin: ")
print("Merhaba, ", ad, "!")

dogum_yili = int(input("Doğum yılınızı yazınız: "))
yas = 2025 - dogum_yili
print("Yaşınız: ", yas)

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
toplam = sayi1 + sayi2
print("Toplam: ", toplam)