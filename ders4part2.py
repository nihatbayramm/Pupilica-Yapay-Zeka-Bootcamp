import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Veri yukleme
# Iris veri setini okuyoruz ve ilk 5, son 5 satirini ekrana yazdiriyoruz
veri = pd.read_csv("Iris.csv")
print(veri.head())  # Ilk 5 satiri goster
print(veri.tail())  # Son 5 satiri goster
print(veri.info())  # Veri bilgilerini yazdir
print(veri.columns)  # Sutun isimlerini yazdir
print(veri.describe())  # Istatistiksel ozet verileri

# Turleri unique olarak kontrol et
# "Species" sutunundaki benzersiz degerleri kontrol ediyoruz
print(veri["Species"].unique())

# Turlere gore veri ayirma
# Iris ciceginin 3 farkli turu icin veriyi ayri ayri filtreliyoruz
veri_Iris_setosa = veri[veri.Species == "Iris-setosa"]
veri_Iris_versicolor = veri[veri.Species == "Iris-versicolor"]
veri_Iris_virginica = veri[veri.Species == "Iris-virginica"]

# Line plot (Cizgi Grafigi)
# SepalLengthCm ile PetalWidthCm degerlerini ve ID-PetalWidthCm degerlerini ciziyoruz
plt.figure(figsize=(8, 4))  # Grafik boyutunu ayarliyoruz
plt.plot(veri["SepalLengthCm"], veri["PetalWidthCm"], color="blue", alpha=0.5, label="Sepal-Petal Line")
plt.plot(veri["Id"], veri["PetalWidthCm"], color="red", alpha=0.7, label="ID-Petal Line")

# Grafik basligi ve eksen etiketleri ekliyoruz
plt.title("IRIS CICEGI GORSELLESTIRME")  # Grafik basligi
plt.xlabel("X Ekseni")  # X ekseni etiketi
plt.ylabel("Y Ekseni")  # Y ekseni etiketi
plt.legend()  # Grafige aciklama (legend) ekleniyor
plt.show()  # Grafigi ekranda gosteriyoruz

# Scatter plot (Nokta Grafigi)
# SepalLengthCm ve PetalWidthCm degerlerine gore bir nokta grafigi olusturuyoruz
plt.figure(figsize=(8, 4))  # Grafik boyutunu ayarliyoruz
plt.scatter(veri["SepalLengthCm"], veri["PetalWidthCm"], color="blue", alpha=0.5, label="Scatter")
plt.scatter(veri["Id"], veri["PetalWidthCm"], color="black", alpha=0.7, label="ID-PetalWidth")

# Grafik basligi ve eksen etiketleri ekliyoruz
plt.title("IRIS CICEGI GORSELLESTIRME")  # Grafik basligi
plt.xlabel("Sepal Length (Cm)")  # X ekseni etiketi
plt.ylabel("Petal Width (Cm)")  # Y ekseni etiketi
plt.legend()  # Grafige aciklama (legend) ekleniyor
plt.show()  # Grafigi ekranda gosteriyoruz
