import numpy as np  # Numpy kutuphanesi import ediliyor.

# 1. Listeyi numpy diziye donusturme
liste = [1, 2, 3, 5]  # Python listesi
dizi = np.array(liste)  # Listeyi numpy dizisine donusturuyoruz
print("Numpy Dizi:", dizi)

# 2. Dizinin boyutunu sorgulama
boyut = dizi.shape  # Dizinin boyutunu aliyoruz
print("Dizi Boyutu:", boyut)

# 3. Diziyi yeniden sekillendirme
dizi = np.array([1, 2, 3, 5])  # Yeni numpy dizisi
dizi1 = dizi.reshape(2, 2)  # 2x2 sekline donusturme
print("Yeniden Sekillendirilmis Dizi:\n", dizi1)

# 4. Dizinin eleman sayisini bulma
print("Eleman Sayisi:", dizi1.size)

# 5. Dizinin tipini sorgulama
print("Dizinin Tipi:", type(dizi1))

# 6. 2 Boyutlu dizi olusturma
dizi2D = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
print("2 Boyutlu Dizi:\n", dizi2D)

# 7. Sifirlardan olusan dizi
sifirDizi = np.zeros((3, 4))  # 3x4 boyutunda sifir dizisi
print("Sifir Dizisi:\n", sifirDizi)

# 8. Birlerden olusan dizi
birlerDizi = np.ones((3, 4))  # 3x4 boyutunda bir dizisi
print("Bir Dizisi:\n", birlerDizi)

# 9. Araliklarla dizi olusturma
aralikDizi = np.arange(10, 50, 5)  # 10'dan 50'ye kadar, 5'er artarak
print("Aralik Dizisi:", aralikDizi)

# 10. Esit aralikli dizi olusturma
linspaceDizi = np.linspace(1, 10, 5)  # 1 ile 10 arasinda 5 esit deger
print("Linspace Dizisi:", linspaceDizi)

# 11. Baska bir linspace ornegi
sayi = np.linspace(0, 10, 4)
print("Linspace 4 Deger:", sayi)

# ---------------------------
# Numpy Temel Islemler
# ---------------------------

# Matematiksel islemler
a = np.array([1, 2, 3])  # Birinci dizi
b = np.array([4, 5, 6])  # Ikinci dizi

print("Toplama:", a + b)
print("Carpma:", a * b)
print("Cikarma:", a - b)
print("Bolme:", a / b)

# Kare alma
print("A Dizisinin Karesi:", a ** 2)
print("B Dizisinin Karesi:", b ** 2)

# Filtreleme
print("A Dizisinin 2. Elemani:", a[1])
print("B Dizisinin 2. Elemani:", b[1])
print("A Dizisinde 2'den Kucuk Olanlar:", a < 2)

# Matris carpimi
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 matris
b = np.array([[4, 5, 6], [7, 8, 9]])  # 2x3 matris
print("Matris A:\n", a)
print("Matris A ile B Transpozunun Carpimi:\n", a.dot(b.T))

# Maximum, minimum ve toplam
print("A Dizisinin En Buyuk Degeri:", np.max(a))
print("A Dizisinin En Kucuk Degeri:", np.min(a))
print("A Dizisinin Toplami:", np.sum(a))

# Satir bazinda toplama
print("Satir Bazinda Toplam:", a.sum(axis=1))

# ---------------------------
# Rastgele Sayi Uretme
# ---------------------------

# 0-1 arasinda rastgele sayilar
rasgeleDizi = np.random.random((3, 3))  # 3x3 rastgele deger
print("0-1 Rastgele Dizi:\n", rasgeleDizi)

# Normal dagilimli rastgele degerler
rasgeleDizi2 = np.random.normal(0, 1, 5)  # Ortalama=0, Std=1, 5 deger
print("Normal Dagilimli Rastgele Dizi:", rasgeleDizi2)

rasgeleDizi3 = np.random.normal(0, 1, (5, 3))  # 5x3 boyutlu dizi
print("Normal Dagilimli 2D Dizi:\n", rasgeleDizi3)

# ---------------------------
# Indeksleme ve Slicing
# ---------------------------

dizi = np.array([1, 2, 3, 4, 5])
print("Ilk Eleman:", dizi[0])
print("1'den 3'e Kadar:", dizi[1:3])
print("Ilk 3 Eleman:", dizi[:3])

# 2D Dizi Indeksleme
dizi2D = np.array([[1, 2, 3, 4, 5], [6, 7, 89, 9, 8]])
print("Eleman [0,0]:", dizi2D[0, 0])
print("Eleman [0,3]:", dizi2D[0, 3])
print("Satir 1:", dizi2D[1, :])
print("Sutun 2:", dizi2D[:, 2])

# ---------------------------
# Sekil Manipulasyonu
# ---------------------------

diziikiD = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Orjinal Sekil:", diziikiD.shape)

# Yeniden sekillendirme
a = diziikiD.reshape(diziikiD.shape[0] * diziikiD.shape[1], 1)
print("Yeniden Sekillendirilmis Dizi:\n", a)

# Transpoz alma
tranzpoz = diziikiD.T
print("Transpoz:\n", tranzpoz)

# Tek boyutlu hale getirme (ravel)
ravelDeger = diziikiD.ravel()
print("Tek Boyutlu Dizi:", ravelDeger)
