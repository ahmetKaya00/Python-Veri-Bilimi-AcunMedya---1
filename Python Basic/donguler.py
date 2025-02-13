for i in range(5):
    print(i)

toplam = 0
for i in range(1,11):
    toplam += i
print("Toplam: ", toplam)

kelime = input("Bir Kelime Girin: ")
for i in range(5):
    print(kelime)

sayi = 1
while sayi <= 5:
    print(sayi)
    sayi += 1

dogru_sifre = "1234"
girilen_sifre = ""

while girilen_sifre != dogru_sifre:
    girilen_sifre = input("Şifre girin")

print("Giriş Başarılı!")