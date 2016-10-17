# -*- coding: utf-8 -*-
#importam os modul, za upravljanje map, datotek, poti..
import os

#začetek programa, uporabnik vpiše z številko kaj želi narediti
def decision():
    print("*" * 75 + "\nPozdravljeni v program kjer lahko pregledujete, ustvarjate, preimenujete in brišete mape.\nIzbirate z številko!\n\t0. Izpiši vse mape\n\t1. Ustvari mapo\n\t2. Preimenuj mapo \n\t3. Izbriši mapo\n\t4. Izhod iz programa")
    #če vpiše številko se ta vrne, drugače pa izpiše error
    try:
        value = int(input("> "))
        return value
    except ValueError:
        print("Vpisati morate številko od 1 do 4!\n")
    except:
        print("What did you do?!\n")

#izpiše vse mape, ki obstajajo, če jih ni izpiše, da ne obstaja nobena mapa
def list_folders():
    #izpiše vse mape in datoteke
    dirs = os.listdir()
    #pridobim pot do te mape
    path = os.getcwd()
    #spremenljivka za preverjanje če obstaja kakšna mapa ali ne
    st_map = 0
    #z for zanko grem čez vse mape in datoteke
    for d in dirs:
        #ker želim izpisati samo mape, postavim pogoj, ki preveri za mape
        if (os.path.isdir(d)):
            #če najde mapo prištejem k številu map
            st_map += 1
            #izpišem mapo
            print(os.path.join(path, d))
    #\n
    print()
    #če ni nobenih map izpišem sledeče
    if(st_map == 0):
        print("Ni nobenih map na tej poti.\n")

#funkcija za ustvarjanje map
def create_folder():
    #uporabnik vpiše ime mape, če že obstaja izpiše error
    try:
        fldr_name = input("Vpišite ime mape: ")
        os.mkdir(fldr_name)
        print("Mapa je bila uspešno ustvarjena.\n")
    except OSError:
        print("Mapa s tem imenom '{}' že obstaja.\n".format(fldr_name))

#funkcija za preimenovanje map
def rename_folder():
    #uporabnik najprej vpiše ime datoteke, ki jo želi preimenovati
    try:
        fldr_name = input("Vpišite ime mape, ki jo želite preimenovati: ")
        #če ta mapa ne obstaja izpiše error
        if not os.path.exists(fldr_name):
            raise Exception("Ta mapa ne obstaja!")
        #če obstaja, uporabnik nato vpiše novo ime za to mapo
        new_fldr_name = input("Vpišite novo ime za mapo '{}': ".format(fldr_name))
        os.rename(fldr_name, new_fldr_name)
        print("Mapa je bila uspešno preimenovana v '{}'.\n".format(new_fldr_name))
    except:
        print("Ta mapa ne obstaja.\n")

#funkcija za brisanje map
def delete_folder():
    #uporabnik vpiše ime mape, ki jo želi izbrisati
    try:
        fldr_name = input("Vpišite ime mape, ki jo želite izbrisati: ")
        #če obstaja ta mapa jo izbriše, drugače pa vrne error
        if os.path.exists(fldr_name):
            os.rmdir(fldr_name)
        print("Mapa je bila uspešno izbrisana\n")
    except FileNotFoundError:
        print("Mapa z imenom '{}' ne obstaja.\n".format(fldr_name))

#glavna funkcija
def main():
    #dokler uporabnik ne vpiše št. za izhod, program laufa naprej
    while True:
        #shranim vrednost, ki jo vrne funkcija decision
        response = decision()
        #glede na št. kličem določeno funkcijo
        if(response >= 0) and (response <= 4):
            if(response == 0):
                list_folders()
            elif(response == 1):
                create_folder()
            elif(response == 2):
                rename_folder()
            elif(response == 3):
                delete_folder()
            else:
                break

#klic glavne funkcije
main()
