# listeler ?
# listeler birer dizidir. Dizilerde elemanlar birer index ile tanımlanır. Listeler de elemanlar birer index ile tanımlanır.

liste =["süt","ekmek","yumurta"]
fiyat = [10,20,30]
print(liste[0])
print(fiyat[0])

# indeksleme : indeks 0'dan baslar !!!
# liste[0] = "süt"
# liste[1] = "ekmek"
# liste[2] = "yumurta"
# fiyat[0]= 10
# fiyat[1] = 20
# fiyat[2] = 30

haftaninGunleri = ["pazartesi","sali","çarşamba","perşembe","cuma"]
# haftaninGunleri[0] = "pazartesi"
# haftaninGunleri[1] = "salı"
# haftaninGunleri[2] = "çarşamba"

#sondan baslayarak indeksleme
print(haftaninGunleri[-1])
print(haftaninGunleri[-2])
print(haftaninGunleri[-3])
print(haftaninGunleri[-4])

#uzunluk bulma 'len' komutu kullanilir

print(len(haftaninGunleri)) # 5 

print(len(fiyat)) # 3


print(haftaninGunleri[0:3])  #pazartsinden carsambaya kadar yazdirir.

print(haftaninGunleri[0:6:2]) #2'ser atlayarak yazdirir.

#append komutu ile liste elemanina yeni eleman ekleriz

haftaninGunleri.append("cumartesi")

# remove komutu ile listeden eleman sileriz

haftaninGunleri.remove("sali")

# sort komutu ile listede elemanlar siralanir

fiyat.sort()

# tuple : 
# tuple de degiskenlere ulasim saglanir ama degiskenleri degistirelemez tuple de degiskenleri degistirmek icin tuple'i list'e cevirmek gerekir.

tupleList=(1,2,2,2,2,2,3,4,5)

# tupleList[0]=5 hata aliriz
#lis komutlarinin cogu gecerlidir burda
print(tupleList[0])

print(tupleList.count(2)) #kac tane 2 oldugunu gosterir

# veri tipleri 
#dictionary
#key value degerlerinden olusur
kelimeler = {
    "merhaba" : "hello",
    "selam" : "hi",
    "nasilsin" : "how are you"
    
    }

print(kelimeler)

sehirPlaka={
    "istanbul" : 34,
    "ankara" : 6,
    "izmir" : 35,
    "Sirnak" : 73 ,
}
print(sehirPlaka.keys())
print(sehirPlaka.values())


#veri tipleri donusumu
#string
#int
#float

metin ="16"
kesirliSayi=16.5
sayi=16
print(type(metin))
print(type(kesirliSayi))
print(type(sayi))
#string => int
metinİnt=int(metin)
print(type(metinİnt))
#float => int
kesirliSayiİnt=int(kesirliSayi)
print(kesirliSayiİnt)
#str => float
kesirliSayiString=str(kesirliSayi)
print(type(kesirliSayiString))

#int => float
sayiFloat=float(sayi)
print(type(sayiFloat))

#if - else 
#elif
sayi1=5
sayi2=10
if sayi1>sayi2:
    #eğer  koşul saglaniyorsa bu kod calissir

    print(f"{sayi1} {sayi2} den büyüktür")

elif sayi1==sayi2: #eğer  koşul saglaniyorsa bu kod calissir
      print(f"{sayi1} = {sayi2}")
else:
        print(f"{sayi1} {sayi2} den küçüktür")
        #eğer  koşul saglanmiyorsa bu kod çalışır


list=[1,2,3,4,5]
deger=5

if deger in list:
    print(f"{deger} listede var")
else:
        print(f"{deger} listede yok")


countary={
    "Turkey": "Ankara",
    "USA": "Washington",
    "Canada": "Ottawa"

}

if "Turkey" in countary:
    print(f"Turkiye'nin başkenti {countary['Turkey']}")
else:
        print("Türkiye listede yok")
         
lisst=["pazartesi","sali","carsamba","persembe","cuma","cumartesi","pazar"]

if lisst[2]=="pazartesi":
    print("2.indekste")

else :
    print(f"2.indeksinde degil indeks {lisst.index("pazartesi")} ")

#Donguler
#for loop

for i in range(1,11): #1 den 10 a kadar dondurur
    print(i)

sayiii=[1,5,4,1,2]
for i in sayiii:
    print(i**2) #her bir elemanin karesini alir



for i in "pazartesi" : 
    print(i) #her bir karakteri alir

top=[1,2,3,4,5,6]
sonuc = 0
for i in top:
     sonuc +=i 
print(sonuc)

metin = "bugun python dersi var"
metinList=metin.split(" ") #metni bosluklara gore ayirir liste yapar

kucuk=[]
for i in metinList:
    kucukKelime=i.lower()
    kucuk.append(kucukKelime)
print(kucuk)

buyuk=[]
for i in metinList:
    buyuKelime=i.upper()
    buyuk.append(buyuKelime)
print(buyuk)


listee = [1, 2, 3, 4, 5, 6]
def fonksiyon(liste):
    cifttoplam = 0
    tekToplam = 0
    for i in liste:
        if i % 2 == 0:
            cifttoplam += i
        else:
            tekToplam += i
    return f"cift sayilarin toplami: {cifttoplam} \ntek sayilarin toplami: {tekToplam}"

toplamm = fonksiyon(listee)
print(toplamm)



#While dongusu
sayi = 0
while sayi < 10:
    print(sayi)
    sayi += 1

print("while dongusu bitti")

#while ile toplama
liste =[1,2,3,4,5,6]
toplam = 0
sayac = 0
while sayac < len(liste):
    toplam += liste[sayac]
    sayac += 1
print(toplam)



#while ile cift sayilarin toplami
liste = [1,2,3,4,5,6]
toplam = 0
sayac = 0
while sayac < len(liste):
    if liste[sayac] % 2 == 0:
        toplam += liste[sayac]
        sayac += 1
    else:
       sayac += 1
      

print(toplam)





