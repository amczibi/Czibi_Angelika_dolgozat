import random

def parosszam():
    szam = int(input("Adj meg egy páros számot: "))
    paros = True
    while paros:
        if szam % 2 != 0:
            szam = int(input("A megadott szám nem páros, adj meg egy páros számot: "))
        else:
            paros = False
            print(f"A megadott szám {szam} páros")


def beker_harom():
    szam = 0
    i = 0
    index = 1
    #szam = int(input(f"Add meg az {index}. páros számot: "))
    while i < 3:
        if szam % 2 == 0:
            szam = int(input(f"Add meg az {index}. páros számot: "))
        else:
            print(f"Nem páros szám, add meg az {index}. páros számot")
        index += 1
        i += 1


szamok = []
def legkisebb():
    min = 0
    i = 0
    while (i < len(szamok)):
        if (szamok[i] > szamok[min]):
            min = i
            i += 1
    print(min)
    print(szamok[min])


randszam = []
def veletlen():
    velszam = 0
    i = 0
    while i <= 13:
        velszam = int((random.random()*190 - 40))
        randszam.append(velszam)
        print(velszam)
        i += 1

    ketjegyuek_szama()
    paros_osszege()
    paratlan_osszege()
    melyik_nagyobb()


def ketjegyuek_szama():
    i = 0
    db = 0
    while i < len(randszam):
        if randszam[i] // 10 > 0 and randszam[i] // 10 < 10 or randszam[i] // 10 <= -1 and randszam[i] // 10 >= -9:
            db += 1
        i += 1
    print(f"A listában {db} db kétjegyű szám van.")


def paros_osszege(osszeg_p):
    i = 0
    osszeg_p = 0
    while i < len(randszam):
        if randszam[i] % 2 == 0:
            osszeg_p += randszam[i]
        i += 1
    print(f"A páros számok összege {osszeg_p}.")


def paratlan_osszege(osszeg_ptl):
    i = 0
    osszeg_ptl = 0
    while i < len(randszam):
        if randszam[i] % 2 != 0:
            osszeg_ptl += randszam[i]
        i += 1
    print(f"A páratlan számok összege {osszeg_ptl}.")


def melyik_nagyobb(osszeg_p, osszeg_ptl):
    paros_osszege()
    paratlan_osszege()
    if osszeg_p > osszeg_ptl:
        print(f"A párosok összege {osszeg_p} > a páratlanok összege {osszeg_ptl}")
    else:
        print(f"A páratlanok összege {osszeg_ptl} > a párosok összege {osszeg_p}")


def beolvasas(fajlnev):
    fajl = open("stadionok.txt", "r", encoding = 'utf-8')
    fajl_tartalom = fajl.read()
    print(fajl_tartalom)
    fejlec = fajl.readline().strip()
    sorok = fajl.readlines()

    tarolas(sorok)


stadion_nev = []
stadion_helyszin = []
stadion_csapat = []
palya_elso = []
palya_utolso = []

def tarolas(sorok):
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split(", ")
        stadion_nev.append(sor[0])
        stadion_helyszin.append(sor[1])
        stadion_csapat.append(sor[2])
        palya_elso.append(sor[3])
        palya_utolso.append(sor[4])
        i += 1