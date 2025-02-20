def merhaba():
    print("Merhaba, Ahmet!")

merhaba()

def selam_ver():
    print("Merhaba!")

selam_ver()

def selam_ver(isim="Misafir"):
    print(f"Selam, {isim}!")

selam_ver("Ali Koç")

def toplama(a,b):
    print(f"Sonuç: {a + b}")

toplama(3,5)

def kare_al(sayi):
    return sayi ** 2

sonuc = kare_al(4)
print(sonuc)

def toplam(*sayilar):
    return sum(sayilar)

print(toplam(1,2,3,4,5,6,7,8,9))

def bilgiler(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")

bilgiler(ad="Ahmet", yaş=37,şehir="Mersin")


kullanici_listesi = []

def kullanici_ekle(ad,soyad,yas,sehir):
    kullanici = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Şehir": sehir
    }

    kullanici_listesi.append(kullanici)
    print(f"Kullanici eklendi: {ad} {soyad}")

kullanici_ekle("Ahmet", "Kaya",15,"Ankara")
kullanici_ekle("Ayşe", "Kalaycı",35,"Çorum")

def kullanici_listele():
    for kullanici in kullanici_listesi:
        print(kullanici)

kullanici_listele()
