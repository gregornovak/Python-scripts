# -*- coding: utf-8 -*-

#naredim random list števil
my_list = [33, 12, 5, 13, 8, 9, 65]
print("Original list:", my_list)
#pridobim dolžino v listu, ter odštejem -1, ker se začne pri 0
length = len(my_list) - 1
#na začetku nastavim da je sorted = false
sorted = False
#dokler ni sorted true ne pojdi iz while zanke
while not sorted:
    #nastavim sorted na true, če je že urejeno po velikosti
    sorted = True
    #zanka, ki se ponovi tolikokrat kot je določeno v length spremenljivki
    for i in range(length):
        #preverim če je številka na "levi" strani večja od tiste na desni
        if my_list[i] > my_list[i+1]:
            #če je leva večja, nastavim sorted na false, zato da gre še enkrat v for zanko
            sorted = False
            #število na "levi" strani shranim v začasno spremenljivko
            temp = my_list[i]
            #številko na "desni" strani shranim v spremenljivko, ki je prej bila na "levi" strani
            my_list[i] = my_list[i+1]
            #na koncu pa še shranim številko, ki je bila na "levi" strani na "desno" stran
            my_list[i+1] = temp
print("Sorted list:", my_list)
