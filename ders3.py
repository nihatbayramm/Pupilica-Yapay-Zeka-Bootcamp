# Gerekli kütüphanelerin import edilmesi
import pandas as pd
import numpy as np

# pandas kütüphanesi:
# Veri işleme, analiz, depolama, temizleme, dönüştürme, görselleştirme ve sorgulama işlemleri için kullanılır.

# ------------------ DataFrame Oluşturma ------------------ #
# Basit bir sözlük oluşturuluyor ve DataFrame'e dönüştürülüyor
dictionary = {"İsim": ["ali", "veli", "ahmet"],
              "Yas": [10, np.nan, 30],
              "maas(TL)": [10.50, 200, 300]}
veri = pd.DataFrame(dictionary)

print(veri)  # DataFrame'i ekrana yazdır
print(type(veri))  # Veri türünü yazdır (DataFrame)
print(veri.head())  # İlk 5 satırı göster
print(veri.tail())  # Son 5 satırı göster

print(veri.columns)  # Sütun isimlerini yazdır
print(veri.index)  # Satır indekslerini yazdır

# TEMEL BİLGİLERE ERİŞİM
print(veri.info())  # DataFrame hakkında temel bilgiler (veri türleri, null değerler vb.)
print(veri.describe())  # Sayısal sütunların istatistiksel özetini göster
print(veri.shape)  # Satır ve sütun sayısını yazdır

# ------------------ Indexleme ve Dilimleme ------------------ #
# Sözlük yeniden tanımlanıyor
dictionary = {"İsim": ["ali", "veli", "ahmet"],
              "Yas": [10, np.nan, 30],
              "maas(TL)": [10.50, 200, 300]}
veri = pd.DataFrame(dictionary)

# Satırları ve sütunları indeksleme
print(veri.loc[0])  # İlk satırı göster
print(veri.loc[0:1])  # İlk iki satırı göster
print(veri.loc[0:2, "İsim"])  # "İsim" sütunundan ilk üç satırı göster
print(veri.loc[0:2, "Yas"])  # "Yas" sütunundan ilk üç satırı göster
print(veri.loc[0:2, "Yas":"maas(TL)"])  # "Yas" ve "maas(TL)" sütunlarını göster

# ------------------ Sütun Ekleme ------------------ #
# Yeni sütun ekleniyor: şehir
veri["sehir"] = ["sırnak", "ankara", "istanbul"]
print(veri)

# Yeni sütun ekleniyor: maaşın %20 zamlı hali
veri["maasZamli20"] = veri["maas(TL)"] + (20 * veri["maas(TL)"] / 100)
print(veri)

# Dilimleme işlemleri
print(veri.loc[0:2, "Yas"])  # Yas sütununu göster
print(veri.loc[0:2, "Yas":"maasZamli20"])  # Yas ve maasZamli20 sütunlarını göster
print(veri.iloc[0:2, 0:2])  # İlk iki satır ve ilk iki sütunu indeksle
print(veri.iloc[0:1, 0:4])  # İlk satır ve ilk dört sütunu indeksle

# ------------------ Yeni DataFrame ve Filtreleme ------------------ #
sozluk1 = {"isim": ["ali", "veli", "murat", "ayse", "hilal"],
           "yas": [1, 2, 3, 4, 5],
           "maas": [66, 20, 15, 5, 50]}
veri2 = pd.DataFrame(sozluk1)
print(veri2)

# İndeksle sütun seçme
print(veri2.iloc[2:3, 0:3:2])  # Üçüncü satırdaki isim ve maaş sütunlarını göster
print(veri2.iloc[2, 3:])  # Hatalı satır, ancak sütun mevcut olmadığından uyarı verir

# Filtreleme işlemleri
veri2["sehir"] = ["ankara", "ankara", "sirnak", "sirnak", "batman"]
print(veri2)

filtre1 = veri2["yas"] > 2  # Yas sütunundaki değerler 2'den büyük olanları filtrele
filtrelenmis = veri2[filtre1]
print(filtrelenmis)

filtre2 = veri2["maas"] > 20  # Maaşı 20'den büyük olanları filtrele
filtrelenmis2 = veri2[filtre2]
print(filtrelenmis2)

# İki filtreyi aynı anda kullanma
ikilifiltre = veri2[filtre1 & filtre2]
print(ikilifiltre)

# ------------------ Yeni Örnek DataFrame ------------------ #
data = {"yas": [1, 2, 3, 4, 5],
        "maas": [66, 20, 15, 5, 50]}
verii = pd.DataFrame(data)

# Yeni sütunlar ekleniyor
verii["ulke"] = ["turkiye", "kanada", "etiyopya", "norvec", "brezilya"]
verii["sehir"] = ["ankara", "istanbul", "sirnak", "ankara", "sirnak"]

# Yeni bir sütun hesaplama: yaş/maaş oranı
verii["yas/maas"] = verii["maas"] / verii["yas"]
print(verii)

# Ortalama yaş hesaplama (Ankara şehir filtresi)
ort = verii[verii["sehir"] == "ankara"]["yas"].mean()
print("Ankara'daki ortalama yaş:", ort)

# Maksimum maaş hesaplama (Ankara şehir filtresi)
max = verii[verii["sehir"] == "ankara"]["maas"].max()
print("Ankara'daki maksimum maaş:", max)

# Şırnak şehrindeki ortalama yaş
sirnakOrt = verii[verii["sehir"] == "sirnak"]["yas"].mean()
print("Şırnak'taki ortalama yaş:", sirnakOrt)

# Şırnak şehrindeki maksimum maaş
sirnakmax = verii[verii["sehir"] == "sirnak"]["maas"].max()
print("Şırnak'taki maksimum maaş:", sirnakmax)
