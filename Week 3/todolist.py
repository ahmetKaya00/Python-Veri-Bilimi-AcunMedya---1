def gorev_ekle():
    gorev = input("Eklemek istediğiniz görevi yazın: ")
    with open("todo.txt","a",encoding="utf-8") as dosya:
        dosya.write(gorev + "\n")
    print("Görev başarılı bir şekilde eklendi")

gorev_ekle()

def gorevleri_goruntule():
    with open("todo.txt","r",encoding="utf-8") as dosya:
        print("Yapılacaklar listesi:\n" + dosya.read())

gorevleri_goruntule()