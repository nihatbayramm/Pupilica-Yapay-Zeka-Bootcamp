import pandas as pd

# veriyi iceriye aktar
veri = pd.read_csv("olimpiyatlar.csv")
veri_head = veri.head(15)
"""
veride nan degerler var, cikart veya doldur
games columnı gereksiz, veriden drop
her sporcu madalya almamis: madalya nan = madalya alamamis
id gereksiz
bir kisi iki takima katilmis? 1900 yilinda orada iki ulke varmiydi
ülke kısaltması yada takim gereksiz.
1920 den oncesi acaba guvenilir veri mi?
"""

veri.info()

# sutun isimlerinin duzenlenmesi
column = veri.columns
veri.rename(columns = {
    "ID" : "id",
    "Name" : "isim",
    "Sex" : "cinsiyet",
    "Age" : "yas",
    "Height" : "boy",
    "Weight" : "kilo",
    "Team" : "takim",
    "NOC": "uok", # ulusal olimpiyat komite
    "Games" : "oyunlar",
    "Year" : "yil",
    "Season" :"sezon",
    "City" : "sehir",
    "Sport" : "spor",
    "Event" : "etkinlik",
    "Medal" : "madalya"
    }, inplace = True)

# gereksiz/yararsiz verinin cikarilmasi
veri = veri.drop(["oyunlar"], axis = 1) 
veri_head = veri.head(15)
veri_duplicated = veri[veri.duplicated()] # birbirini tekrarlayan veri

# %% kayip veri problemi

"""
boy ve kilo sutununda bulunan kayip verileri dolduralim (etkinlik ortalamasi) ?
ortalama veya  medyan? bu veri seti icin fark etmez.
madalya alamayan sporculari veri setinden cikartalim

"""
# ortalama veya  medyan?
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.hist(veri.boy, bins = 100)
plt.title("boy")

plt.figure()
plt.hist(veri.kilo, bins = 100)
plt.title("kilo")

describe = veri.describe()

# boy ve kilo sutununda bulunan kayip verileri dolduralim (etkinlik ortalamasi)

# unique etkinliklerin ve sayisinin bulunmasi
essiz_etkinlik = pd.unique(veri.etkinlik) 

veri_gecici = veri.copy() # gercek veriyi kaybetmemek icin kopyala

boy_kilo_list = ["boy", "kilo"] # kayip veri sorunu olan sutunlar

for e in essiz_etkinlik: # etkinlik ozelinde iterasyona basla
    
    # etkinlik filtresi olustur
    etkinlik_filtresi = veri_gecici.etkinlik == e

    # veriyi etkinlige gore filtrele
    veri_filtreli = veri_gecici[etkinlik_filtresi]
    
    # boy ve kilo icin etkinlik ozelinde ortalam bul
    for s in boy_kilo_list:
        
        ortalama = np.mean(veri_filtreli[s])
        
        if np.isnan(ortalama) == False:
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri[s])
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)

    veri_gecici[etkinlik_filtresi] = veri_filtreli

veri = veri_gecici.copy()
veri.info()

# yas da bulunan kayip veri sorununu cinsiyet ve spora gore dolduralim
essiz_cinsiyet = pd.unique(veri.cinsiyet) 
essiz_spor = pd.unique(veri.spor) 

veri_gecici = veri.copy() # gercek veriyi kaybetmemek icin kopyala

for c in essiz_cinsiyet: 
    for s in essiz_spor:
    
        # cinsiyet ve spor filtresi olustur
        cinsiyet_spor_filtresi = np.logical_and(veri_gecici.cinsiyet == c, veri_gecici.spor == s)
    
        # veriyi etkinlige gore filtrele
        veri_filtreli = veri_gecici[cinsiyet_spor_filtresi]
        
        ortalama = np.mean(veri_filtreli["yas"])
        
        if np.isnan(ortalama) == False:
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri["yas"])
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(tum_veri_ortalamasi)

        veri_gecici[cinsiyet_spor_filtresi] = veri_filtreli

veri = veri_gecici.copy()
veri.info()

# madalya alamayan sporcularin bulunmasi
madalya_degiskeni = veri.madalya
null_sayisi = pd.isnull(madalya_degiskeni).sum() # madalya alamayan sporcu sayisi

madalya_degiskeni_filtresi = pd.isnull(madalya_degiskeni)

veri = veri[~madalya_degiskeni_filtresi]

veri.to_csv("olimpiyatlar_temizlenmis.csv", index = False)

# %% tek degiskenli veri analizi
import matplotlib.pyplot as plt

def plotHistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins =85, color = "orange")
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas", "boy", "kilo", "yil"]
for degisken in sayisal_degisken:
    plotHistogram(degisken)


def plotBox(degisken):
    plt.figure()
    plt.boxplot(veri[degisken])
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas", "boy", "kilo"]
for degisken in sayisal_degisken:
    plotBox(degisken)

# %% kategorik degiskenler
veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")
def plotBar(degisken, n = 5): # en cok 5 adet veriyi gorsellestir

    veri_ = veri[degisken]
    veri_sayma = veri_.value_counts() # value counts
    veri_sayma = veri_sayma[:n]
    
    plt.figure()
    plt.bar(veri_sayma.index, veri_sayma, color = "orange")
    plt.xticks(veri_sayma.index, veri_sayma.index.values)
    plt.xticks(rotation = 45)
    plt.ylabel("Frekans")
    plt.title(f"Veri Frekansi: {degisken}")
    plt.show()
    print(f"{veri_sayma}")

# dataframe icierisnde istenilen tipteki degiskenleri bul
categorical_columns = veri.select_dtypes(include = ["object"]).columns

for degisken in categorical_columns:
    plotBar(degisken, 20)
    
# %% iki degiskenli veri analizi

# cinsiyete gore boy ve kilo karsilastirmasi

erkek = veri[veri.cinsiyet == "M"]
kadin = veri[veri.cinsiyet == "F"]

plt.figure()
plt.scatter(kadin.boy, kadin.kilo, alpha = 0.8, label = "Kadin")
plt.scatter(erkek.boy, erkek.kilo, alpha = 0.1, label = "Erkek")
plt.xlabel("boy")
plt.ylabel("kilo")
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.legend()

# correlation calculation
numeric_correlation = veri.loc[:, ["yas", "boy", "kilo"]].corr() 

# madalya ve yas arasindaki correlation
veri_gecici = veri.copy()
veri_gecici = pd.get_dummies(veri_gecici, columns = ["madalya"])
numeric_correlation_yas_madalya = veri_gecici.loc[:, ["yas", 'madalya_Bronze', 'madalya_Gold','madalya_Silver']].corr()

# takimlarin kazandiklari altin gumus ve vronz madalya sayilari 
# groupby
# frupladik, toplamini aldik, siraladik ve ilk 20 sini elde ettik
veri_gecici["takim"] = veri_gecici["takim"].replace({ # soviet union isimlerini rusya ile replace et degistir.
    "Soviet Union": "Russia" 
})
groupby_takim = veri_gecici[["takim", "madalya_Gold", "madalya_Silver", "madalya_Bronze"]].groupby(["takim"], as_index = False).sum()
groupby_takim_sorted = groupby_takim.sort_values(by = "madalya_Gold", ascending = False)
groupby_takim_sorted_10 = groupby_takim_sorted[:20]

turkey = groupby_takim.query("takim == 'Turkey'")  # Sadece Türkiye'yi filtrele

# sehirlere gore kazanilan madalyalarin ortalamalari
groupby_sehir = veri_gecici[["sehir","madalya_Bronze","madalya_Silver","madalya_Gold"]].groupby(["sehir"],as_index=False).sum().sort_values(by = "madalya_Gold", ascending = False)

# cinsiyete gore
groupby_cinsiyet = veri_gecici[["cinsiyet","madalya_Bronze","madalya_Silver","madalya_Gold"]].groupby(["cinsiyet"],as_index=False).sum().sort_values(by = "madalya_Gold", ascending = False)

# %% cok degiskenli veri analizi
# pivot table

# madalya alan sporcularin cinsiyetlerine gore boy, kilo ve yas ortalamalarina bakalim
# 3 adet madalya, 2(cinsiyet)*3(boy, kilo yas)*3(mean, max, min) = 18
veri_pivot = veri.pivot_table(index = "madalya",
                              columns = "cinsiyet",
                              values = ["boy", "kilo", "yas"],
                              aggfunc = {"boy": np.mean, 
                                         "kilo": [np.median, np.max],
                                         "yas": [np.min, np.max, np.std]})

# takimlara ve cinsiyete gore alinan madalya sayilarinin toplami, max ve min degerleri

#takımlara ve cinsiyete gore alınan madalya sayıların toplamı ve maks ve min değeleri
veri_pivot_takim = veri_gecici.pivot_table(index=["takim", "sehir"], 
                                        columns = ["cinsiyet", "sezon"],
                 values=["madalya_Gold","madalya_Silver","madalya_Bronze"], 
                aggfunc={"madalya_Gold":[np.sum],
                         "madalya_Silver":[np.sum],
                         "madalya_Bronze":[np.sum]})

veri_pivot_takim["total"] = (
    veri_pivot_takim["madalya_Gold"].sum(axis =1) +
    veri_pivot_takim["madalya_Silver"].sum(axis =1) + 
    veri_pivot_takim["madalya_Bronze"].sum(axis =1))
veri_pivot_takim = veri_pivot_takim.sort_values(by = "total", ascending = False)[:100]

veri_pivot_takim.to_excel("veri_pivot_takim.xlsx")