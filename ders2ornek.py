import numpy as np

# İlk matris
matris = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 5], [1, 2, 3, 4, 7]])
boy = matris.shape
print("Matrisin boyutu:", boy)

# Matrisin yeniden şekillendirilmesi
print("Yeniden Sekillendirilmis Matris:")
print(matris.reshape(3, 5))

# 1D dizi oluşturma ve yeniden şekillendirme
matris1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
matris1 = matris1.reshape(3, 5)
print("Matris1:\n", matris1)

# Matrislerin Toplamı
if matris.shape == matris1.shape:  # Boyut kontrolü
    toplam = matris + matris1
    print("Matrislerin Toplami:\n", toplam)
else:
    print("Matrislerin boyutlari toplama icin uyumlu degil!")

# linspace ve arange toplama
matrisLinspace = np.linspace(3, 5, 5)  # 3 ile 5 arasında 5 değer
arrange = np.arange(3, 8, 1)           # 3'ten 7'ye kadar (5 değer)

if matrisLinspace.shape == arrange.shape:  # Boyut kontrolü
    d = matrisLinspace + arrange
    print("Linspace ve Arange Toplami:\n", d)
else:
    print("Linspace ve Arange boyutlari uyumlu degil!")

# Matris elemanlarını döngü ile yazdırma ve çarpma işlemi
print("Matris Elemanlari ve Carpim Sonuclari:")
carpim_sonuclari = []
for i in range(matris.shape[0]):  # Satır sayısı kadar dönecek
    for j in range(matris.shape[1]):  # Sütunları döner
        sonuc = matris[i, j] * matris1[i, j]
        carpim_sonuclari.append(sonuc)
        print(f"matris[{i}][{j}] * matris1[{i}][{j}] = {sonuc}")

# Yeniden sekillendirme ve toplama
x = toplam.reshape(15, 1)
y = np.tile(d, 3).reshape(15, 1)  # d dizisini 3 kez tekrarlar
print("x Dizisi:\n", x)
print("y Dizisi:\n", y)

# İlk elemanların toplanması
sum_degeri = x[0] + y[0]
print("Ilk Elemanlarin Toplami:", sum_degeri)

# Kosul kontrolü ve liste ekleme
bos_liste = []
if sum_degeri > 1:
    bos_liste.append(sum_degeri)
    print("Bos Listeye Eklenen Degerler:", bos_liste)
else:
    print("Toplam 1'den kucuk")
