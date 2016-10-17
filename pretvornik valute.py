#!/usr/bin/env python
# -*- coding: UTF-8 -*-
dolar = 0.89098766
evro = 1.12235
print("============================================")
print("Pozdravljeni v pretvornik valut iz evra v dolar ter obratno!")
pretvorba = input("Ali želite pretvoriti znesek?(Da/Ne)")
print("============================================")
pretvorba = pretvorba.upper()
if (pretvorba == "DA"):
    print("Želite pretvarjati iz Evra v Dolar ali obratno?\n\t1. Evro v Dolar\n\t2. Dolar v Evro")
    izbira = int(input("> "))
    if (izbira == 1):
        print("============================================")
        znesek = int(input("Vpišite znesek, ki ga želite pretvoriti: "))
        print("Poteka pretvorba iz Evra v Dolar.....")
        koncni_znesek = znesek * evro
        print("============================================")
        print(znesek , "eurov je " , koncni_znesek, "dolarjev.")
    else:
        print("============================================")
        znesek = int(input("Vpišite znesek, ki ga želite pretvoriti: "))
        print("Poteka pretvorba iz Evra v Dolar.....")
        koncni_znesek = znesek * dolar
        print("============================================")
        koncni_znesek = znesek * dolar
        print(znesek, "dolarjev je", koncni_znesek,"evrov.")
else:
    print("\nPotlej pa kdaj drugič!")
