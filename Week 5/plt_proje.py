import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
notlar = np.random.randint(0,101,1000)

print("Ortalama Not: ", np.mean(notlar))
print("Yüksek Not: ", np.max(notlar))
print("Düşük Not: ", np.min(notlar))
print("Standart Sapma: ", np.std(notlar))

gecenler = notlar[notlar >=50]
kalanlar = notlar[notlar < 50]

print("Geçen Öğrenciler: ", len(gecenler))
print("Kalan Öğrenciler: ", len(kalanlar))

plt.figure(figsize=(10,5))
plt.hist(notlar,bins=10,edgecolor="black",alpha=0.7)
plt.xlabel("Not aralıkları")
plt.ylabel("Öğrenci Sayısı")
plt.title("Ogrenci Not Dagilimi")
plt.grid(True)
plt.show()

sirali_notlar = np.sort(notlar)

dusuk_dilim = sirali_notlar[:100]

yuksek_dilim = sirali_notlar[-100:]

print("En Düşük %10 Ortalaması",np.mean(dusuk_dilim))
print("En Yüksek %10 Ortalaması",np.mean(yuksek_dilim))

