meyveler = ["Elma","Armut","Muz","Kiraz"]
print(meyveler)

print(meyveler[0])
print(meyveler[-4])

meyveler[1] = "Karpuz"
print(meyveler)

meyveler.append("Çilek")
print(meyveler)
meyveler.insert(1, "Portakal")
print(meyveler)
meyveler.remove("Muz")
print(meyveler)

for meyve in meyveler:
    print(meyve)

demet = ("Elma","Armut","Muz")
print(demet[1])

#demet[1] = "Karpuz"

ogrenci = {
    "ad": "Ali",
    "soyad": "Yılmaz",
    "yaş": 25
}
print(ogrenci["ad"])

ogrenci["şehir"] = "İstanbul"
ogrenci["yaş"] = 27

for anahtar, deger in ogrenci.items():
    print(f"{anahtar}: {deger}")

renkler = {"Kırmızı","Mavi","Yeşil","Sarı","Mavi"}
print(renkler)