#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hesapla(a,b,islem):
    
    if islem == "+":
        return (str(a)+ " + "+str(b) + " = " + str(a+b)) 
    if islem == "-":
        return (str(a)+ " - "+str(b) + " = " + str(a-b)) 
    if islem == "*":
        return (str(a)+ " * "+str(b) + " = " + str(a*b)) 
    if islem == "/":
        return (str(a)+ " / "+str(b) + " = " + str(a/b))
    
a = int(input("ilk rakamı giriniz:"))
b = int(input ("ikinci sayıyı giriniz:"))
islem = input("işleminizi seçiniz:+-*/")
hesapla(a,b,islem)
     


# - Basit bir şekilde programı ilk önce yazdık.
# 

# In[ ]:


def hesapla(a,b,islem):
    
    if islem == "+":
        return (str(a)+ " + "+str(b) + " = " + str(a+b)) 
    if islem == "-":
        return (str(a)+ " - "+str(b) + " = " + str(a-b)) 
    if islem == "*":
        return (str(a)+ " * "+str(b) + " = " + str(a*b)) 
    if islem == "/":
        return (str(a)+ " / "+str(b) + " = " + str(a/b))

while True:
    
 a = int(input("ilk rakamı giriniz:"))
 b = int(input ("ikinci sayıyı giriniz:"))
 islem = input("işleminizi seçiniz:+-*/")
 print(hesapla(a,b,islem))
     


# - Programın sürekli çalışması için while true satırını ekledik.

# In[ ]:


def hesapla(a,b,islem):
    
    if islem not in "+-*/":
        return "Lütfen şu işlemlerden birini seçiniz: +-*/"
        
        
    if islem == "+":
        return (str(a)+ " + "+str(b) + " = " + str(a+b)) 
    if islem == "-":
        return (str(a)+ " - "+str(b) + " = " + str(a-b)) 
    if islem == "*":
        return (str(a)+ " * "+str(b) + " = " + str(a*b)) 
    if islem == "/":
        return (str(a)+ " / "+str(b) + " = " + str(a/b))

while True:
    
    a = int(input("ilk rakamı giriniz:"))
    b = int(input ("ikinci sayıyı giriniz:"))
    islem = input("işleminizi seçiniz:+-*/")
    print(hesapla(a,b,islem))


# - işlemleri seçerken doğru bir şekilde sadece istenen işlemlerden birisinin olmasını istediğimiz için bunun uyarısını ekledik.

# In[ ]:


def hesapla(a,b,islem):
    
    if islem not in "+-*/":
        return "Lütfen şu işlemlerden birini seçiniz: +-*/"
        
        
    if islem == "+":
        return (str(a)+ " + "+str(b) + " = " + str(a+b)) 
    if islem == "-":
        return (str(a)+ " - "+str(b) + " = " + str(a-b)) 
    if islem == "*":
        return (str(a)+ " * "+str(b) + " = " + str(a*b)) 
    if islem == "/":
        return (str(a)+ " / "+str(b) + " = " + str(a/b))

while True:
    try:
    
        a = int(input("ilk rakamı giriniz:"))
        b = int(input ("ikinci sayıyı giriniz:"))
        islem = input("işleminizi seçiniz:+-*/")
        print(hesapla(a,b,islem))
    except:
        print("lütfen sayıları düzgün giriniz")


# - rakamların yerine rakam girebilmemiz için uyarı ekledik. string girince uyarıyor.
