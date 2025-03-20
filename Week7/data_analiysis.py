import pandas as pd

data = pd.DataFrame({
    "Yaş": [25,45,30,35,40],
    "Cinsiyet": ["Kadın","Erkek","Erkek","Kadın",None],
    "Maaş": [3000,7000,None,5000,6000],
    "Deneyim":[2,20,5,10,15],
    "Departman": ["IT","Yönetim","Muhasebe","IT","Yönetim"],
    "Terfi": [0,1,0,1,1]
})

print("Veri Setinin İlk 5 Satırı:")
print(data.head())

print("\nVeri Seti Bilgisi:")
print(data.info())

print("\nİstatistiksel Özet:")
print(data.describe())

print("\nEksik Değerlerin Sayısını:")
print(data.isnull().sum())