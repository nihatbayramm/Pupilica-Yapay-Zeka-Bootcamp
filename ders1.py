"""
değişken nedir ?

değişkenler, programlama dillerinde bir değişkenin değerini değiştirebilen bir değişkendir. 
Değişkenler, programlama dillerinin temel unsurlarından biridir. 
Değişkenler, programcının veri depolama ve işleme yapmasına olanak tanır.

"""

"""
integer ?

integer, tam sayıdır.
örnek: 1, 2, 3, 4, 5

"""

tamSayiDegeri=73 # 73 tam sayidir , bu deger integer tipindedir , degiskenin ismi tamSayiDegeri.
tamSayiDegeri = 81 # degiskenin degeri degistirildi , yeni deger 81
tamSayiDegeri2=73 # yeni bir degisken olusturuldu , ismi tamSayiDegeri2 , degeri 73 .

print(tamSayiDegeri2) # degiskenin degeri yazdirildi , 73
print(tamSayiDegeri) # degiskenin degeri yazdirildi , 81
print(type(tamSayiDegeri)) # type() fonksiyonu, degiskenin tipini gostermektedir.
# type() fonksiyonu, degiskenin tipini gostermektedir.

"""
kesirli sayılar ? 

double , float, decimal gibi isimler ile tanimlanabilir.
kesirli sayilar, ondalikli sayilardir.
örnek: 1.5, 2.5, 3.5, 4

"""

kesirliSayi = 3.5 # 3.5 kesirli sayidir , bu deger float tipidir
print(kesirliSayi) # degiskenin degeri yazdirildi , 3.5

"""
4 işlem özelliği

"""

#toplama

toplam = tamSayiDegeri + tamSayiDegeri2  
print(toplam)

#carpma 
carpma = tamSayiDegeri * tamSayiDegeri2  
print(carpma)

#cikarma

cikarma = tamSayiDegeri - tamSayiDegeri2  
print(cikarma)


#bolme 
bolme = tamSayiDegeri / tamSayiDegeri2  
print(bolme)


"""
stringler

"""

metin = "hello"
metin1 = "world"

birlesim =  metin + " "+ metin1

print(birlesim)

#format f string
ad = "ali"
soyad = "can"
yas = 25
kilo = 70
boy = 1.80
print(f"ad:{ad} soyad:{soyad} yas:{yas} kilo : {kilo} boy : {boy}")
#format string
print("boy : {0} kilo : {1}".format(boy , kilo)) 


"""
python syntax  yapisi : 

1. if
2. for
3. while
4. try
5. except
6. else
7. finally
8. with
9. class
10. def
11. lambda
12. list comprehension
13. dictionary comprehension
14. set comprehension
15. generator expression
16. async
17. await
18. yield
19. with
20. as
21. import
22. from
23. as
24. global
25. nonlocal
26. pass
27. break
28. continue
29. return
30. raise
31. assert
32. return
33. yield
34. lambda
35. def

https://www.blackbox.ai/share/5b665fa6-efe6-42b8-bacd-f4ec65ab9c6f

"""

#fonksiyonlar
# kullanici tanimli fonksiyonlar
# Kullanıcı tanımlı fonksiyonlar
def fonksiyon_adi():
    print("Fonksiyon çalıştı")
    # Burada kendini çağırmaktan kaçınıyoruz
    return "Fonksiyon çalıştı"

# Fonksiyonların çalıştığı yer
sonuc = fonksiyon_adi()
print(sonuc)

def dairenin_alani(yaricap):
    pi = 3.14
    alan = pi * (yaricap ** 2)
    return alan

# Kullanıcıdan yarıçapı al
yaricap = int(input("Yarıçapı gir: "))
alan = dairenin_alani(yaricap)
print("Dairenin alanı:", alan)


# dairenin cevre hesaplama

def daireCevreHesaplama(yaricap):
    pi = 3.14
    cevre = 2 * pi * yaricap
    return cevre

yaricap = int(input("Yarıçapı gir: "))
cevre = daireCevreHesaplama(yaricap)
print("Dairenin çevresi:", cevre)


