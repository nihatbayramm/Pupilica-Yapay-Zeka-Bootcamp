# Gerekli kütüphaneler yükleniyor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Veri seti okunuyor
veri = pd.read_csv("Iris.csv")

# Verinin son 5 satırı gösteriliyor
veri.tail()

# Verinin ilk 5 satırı gösteriliyor
veri.head()

# Verinin genel bilgileri ve tipleri gösteriliyor
veri.info()

# Verinin istatistiksel özellikleri (ortalama, standart sapma vb.)
veri.describe()

# Histogram oluşturuluyor
plt.figure()
# Sepal uzunluğu için histogram
plt.hist(veri['SepalLengthCm'], bins=10, alpha=0.5, color="red", label="SepalLengthCm")
# Petal genişliği için histogram
plt.hist(veri['PetalWidthCm'], bins=10, alpha=0.5, color="blue", label="PetalWidthCm")
# Y ekseni etiketi
plt.ylabel("Frekans (adet sayısı)")
# X ekseni etiketi
plt.xlabel("Uzunluk (cm)")
# Başlık
plt.title("Sepal Uzunluğu ve Petal Genişliği Histogramı")
# Legend (açıklama)
plt.legend()
# Grafiği göster
plt.show()

# Matplotlib nesnesini yazdır
print(plt)

# Alt grafikler (subplots) oluşturuluyor
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# İlk grafik: Petal genişliği
ax[0].plot(veri["PetalWidthCm"])  # Petal genişliği çiziliyor
ax[0].set_title("Petal Width")    # Başlık
ax[0].set_xlabel("Index")         # X ekseni etiketi
ax[0].set_ylabel("Cm")            # Y ekseni etiketi

# İkinci grafik: Sepal uzunluğu
ax[1].plot(veri["SepalLengthCm"])  # Sepal uzunluğu çiziliyor
ax[1].set_title("Sepal Length")    # Başlık
ax[1].set_xlabel("Index")          # X ekseni etiketi
ax[1].set_ylabel("Cm")             # Y ekseni etiketi

# Grafik düzenlemelerini sıkıştır
plt.tight_layout()

# Grafik gösteriliyor
plt.show()
