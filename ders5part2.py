import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV dosyasını oku
veri = pd.read_csv("olimpiyatlar.csv")

# İlk 10 satırı göster
print(veri.head(10))

# Veri seti hakkında bilgi
veri.info()

# Sütun isimlerini yazdır
print("Orijinal Sütunlar:", veri.columns)

# Sütun isimlerini Türkçe karşılıklarıyla değiştir
veri.rename(columns={
    "ID": "id",
    "Name": "isim",
    "Sex": "cinsiyet",
    "Age": "yaş",
    "Height": "boy",
    "Weight": "kilo",
    "Team": "takım",
    "NOC": "ülke_kodu",
    "Games": "oyunlar",
    "Year": "yıl",
    "Season": "mevsim",
    "City": "şehir",
    "Sport": "spor",
    "Event": "etkinlik",
    "Medal": "madalya"
}, inplace=True)

# Gereksiz sütunları çıkar
veri.drop(columns=["oyunlar"], axis=1, inplace=True)

# Tekrarlayan veriler
duplicat = veri[veri.duplicated()]
print("Tekrarlayan Veriler:")
print(duplicat)

# Kayıp veri analizi
plt.figure()
plt.hist(veri["boy"], bins=100, color="blue", alpha=0.7)
plt.title("Boy Histogramı")
plt.figure()
plt.hist(veri["kilo"], bins=100, color="green", alpha=0.7)
plt.title("Kilo Histogramı")

# Veri özet bilgisi
print(veri.describe())

# Etkinliklerin eşsiz değerleri
essizEtkinlik = pd.unique(veri["etkinlik"])
print("Eşsiz Etkinlikler:")
print(essizEtkinlik)

# Kayıp verileri doldurma
boyKiloList = ["boy", "kilo"]
for etkinlik in essizEtkinlik:
    for sutun in boyKiloList:
        if sutun in veri.columns:
            etkinlik_filtre = veri["etkinlik"] == etkinlik
            ortalama = veri.loc[etkinlik_filtre, sutun].mean()
            veri.loc[etkinlik_filtre, sutun] = veri.loc[etkinlik_filtre, sutun].fillna(ortalama)

# Yaş sütunundaki NaN değerlerini doldurma (cinsiyet ve spor bazında)
gruplar = veri.groupby(["cinsiyet", "spor"])
for (cinsiyet, spor), grup in gruplar:
    ortalama_yas = grup["yaş"].mean()
    veri.loc[(veri["cinsiyet"] == cinsiyet) & (veri["spor"] == spor), "yaş"] = \
        veri.loc[(veri["cinsiyet"] == cinsiyet) & (veri["spor"] == spor), "yaş"].fillna(ortalama_yas)

# Madalya almayan sporcuların çıkarılması
madalyaDegiskeniFiltre = pd.isnull(veri["madalya"])
veri2 = veri[~madalyaDegiskeniFiltre]

# Veri setini temizlenmiş dosya olarak kaydet
veri.to_csv("olimpiyatlar_temizlenmis.csv", index=False)

# Tek değişkenli veri analizi
def plothistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins=85, color="orange", alpha=0.7)
    plt.xlabel(degisken)
    plt.title(f"{degisken} Histogramı")
    plt.show()

sayisal_degisken = ["yaş", "boy", "kilo", "yıl"]
for degisken in sayisal_degisken:
    plothistogram(degisken)

# Box plot
def plotbox(degisken):
    plt.figure()
    plt.boxplot(veri[degisken].dropna(), vert=False)
    plt.xlabel(degisken)
    plt.title(f"{degisken} Boxplot")
    plt.show()

for degisken in sayisal_degisken:
    plotbox(degisken)
