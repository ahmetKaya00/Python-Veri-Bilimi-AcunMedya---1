print("Merhaba")

#print(10/0)

#print("Merhaba" + 5)
"""
liste = [1,2,3]
print(liste[5])
"""
try:
    x = int(input("Bir sayı giriniz: "))
    print(f"Girdiğiniz sayı: {x}")
except ValueError:
    print("Hata: Lütfen geçerli bir sayı girin!")

try:
    dosya = open("ornek.txt","r")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya Bulunamadı.")
finally:
    dosya.close()
    print("Dosya kapatıldı.")

def bolme(a,b):
    if b == 0:
        raise ZeroDivisionError("Bir sayıyı sıfıra bölemezsin!")
    return a / b

print(bolme(10,0))


print("Merhaba")