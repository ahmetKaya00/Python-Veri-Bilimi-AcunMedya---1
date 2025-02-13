#Aritmetiksel Operatörler

sayi1 = 10
sayi2 = 3

print("Toplam: ", sayi1 + sayi2)
print("Çıkarma: ", sayi1 - sayi2)
print("Çarpma: ", sayi1 * sayi2)
print("Bölme: ", sayi1 / sayi2)
print("Tam Bölme: ", sayi1 // sayi2)
print("Tam Bölme: ", sayi1 % sayi2)
print("Üst Alma: ", sayi1 ** sayi2)

#Karşılaştırma

print(sayi1 < sayi2)
print(sayi1 == sayi2)
print(sayi1 != sayi2)

#Matıksal Opertatörler

yas = 18
ehliyet = True

print(yas >= 18 and ehliyet)
print(yas < 18 or ehliyet)
print(not ehliyet)

#Koşullu ifadeler

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Sayı Pozitif")
elif sayi < 0:
    print("Sayı Negatif")
else:
    print("Sayı Sıfırdır")
