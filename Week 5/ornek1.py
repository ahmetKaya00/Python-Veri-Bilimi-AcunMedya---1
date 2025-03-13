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
