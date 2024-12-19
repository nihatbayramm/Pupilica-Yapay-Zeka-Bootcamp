import pandas as pd
import numpy as np

# Veri sozlugu
# "İsim", "Yas" ve "maas(TL)" adinda sutunlar iceren bir sozluk olusturuluyor
dictionary = {"İsim": ["ali", "veli", "ahmet"],
              "Yas": [10, 58, 30],
              "maas(TL)": [10.50, 200, 300]}

# DataFrame olusturma
# Yukarıdaki sozluktan bir pandas DataFrame'i olusturuluyor
veri = pd.DataFrame(dictionary)

# Ortalama yas hesaplanıyor
ortalama_yas = veri["Yas"].mean()

# Yas grubunu for dongusuyle ekleme
# Yas gruplarini (büyük veya küçük) for dongusu ile ekliyoruz
yasGrubu = []

for i in range(len(veri["Yas"])):
    if veri["Yas"][i] > ortalama_yas:
        yasGrubu.append("büyük")  # Yas ortalamadan büyükse "büyük" ekleniyor
    else:
        yasGrubu.append("kucuk")  # Yas ortalamadan küçükse "küçük" ekleniyor

# Yeni sutunu ekleme
veri["yasGrubu"] = yasGrubu

# List Comprehension ile yas grubunu ekleme
# Yukarıdaki işlemi list comprehension ile de yapıyoruz
veri["yasGrubu2"] = ["büyük" if veri["Yas"][i] > ortalama_yas else "kucuk" for i in range(len(veri["Yas"]))]

# Sonuclari gosterme
print(veri)

# "Yeni yaş" hesaplama, "Ali"nin yaşı 2 katına çıkarılıyor, diğerlerinin 5 katına
veri["newYas"] = [veri["Yas"][i] * 2 if veri["İsim"][i] == "ali" else veri["Yas"][i] * 5 for i in range(len(veri["İsim"]))]

# Sonuçları yazdırma
print(veri)


# Yas 10 yil sonrasi fonksiyonu
# Yas'a 10 yıl ekleyen fonksiyon
def yas10sonrasi (age):
    output = age + 10
    return output

# Yeni sutun "yas10yilsonra" ekleniyor
veri["yas10yilsonra"] = veri["Yas"].apply(yas10sonrasi)

# Sonuçları yazdırma
print(veri)


# Yas çarpım fonksiyonu
# "Ali"nin yaşı 2 ile çarpılır, diğerlerinin yaşı 5 ile çarpılır
def yasCarpim (df):
    if df.İsim == "ali":
        return df.Yas * 2
    else:
        return df.Yas * 5

# Yeni sütun "yasCarpim" ekleniyor
veri["yasCarpim"] = veri.apply(yasCarpim, axis=1)
print(veri)


# Isim uzunluğuna göre işlem yapan fonksiyon
# İsim uzunluğuna göre yaşa farklı bir çarpan uygulanıyor
def uzunluk(df):
    if len(df["İsim"]) == 5:
        return df["Yas"] * 2
    elif len(df["İsim"]) == 6:
        return df["Yas"] * 4
    elif len(df.İsim) == 3:
        return df["Yas"] * 6
    else:
        return df.Yas * 4

# Yeni sütun "uzunlukluYas" ekleniyor
veri["uzunlukluYas"] = veri.apply(uzunluk, axis=1)
print(veri)

# Veri birlestirme

# 1. sozlukle DataFrame olusturma
sozluk1 = {
    "isim": ["ali", "veli", "ayşe"],
    "yas": [20, 30, 40],
}

veri1 = pd.DataFrame(sozluk1)

# 2. sozlukle DataFrame olusturma
sozluk2 = {
    "isim": ["nihat", "hasan", "batu"],
    "yas": [50, 30, 80],
}

veri2 = pd.DataFrame(sozluk2)

# DataFrame'leri satir satir birlestirme
veribirlesim = pd.concat([veri1, veri2], axis=0)  # axis=0 satir satir birlestirir

# Sonucu yazdirma
print(veribirlesim)

# 3. sozlukle DataFrame olusturma
sozluk3 = {
    "sehir": ["x", "y", "z"],
    "yas": [50, 30, 80],
}

veri3 = pd.DataFrame(sozluk3)

# DataFrame'leri satir satir birlestirme
veribirlesim1 = pd.concat([veri1, veri3], axis=0)

# Sonucu yazdirma
print(veribirlesim1)
