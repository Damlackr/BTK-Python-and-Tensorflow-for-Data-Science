#!/usr/bin/env python
# coding: utf-8

# ### Değişkenler(Variables)

# In[1]:


x = 5


# In[2]:


y = 4


# In[3]:


x * y


# In[4]:


x


# In[5]:


x  = 6


# In[6]:


x * y


# -kodlar sırası ile çalışır.
# -sayıları değişkenlere atıp kullanabiliriz.
# -3. satırı tekrar çalıştırırsak güncel değere göre işlem yapar ve -24- bulur. sırası ile çalışarak işlem yapar.

# ### INTEGER & FLOAT

# In[8]:


benimDegiskenim + benimDigerDegiskenim


# In[7]:


benimDegiskenim = 10
benimDigerDegiskenim = 20


# In[9]:


type(benimDegiskenim)


# In[11]:


sonuc = benimDigerDegiskenim / benimDegiskenim


# In[12]:


sonuc


# In[13]:


type(sonuc)


# In[14]:


a = 3
b = 2
a / b


# In[15]:


pi = 3.14
type(pi)


# In[17]:


a = 5
type(a)


# In[18]:


a / pi


# In[19]:


a = 5
b = 4


# In[20]:


sonuc = a + b


# In[21]:


type(sonuc)


# In[22]:


x = 5
y = 3
x * y * 10


# In[23]:


x * x* x* x


# In[24]:


x ** 4


# In[25]:


#remaindr-kalınıBulmak

10 % 2


# In[26]:


11 % 2


# In[27]:


kullanicininYasi = 10


# In[28]:


kullanicininYasi * 5 /3


# In[29]:


type(kullanicininYasi)


# In[31]:


kullanicininYasi = input("Yaşınızı Giriniz:")


# In[32]:


kullanicininYasi


# tırnak içinde olması diğerlerinden farklıdır bu metindir(string). Numara değildir.

# In[33]:


type(kullanicininYasi)


# In[34]:


kullanicininYasi * 4


# ### STRING

# In[35]:


"merhaba dünya"


# In[36]:


x = "merhaba dünya"


# In[37]:


x = 10


# In[38]:


x = 20.5


# In[39]:


x = "hello"


# In[40]:


type(x)


# In[41]:


y = 'yeni string'


# In[42]:


type(y)


# -Tek tırnak kullanımı bazen soruna sebep olabilir.
# Örnek: 'anıl'ınyeri'-yanlış
#        "alın'ın yeri"-doğru"

# In[44]:


a = 5


# In[45]:


y.split()


# Tab tuşuna basıp bir sürü fonskiyonları görebiliriz. 
# a. yazıp tab a basıyoruz. ( nokta koymamız gerek)

# In[46]:


benimString = "Damla Çakır"


# In[47]:


benimString * 4


# In[52]:


benimInput = input("Yaşınızı Giriniz:")


# In[53]:


type(benimInput)


# In[54]:


benimIntInput = int(benimInput)
type(benimIntInput)


# In[55]:


benimIntInput / 3 * 5


# In[56]:


k = "Çakır"


# In[57]:


len(k)


# In[58]:


print("merhaba \npython")


# In[59]:


isimString = "Damla Çakır"


# ### Index

# In[60]:


isimString[0]


# In[61]:


isimString[7]


# In[63]:


isimString[5]


# In[64]:


isimString[-2]


# In[65]:


isimString[0] + isimString[-1]


# In[66]:


yeniString="0123456789"


# In[67]:


yeniString[2:]


# In[68]:


harfString="abcdefgh"


# In[69]:


harfString[3:]


# In[70]:


harfString[:3]


# ### Slicing

# In[71]:


gelenVeri = "AhmetinYasi65"


# In[72]:


gelenVeri[:-2]


# In[73]:


gelenVeri[-2:]


# In[74]:


gelenVeri[2:4]


# In[75]:


#Step Size


# In[76]:


gelenVeri[::]


# In[77]:


gelenVeri[::2]


# -2'şer 2'şer atlamayı gösterir.

# In[79]:


gelenVeri[1:10:3]


# In[80]:


gelenVeri[::-1]


# -Tersten yazmamızı da sağlar.

# In[81]:


benimIsmim = "damla"


# In[82]:


benimIsmim.capitalize()


# In[83]:


benimIsmim


# In[86]:


benimYeniIsmim = benimIsmim.capitalize()


# In[87]:


benimYeniIsmim


# In[88]:


benimTamIsmim = "Damla Çakır"


# In[91]:


benimTamIsmim.split()


# In[92]:


type(benimTamIsmim.split())


# In[98]:


listeler = benimTamIsmim.split() 


# In[100]:


listeler


# In[94]:


listeler[0]


# In[101]:


benimTamIsmim.upper()


# In[102]:


benimIsmim + "dır"


# In[106]:


benimSoyismim = "çakır"


# In[107]:


benimIsmim + " " + benimSoyismim


# In[108]:


j = "5"
k = "10"
j + k


# In[109]:


j = 5
k = 10
j + k


# ### Listeler

# In[1]:


benimString = "Damla Çakır"


# In[2]:


benimString[0]


# immutability & mutable = değişmezlik listeler de yok.

# In[3]:


benimListem = [10, 20, 30, 40]


# In[4]:


type(benimListem)


# In[5]:


benimNumaram = 10
benimDigerNumaram = 20


# In[6]:


benimNumaraListem = [benimNumaram, benimDigerNumaram]


# In[7]:


benimListem[3]


# In[8]:


benimNumaraListem[0]


# In[10]:


benimListem


# In[11]:


benimListem[0] = 100


# In[12]:


benimListem


# In[13]:


benimListem.append(50)


# In[14]:


benimListem


# In[15]:


benimListem.pop()


# In[16]:


benimListem


# pop: son elemanı atar
# remove: girileni çıkarır
# count: sayma
# reverse =  ters çevirir
# 

# In[17]:


benimListem.remove(40)


# In[18]:


benimListem


# In[19]:


benimListem.count(20)


# In[20]:


benimListem.append(20)


# In[21]:


benimListem


# In[22]:


benimListem.count(20)


# In[23]:


benimStringListem = ["atıl", "ahmet", "zeynep"]


# In[24]:


benimDigerListem = ["mehmet", "mahmut", "atlas"]


# In[25]:


benimToplamListem = benimStringListem + benimDigerListem


# In[26]:


benimToplamListem


# In[27]:


benimToplamListem * 5


# In[31]:


benimToplamListem


# In[33]:


benimToplamListem.reverse()


# In[34]:


benimToplamListem


# In[35]:


karisikListe = [1,2,3.5,"damla",9]


# In[36]:


type(karisikListe)


# In[38]:


sonucum = karisikListe[3]
karisikListe[3]


# In[39]:


type(sonucum)


# In[40]:


nestedList = [1, 5, "damla", 4, [6,"z"]]


# In[41]:


zDegiskenimiz = nestedList[4][1]


# In[42]:


zDegiskenimiz


# In[45]:


karmasikListe = [[1,2,3,["a","b"],50], 40, 20,["z",5.5],[3,["a"]]]


# In[49]:


bDegiskenimiz = karmasikListe[0][3][1]
bDegiskenimiz


# In[50]:


nestedList


# In[51]:


nestedList[:2]


# In[52]:


type(nestedList[:2])


# ### Sözlük

# In[53]:


benimListem = [1, 2, 3]


# In[54]:


benimListem[0]


# key-value pairing ( anahtar kelime- değer eşleşmesi

# In[55]:


benimYemeklerim = ["Elma", "Karpuz", "Muz"]


# In[56]:


benimKalorilerim = [100, 200, 300]


# In[57]:


benimYemeklerim[1]


# In[58]:


benimKalorilerim[1]


# dictionary

# In[59]:


benimSozluk = {"anahtarkelime" : "deger"}


# In[60]:


type(benimSozluk)


# In[61]:


benimSozluk["anahtarkelime"]


# In[62]:


benimYemekKaloriSozlugum = {"elma" : 100, "karpuz" : 200,"muz" : 300}


# In[64]:


benimYemekKaloriSozlugum["muz"]


# In[65]:


benimYemekKaloriSozlugum["elma"] = 200
benimYemekKaloriSozlugum


# In[66]:


benimDegisikSozlugum = {1: "damla", 2: "çakır"}


# In[67]:


benimDegisikSozlugum[1]


# In[70]:


yeniDictionary = {"anahtar1" : 100, 
                  "anahtar2": [20,20,30,40,4.5,"damla"],
                  "anahtar3": {"anahtar9" : 4}}


# In[71]:


yeniDictionary.keys()


# In[72]:


yeniDictionary.values()


# In[73]:


yeniDictionary["anahtar2"][-1]


# In[74]:


yeniDictionary["anahtar3"]["anahtar9"]


# ### Set

# In[75]:


benimListem = [1, 2, 3, 1, 2, 3]


# In[76]:


benimListem[3]


# In[77]:


benimListem


# set bir elemanı bir defa içinde barındırır.

# In[78]:


benimListeSetim =  set(benimListem)


# In[79]:


type(benimListem)


# In[80]:


type(benimListeSetim)


# In[81]:


benimListeSetim


# In[82]:


benimSet = {"a", "b" ,"c"}


# In[83]:


type(benimSet)


# In[84]:


benimSet


# In[85]:


bosListe = []


# In[86]:


type(bosListe)


# In[87]:


bosListe.append(1)
bosListe


# In[88]:


bosSet = {}


# In[89]:


type(bosSet)


# In[97]:


bosSozluk= {}


# In[98]:


type(bosSozluk)


# In[101]:


bosSozluk["anahtarKelime"] = 10


# In[102]:


bosSozluk


# In[103]:


benimBosSetim = set ()


# In[104]:


benimBosSetim


# In[105]:


benimBosSetim.add(10)


# In[106]:


benimBosSetim.add(10)


# In[107]:


benimBosSetim.add(20)


# In[108]:


benimBosSetim


# In[111]:


benimBosListem = list()
benimBosListem


# In[112]:


benimBosListem.append(10)
benimBosListem


# In[113]:


benimBosSozlugum = dict()
benimBosSozlugum


# In[114]:


benimBosSozlugum["key"] = 3234


# In[115]:


benimBosSozlugum


# ### Tuple

# In[116]:


benimListem = [1,2,"a",4.5]


# In[117]:


benimListem[0]


# In[118]:


benimListem[0] = 100


# In[119]:


benimListem


# In[120]:


benimTuple = (1,2,"a",4.5)


# In[121]:


benimTuple


# In[122]:


benimTuple[0]


# In[123]:


#benimTuple[2] = "b"


# In[124]:


benimTuple.count("a")


# In[126]:


benimTuple.index(4.5)


# ### Boolean

# In[127]:


benimBoolen  = True


# In[128]:


benimBoolen


# In[129]:


type(benimBoolen)


# In[130]:


benimBoolean = False


# In[131]:


10 > 5


# In[132]:


10 < 5


# In[133]:


listem = [5000 , 10000, 3000, 1000, 2000, 4000]


# In[135]:


len(listem)


# In[136]:


sum


# In[137]:


sum(listem)


# In[138]:


ortalama = sum(listem) / len(listem)


# In[139]:


ortalama


# In[140]:


listem[3] > ortalama


# In[141]:


kullaniciMaas = input("maaş bilginizi giriniz:")


# In[142]:


kullaniciMaasInt = int(kullaniciMaas)


# In[144]:


kullaniciMaasInt > ortalama


# ### Kıyaslamalar

# In[145]:


x = 10
y = 8


# In[146]:


x > y


# In[147]:


x < y


# In[148]:


x >= y


# In[149]:


9 >= 9


# In[150]:


x <= y


# In[151]:


x = y


# In[152]:


x


# In[153]:


y


# In[154]:


x = 10


# In[155]:


x ==y


# In[156]:


x != y


# In[157]:


3 > 1 and 3 > 2


# In[158]:


1 > 3 and 3 > 2


# In[159]:


1 > 3 or 3 > 2


# In[160]:


not 5 == 5 


# In[161]:


not 5 == 4 


# ### Eğer Kontrolleri

# In[168]:


if 3 > 4:
    print("damla çakır")
    print("if koşulu sağlandı")
print("if koşulundan dışarı çıktık")


# In[170]:


x = 5
y = 4


# In[174]:


if x > y:
    print("x, y'den daha büyükmüş")
elif y > x:
    print("y, x'den daha büyükmüş")
else:
    print("y ve x birbirine eşitmiş")


# In[175]:


benimKahramanim = input("Super kahraman seçiniz:")


# In[176]:


if benimKahramanim == "Batman":
    print("Batman!i seçtiniz tebrikler")
elif benimKahramanim == "Superman":
    print("Keşke Batman'i seçseydiniz.")
elif benimKahramanim == "Ironman":
    print("Iron man kimdir?")
else:
    print("Bunu tanımıyoruz")


# In[177]:


a = 10
b = 20
c = 30


# In[178]:


if a > b and b > c:
    print("a, b'den büyük VE b de c'den büyük")
elif a < b and b < c:
    print("a, b'den küçük VE b de c'den küçük")
else:
    print("bu koşullar olmadı")
  


# In[179]:


m = 10
k = 4
l = 5


# In[180]:


if m > k or k > 1:
    print("bu çalıştırılacak mı?")
    


# In[181]:


karakterCanli = True


# In[182]:


if karakterCanli == True:
    print("oyun karakteriniz yaşıyor")
else:
    print("oyun karakteriniz yaşamıyor")


# In[183]:


if karakterCanli:
    print("yaşıyor")
else:
    print("yaşamıyor")


# In[185]:


if not karakterCanli:
    print("yaşamıyor")


# In[190]:


benimString = "Damla Çakır"
if benimString == "damla Çakır":
    print("eşitmiş")
else: 
    print("eşit değilmiş")


# In[191]:


if "Çakır" in benimString:
    print("varmış")
else:
    print("yokmuş")


# In[192]:


benimListem=[10,20,30,40,50]


# In[193]:


if 60 in benimListem:
    print("var")


# In[194]:


benimSozluk = {"muz" : 100, "elma" : 150, "karpuz" : 500}


# In[196]:


if "muz" in benimSozluk.keys():
    print("varmış")
    


# In[199]:


if 800 in benimSozluk.values():
    print("varmış")
else:
    print("yokmuş")


# ### For Döngüsü

# In[200]:


benimListem = [10, 20, 30 , 40, 50]


# In[201]:


if 10 in benimListem:
    print("evet var")


# In[202]:


benimListem[0] * 5 / 3


# In[203]:


benimListem[1] * 5 / 3


# In[206]:


print("döngü başladı")
for numara in benimListem:
    print(numara * 5 / 3)
print("döngü bitti")


# In[208]:


for num in benimListem:
    yeniNumara = num * 5 / 3
    print(yeniNumara)


# In[212]:


yeniListe = [1,2,3,4,5,6]


# In[214]:


for rakam in yeniListe:
    if rakam % 2 == 0:
        print(rakam)


# In[215]:


yeniString = "Damla Çakır"


# In[216]:


for harf in yeniString:
    print(harf)


# In[217]:


benimTuple = (1,2,3,4,5)


# In[218]:


for eleman in benimTuple:
    print(eleman - 10)


# In[228]:


koordinatListesi = [ (10.2, 15.2), (32.4, 16.2), (40.2,20.2)]


# In[220]:


type(koordinatListesi)


# In[221]:


type(koordinatListesi[0])


# In[229]:


for eleman in koordinatListesi:
    print(eleman)


# In[230]:


for eleman in koordinatListesi:
    print(eleman[1])


# In[231]:


for (x,y) in koordinatListesi:
    print(y)


# In[232]:


benimGaripListem = [ (1,2,3), (4,5,6), (7,8,9)]


# In[233]:


for (x, y, z) in benimGaripListem:
    print(z)


# In[234]:


benimSozluk = {"muz": 150, "portakal":250, "elma": 400}


# In[235]:


for (anahtar, deger) in benimSozluk.items():
    print(deger)


# ### Continue Break Pass

# In[1]:


benimListem = [5, 10, 15, 25, 30]


# In[2]:


for numara in benimListem:
    print( numara/5 )


# In[3]:


for numara in benimListem:
    if numara == 15:
        break
    print(numara)


# belli bir koşulda döngüyü bitirmek istiyorsak break kullanılır.

# In[4]:


for numara in benimListem:
    if numara == 15:
        continue
    print(numara)


# eşit olanı geçerek devam ediyor.

# In[5]:


for numara in benimListem:
    pass


# aklımızda anlık olarak pass yazarak dikkate almamak üzere kullanılır.

# ### While Döngüsü

# In[11]:


x = 0


# In[12]:


while x <10:
    print(x)
    x = x + 1


# In[13]:


benimListem = [1,2,3,4,5]


# In[14]:


benimListem.pop()


# In[15]:


benimListem


# In[17]:


benimListem.append(5)


# In[18]:


benimListem


# In[19]:


while 3 in benimListem:
    print("3 hala listenin içinde")
    benimListem.pop()
    


# In[20]:


numara = 0


# In[21]:


while numara < 5:
    if numara == 4:
        break
    print(numara)
    numara = numara + 1
    


# In[27]:


yeniDegisken = 0


# In[23]:


while yeniDegisken < 15:
    print("yeniDegiskenin güncel değeri:"+ str(yeniDegisken))
    yeniDegisken = yeniDegisken + 1


# In[28]:


while yeniDegisken < 15:
    print(f"yeniDegisken'in güncel değeri: {yeniDegisken}")
    yeniDegisken = yeniDegisken + 1


# f format anlamına geliyor.

# ### Veri Biliminde Önemli Methotlar

# In[29]:


benimListem= [0,1,2,3,4,5,6]


# In[31]:


for numara in benimListem:
    print(numara)


# ### range

# In[32]:


range(15)


# In[34]:


list(range(15))


# In[36]:


for numara in list(range(15)):
    print(numara * 5)


# In[37]:


list(range(5,21,4))


# ### enumerate

# In[39]:


index = 0


# In[40]:


for numara in list(range(5,15)):
    print(f"güncel numara: {numara} güncel index: {index}")
    index = index + 1


# In[41]:


for eleman in enumerate(list(range(5,15))):
    print(eleman)


# In[42]:


for (index,numara) in enumerate(list(range(5,15))):
    print(numara)


# ### random

# In[44]:


from random import randint


# In[45]:


randint(0,100)


# In[46]:


randint(0,100)


# In[50]:


yeniListe = list(range(0,10))
yeniListe


# In[51]:


yeniListe[randint(0,9)]


# In[52]:


from random import shuffle


# In[53]:


shuffle(yeniListe)
yeniListe


# ### Zip

# In[54]:


yemekListesi = ["muz", "ananas", "elma"]
kaloriListesi = [100,200,300]
gunListesi = ["pazartesi", "salı", "çarşamba"]


# In[55]:


type(zip(yemekListesi,kaloriListesi,gunListesi))


# In[56]:


ziplenmisListe = list(zip(yemekListesi,kaloriListesi,gunListesi))


# In[57]:


for eleman in ziplenmisListe:
    print(type(eleman))


# In[58]:


ziplenmisListe


# ### listeler ileri seviye

# In[60]:


listeOrnegi = []
benimString = "damla çakır"

for harf in benimString:
    listeOrnegi.append(harf)
listeOrnegi


# In[61]:


yeniString = "damla ÇAKIR"


# In[62]:


yeniListeOrnegi = [eleman for eleman in yeniString]
yeniListeOrnegi


# In[64]:


ikinciListeOrnegi = [numara ** 5 for numara in list(range(0,10))]
ikinciListeOrnegi


# ### Fonksiyonlar

# In[65]:


benimAdim = "damla çakır"


# In[66]:


benimAdim.upper()


# In[67]:


benimAdim


# In[68]:


benimAdimBüyükHarfli = benimAdim.upper()
benimAdimBüyükHarfli


# In[69]:


benimAdim


# In[70]:


help(benimAdim.upper)


# In[71]:


def ilkFonskiyon():
    print("ilk fonksiyonum")
    


# In[73]:


ilkFonskiyon()


# - kodları düzenli yapar
# - istediğimiz kadar faklı yerde çağırabiliriz.(verimli olmasını sağlıyor.)
# - girdi alıp çıktı verebiliyorlar

# ### input & return

# In[75]:


def merhabaDunya(yazdirilacakIsim):
    print("merhaba")
    print(yazdirilacakIsim)


# In[77]:


merhabaDunya("python")


# In[80]:


def merhaba( isim = "damla"):
    print("merhaba")
    print(isim)


# In[81]:


merhaba()


# In[82]:


merhaba("ayşe")


# In[83]:


def toplama(numara1,numara2):
    sonuc = numara1+numara2
    print(sonuc)


# In[84]:


toplama(10,20)


# In[85]:


toplama(-200,350)


# In[86]:


def superToplama(num1,num2,num3):
    print(num1+num2+num3)


# In[87]:


superToplama(20,30,50)


# In[88]:


yeniDegisken = toplama(10,20)


# In[90]:


print(yeniDegisken)


# In[91]:


type(yeniDegisken)


# In[92]:


def dondurmeliToplama(num1,num2,):
    return num1+num2


# In[93]:


yeniSonuc = dondurmeliToplama(10,20)


# In[94]:


type(yeniSonuc)


# In[101]:


def kontrolFonk(s):
    if s == "damla":
        print("verdiğiniz string damla")
    else:
        print("verdiğiniz string başka bir şey")


# In[102]:


kontrolFonk("damla")


# In[103]:


kontrolFonk("ayşe")


# ### sayısız argüman - args & kwargs

# In[104]:


def yeniToplama(*args):
    return sum(args)
yeniToplama(10,20,30,50,60)


# In[107]:


def benimFonksiyonum(*args):
    return(args)


# In[108]:


type(benimFonksiyonum(20,30,40))


# In[113]:


def ornekFonksiyon(**kwargs):
    return(kwargs)


# In[114]:


type(ornekFonksiyon(muz = 100, elma = 200, ananas = 300))


# In[115]:


def keyWordKontrolu(**kwargs):
    if "damla" in kwargs:
        print("damla var")
    else:
        print("damla yok")


# In[117]:


keyWordKontrolu(damla = 70, zeynep = 50, mehmet = 40)


# ### Önemli Fonksiyonlar
# 

# In[118]:


def bolmeIslemi(numara):
    return numara / 2


# In[119]:


bolmeIslemi(20)


# In[120]:


benimListem = [1,2,3,4,5,6,7,8,9,10]


# In[121]:


yeniListe = []
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))


# In[122]:


yeniListe


# ### map

# In[123]:


list(map(bolmeIslemi, benimListem))


# In[124]:


def kontrolFonksiyonu(string):
    return "a" in string


# In[125]:


"a" in "Damla"


# In[127]:


kontrolFonksiyonu("zeynep")


# In[128]:


kontrolFonksiyonu("ayşe")


# In[129]:


stringListesi = ["damla", "atıl","zeynep","mehmet","levent"]


# In[132]:


sonucListesi = list(map(kontrolFonksiyonu,stringListesi))


# In[133]:


sonucListesi


# In[134]:


sonucListesi.count(False)


# ### Filter
# 

# In[135]:


list(filter(kontrolFonksiyonu, stringListesi))


# - True olanları gösteriyor.

# ### lambda

# In[136]:


carpma = lambda numara : numara * 3


# In[137]:


carpma(10)


# In[138]:


ornekListesi = [10,20,30]


# In[140]:


list(map(lambda numara : numara * 4,ornekListesi))


# ### scope(kapsam)

# In[141]:


numara = 20

def carpma(rakam):
    numara = 10
    return numara * rakam


# In[142]:


carpma(5)


# In[143]:


print(numara)


# In[144]:


x = 20
x = 10


# In[145]:


x


# ### Local, Enclosing, Global, Built-In

# In[147]:


benimAdim = "Damla" #Global

def benimFonksiyonum():
    benimAdim = "Mahmut"
    #Enclosing
    def icFonksiyon():
        benimAdim = "Ayşe"
        #local
        print(benimAdim)
    icFonksiyon()


# In[148]:


benimFonksiyonum()


# In[149]:


print(benimAdim)


# In[150]:


y = 10

def yeniFonksiyon(y):
    print(y)
    y = 5
    print(y)
    return y
    


# In[151]:


yeniFonksiyon(3)


# In[152]:


y


# In[153]:


y = yeniFonksiyon(3)


# In[154]:


y


# In[157]:


y = 10

def ornekFonksiyon():
    global y
    y = 5
    print(y)


# In[158]:


ornekFonksiyon()


# In[159]:


y


# In[ ]:




