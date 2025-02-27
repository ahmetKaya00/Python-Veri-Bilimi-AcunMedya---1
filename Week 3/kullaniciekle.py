import json
def kullanici_ekle():
    ad = input("Adınızı girin: ")
    yas = input("Yaşınızı girin: ")
    kullanici = {"ad": ad, "yas":yas}
    with open("kullanicilar.json","a",encoding="utf-8") as dosya:
        json.dump(kullanici, dosya, ensure_ascii=False)
        dosya.write("\n")

kullanici_ekle()