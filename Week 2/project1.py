ogrenciler = []

def ogrenci_ekle():
    ad = input("Öğrencinin Adını Girin: ")
    soyad = input("Öğrencinin Soyadını Girin: ")
    yas = input("Öğrencinin Yaşını Girin: ")
    dersler = input("Öğrencinin aldığı dersleri aralarına virgül koyarak girin: ").split(",")

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Dersler": [ders.strip() for ders in dersler]
    }
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!")

def ogrenci_listele():
    if not ogrenciler:
        print("Henüz öğrenci eklenmedi!")
        return
    for i, ogreci in enumerate(ogrenciler, start=1):
        print(f"{i}. {ogreci['Ad']} {ogreci['Soyad']} - Yaş: {ogreci['Yaş']}")

def menu():
    while(True):
        print("\nÖğrenci Yönetim Sistemi")
        print("1. Yeni Öğrenci Ekle")
        print("2. Öğrenci Listesini Göster")
        print("6. Çıkış")

        secim = input("Lütfen yapmak istediğiniz işlemi (1-6) arasında seçin")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_listele()
        elif secim == "6":
            print("Sistemden çıkılıyor...")
            break
        else:
            ("Geçersiz bir giriş yaptınız")





menu()






