def gunluk_yaz():
    not_metni = input("Günlüğünüze eklemek istediğiniz metni girin: ")
    with open("gunluk.txt","a",encoding="utf-8") as dosya:
        dosya.write(not_metni + "\n")
    print("Not başarılı bir şekilde eklendi!")


def gunluk_goruntule():
    with open("gunluk.txt","r",encoding="utf-8") as dosya:
        print("\nGünlük Notları:\n" + dosya.read())

gunluk_goruntule()