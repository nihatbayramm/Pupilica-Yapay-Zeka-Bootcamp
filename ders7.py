import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

# Sütun isimlerini kontrol et
print(veri.columns)

# Scatter plot: Boy ve kilo arasındaki ilişkiyi görselleştirme
sns.set_style("darkgrid")
plt.figure()
sns.scatterplot(x="boy", y="kilo", data=veri)
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.show()

# Scatter plot: Boy ve kilo arasındaki ilişkiyi madalya türüne göre görselleştirme
plt.figure()
sns.scatterplot(x="boy", y="kilo", data=veri, hue="madalya")
plt.title("Boy ve Kilo Arasındaki İlişki Madalya Türüne Göre")
plt.show()

# Scatter plot: Doğrusal regresyon ile boy ve kilo arasındaki ilişki
plt.figure()
sns.regplot(x="boy", y="kilo", data=veri, marker="+", color="red")
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.show()

# lmplot: Sezona göre boy ve kilo karşılaştırması
sns.lmplot(x="boy", y="kilo", data=veri, hue="sezon", palette="muted")
plt.title("Boy ve Kilo Arasındaki İlişki Sezona Göre")
plt.show()

# Line plot: Sezon ve boy arasındaki ilişki (madalya türüne göre)
veri["sezon"] = veri["sezon"].astype("category")  # Sezon kategorik değilse dönüştür
plt.figure()
sns.lineplot(x="sezon", y="boy", data=veri, hue="madalya")
plt.title("Sezon ve Boy Arasındaki İlişki")
plt.show()

# Histogram: Boy dağılımı (cinsiyete göre KDE ile)
plt.figure()
sns.histplot(x="boy", data=veri, kde=True, hue="cinsiyet")
plt.title("Boy Dağılımı")
plt.show()

# Histogram: Kilo dağılımı (cinsiyete göre ayrı kolonlarda)
plt.figure()
sns.displot(x="kilo", data=veri, kde=True, col="cinsiyet")
plt.title("Kilo Dağılımı")
plt.show()

# İki boyutlu histogram: Boy ve kilo dağılımı (KDE ile, cinsiyete göre)
sns.displot(veri, x="boy", y="kilo", kind="kde", hue="cinsiyet")
plt.show()

# Bar plot: Cinsiyet ve boy arasındaki ilişki (madalya türüne göre)
plt.figure()
sns.barplot(x="cinsiyet", y="boy", data=veri, hue="madalya")
plt.title("Cinsiyet ve Boy Arasındaki İlişki")
plt.show()

# Catplot: Cinsiyet ve boy arasındaki ilişki (sezona göre ayrı kolonlarda)
sns.catplot(x="cinsiyet", y="boy", data=veri, kind="bar", hue="madalya", col="sezon")
plt.title("Cinsiyet ve Boy Arasındaki İlişki")
plt.show()

# Box plot: Cinsiyet ve boy arasındaki ilişki (madalya türüne göre)
plt.figure()
sns.boxplot(x="cinsiyet", y="boy", data=veri, hue="madalya")
plt.title("Cinsiyet ve Boy Arasındaki İlişki")
plt.show()

# Çok boyutlu kutu grafiği: Sezon, cinsiyet ve madalya türüne göre boy
sns.catplot(x="sezon", y="boy", hue="cinsiyet", col="madalya", data=veri, kind="box")
plt.show()

# Çok boyutlu kutu grafiği: Cinsiyet, yaş ve madalya türü (sezona göre ayrı kolonlarda)
sns.catplot(x="cinsiyet", y="yas", hue="madalya", col="sezon", data=veri, kind="box")
plt.show()

# Korelasyon matrisi ve heatmap
veriGecici = veri.loc[:, ["yas", "boy", "kilo"]]  # Sadece yaş, boy ve kilo sütunlarını seç
correlation = veriGecici.corr()  # Korelasyon hesaplama
plt.figure()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()

# Violin plot: Sezon ve boy dağılımı (cinsiyete göre)
plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri, hue="cinsiyet", split=True)
sns.catplot(x="sezon", y="boy", data=veri, hue="cinsiyet", kind="violin", split=True)
plt.title("Sezon ve Boy Dağılımı")
plt.show()

# Join plot: Boy ve kilo arasındaki ilişki (sezona göre KDE ve histogram)
g = sns.jointplot(x="kilo", y="boy", data=veri, hue="sezon", kind="kde")
g.plot_joint(sns.histplot)
g.plot_joint(sns.boxplot)
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.show()

# Pairplot: Tüm değişkenlerin karşılaştırılması
plt.figure()
sns.pairplot(veri)
g = sns.PairGrid(veri)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde=True)
plt.title("Değişkenler Arası İlişkiler")
plt.show()

# Count plot: Şehirlerin sayısal dağılımı
plt.figure()
sns.countplot(x="sehir", data=veri)
plt.xticks(rotation=90)  # Şehir isimlerini yatay hale getirme
plt.title("Şehirlerin Dağılımı")
plt.show()