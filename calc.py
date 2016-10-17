# -*- coding: utf-8 -*-

st1, operator, st2 = input("Vpišite število1 računsko operacijo ter število 2 z presledki: ").split(" ")
st1 = int(st1)
st2 = int(st2)

if((st1 and operator and st2) != None):
    if(operator == "+"):
        print("Rezultat: {} + {} = {}".format(st1, st2, st1+st2))
    elif(operator == "-"):
        print("Rezultat: {} - {} = {}".format(st1, st2, st1-st2))
    elif(operator == "*"):
        print("Rezultat: {} * {} = {}".format(st1, st2, st1*st2))
    elif(operator == "/"):
        print("Rezultat: {} / {} = {}".format(st1, st2, st1/st2))
    else:
        print("Te operacije ne morate uporabiti!")
else:
    print("Niste vpisali vseh polj!")
