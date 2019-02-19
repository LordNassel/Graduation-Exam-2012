# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:03:01 2018

@author: LordNassel
"""
#%%
"""
Feladat:
    
A nagyvárosokon belül, ha csomagot gyorsan kell eljuttatni egyik helyről a másikra, akkor
sokszor a legjobb választás egy kerékpáros futárszolgálat igénybevétele. A futárszolgálat
a futárjainak a megtett utak alapján ad fizetést. Az egyik futár egy héten át feljegyezte fuvarjai
legfontosabb adatait, és azokat eltárolta egy állományban. Az állományban az adatok
rögzítése nem mindig követi az időrendi sorrendet. Azokra a napokra, amikor nem dolgozott,
nincsenek adatok bejegyezve az állományba.
A fájlban legalább 10 sor van, és minden sor egy-egy út adatait tartalmazza egymástól
szóközzel elválasztva. Az első adat a nap sorszáma, ami 1 és 7 közötti érték lehet. A második
szám a napon belüli fuvarszám, ami 1 és 40 közötti érték lehet. Ez minden nap 1-től kezdődik,
és az aznapi utolsó fuvarig egyesével növekszik. A harmadik szám az adott fuvar során
megtett utat jelenti kilométerben, egészre kerekítve. Ez az érték nem lehet 30-nál nagyobb. 

Például
    
    1 1 5
    1 2 9
    3 2 12
    1 4 3
    3 1 7
    ...
    
A 3. sor például azt mutatja, hogy a hét harmadik napján a második fuvar 12 kilométeres
távolságot jelentett.
Készítsen programot, amely a tavok.txt állomány adatait felhasználva az alábbi
kérdésekre válaszol! A program forráskódját mentse futar néven! (A program megírásakor
a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie,
feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)
A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja
a képernyőre a feladat sorszámát (például: 3. feladat:)! Ha a felhasználótól kér be adatot,
jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

"""
#%%

"""
1. Olvassa be a tavok.txt állományban talált adatokat, s annak felhasználásával oldja meg
a következő feladatokat! 
"""
import sys
 
with open("tavok.txt", "r") as filepointer:
    array = []
    for line in filepointer:
        info = line.replace('\n','').split(' ')
        array.append(info)
    filepointer.close()
print(array)
print(array[0][0])
print(array[0][1])
print(array[0][2])
#%%   
"""
2. Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben! Figyeljen arra,
hogy olyan állomány esetén is helyes értéket adjon, amiben például a hét első napján
a futár nem dolgozott! 
"""
legkisebbnap = 8 #szélsőértékdefiníció
for i in range(0,len(array)):
        hasonlito=int(array[i][0])
        if( hasonlito < legkisebbnap):
            legkisebbnap = hasonlito
print("2.feladat \n A het legelso utja %s km volt" % array[legkisebbnap][2]) # %s, mert sztringet iratunk ki
        

#%%
"""
3. Írja ki a képernyőre, hogy mekkora volt a hét utolsó útja kilométerben! 
"""
legnagyobbnap = 0
szam=1
for i in range(0,len(array)):
        hasonlito = int(array[i][0])
        if(hasonlito > legnagyobbnap):
            legnagyobbnap=hasonlito
            
for i in range(0,len(array)):
        if(hasonlito ==  int(array[i][0])):
            if(szam < int(array[i][1])):
                szam = int(array[i][1])

for i in range(0,len(array)):
    if((legnagyobbnap == int(array[i][0])) and (szam == int(array[i][1]))):
        utolsout=int(array[i][2])
        
print("3.feladat \n A het utolso utja: %d km volt" % utolsout)
        
#%%
"""
4. Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot. Írja ki a képernyőre,
hogy a hét hányadik napjain nem dolgozott a futár! 
"""
print("4.feladat")
munka = [0,0,0,0,0,0,0]
for i in range(0,len(array)):
    cucc = int(array[i][0])
    ujrair = cucc-1
    munka[ujrair]=1
for k in range(0,len(munka)):
    if(munka[k]==0):
        print("A %d. napon nem dolgozott a futar" % (k+1))
    
#%%
"""
5. Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar! Amennyiben több nap
is azonos, maximális számú fuvar volt, elegendő ezek egyikét kiírnia. 
"""
legtobbfuvarnap = 8
legtobbfuvar = 0
for i in range(0,len(array)):   
    szam= int(array[i][1])
    if(legtobbfuvar < szam):
        legtobbfuvar=szam
        legtobbfuvarnap=int(array[i][0])

print("5.feladat \n A het legtobb fuvaros napja: %d" % legtobbfuvarnap)
#%%
"""
6. Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon hány
kilométert kellett tekerni! 

    1. nap: 124 km
    2. nap: 0 km
    3. nap: 75 km
    ...
"""
print("6. feladat")
elso = 0 
masodik = 0 
harmadik = 0 
negyedik = 0 
otodik = 0 
hatodik = 0 
hetedik = 0 
for i in range(0,len(array)):   
    addkm = int(array[i][2])
    most = int(array[i][0])
    if(most == 1):
        elso = elso + addkm
    if(most == 2):
        masodik = masodik + addkm
    if(most == 3):
        harmadik = harmadik + addkm
    if(most == 4):
        negyedik = negyedik + addkm
    if(most == 5):
        otodik = otodik + addkm
    if(most == 6):    
        hatodik = hatodik + addkm
    if(most == 7):    
        hetedik = hetedik + addkm
        
print(" 1.nap: %d km \n 2.nap: %d km \n 3.nap: %d km \n 4.nap: %d km \n 5.nap: %d km \n 6.nap: %d km \n 7.nap: %d km \n" % (elso,masodik,harmadik,negyedik,otodik,hatodik,hetedik))
#%%
"""
7. A futár az egyes utakra az út hosszától függően kap fizetést az alábbi táblázatnak
megfelelően: 
 1 – 2 km 500 Ft
 3 – 5 km 700 Ft
 6 – 10 km 900 Ft
 11 – 20 km 1 400 Ft
 21 – 30 km 2 000 Ft
 
Kérjen be a felhasználótól egy tetszőleges távolságot, és határozza meg, hogy mekkora
díjazás jár érte! Ezt írja a képernyőre! 
"""

bevitt_adat=int(input("Adat (1-30) :"))

if(1 <= bevitt_adat <= 2):
    print("500Ft")
if(3 <= bevitt_adat <= 5):
    print("700Ft")
if(6 <= bevitt_adat <= 10):
    print("900Ft")
if(11 <= bevitt_adat <= 20):
    print("1 400Ft")
if(21 <= bevitt_adat <= 30):
    print("2 000Ft")
else:
    print("Error")
#%%
"""
8. Határozza meg az összes rögzített út ellenértékét! Ezeket az értékeket írja ki
a dijazas.txt állományba nap szerint, azon belül pedig az út sorszáma szerinti
növekvő sorrendben az alábbi formátumban:
1. nap 1. út: 700 Ft
1. nap 2. út: 900 Ft
1. nap 3. út: 2000 Ft
… 
"""
utpernap = [0,0,0,0,0,0,0]

for i in range(0,len(array)):
    cica = int(array[i][1])
    kutya = int(array[i][0])
    if(kutya == 1):
        utpernap[0]=utpernap[0]+1
    if(kutya == 2):
        utpernap[1]=utpernap[1]+1
    if(kutya == 3):
        utpernap[2]=utpernap[2]+1
    if(kutya == 4):
        utpernap[3]=utpernap[3]+1
    if(kutya == 5):
        utpernap[4]=utpernap[4]+1
    if(kutya == 6):
        utpernap[5]=utpernap[5]+1
    if(kutya == 7):
        utpernap[6]=utpernap[6]+1
print(utpernap)

newarray = []
for i in range(1,(utpernap[0]+1)):    
    for j in range(0,len(array)):
        szam = int(array[j][0])
        kukori =int(array[j][1])
        if(szam == 1 and kukori == i):
            ertek=int(array[j][2])
            newarray.append(ertek)
            
for i in range(1,(utpernap[2]+1)):    
    for j in range(0,len(array)):
        szam = int(array[j][0])
        kukori =int(array[j][1])
        if(szam == 3 and kukori == i):
            ertek=int(array[j][2])
            newarray.append(ertek)
            
            
for i in range(1,(utpernap[3]+1)):    
    for j in range(0,len(array)):
        szam = int(array[j][0])
        kukori =int(array[j][1])
        if(szam == 4 and kukori == i):
            ertek=int(array[j][2])
            newarray.append(ertek)
            
            
for i in range(1,(utpernap[4]+1)):    
    for j in range(0,len(array)):
        szam = int(array[j][0])
        kukori =int(array[j][1])
        if(szam == 5 and kukori == i):
            ertek=int(array[j][2])
            newarray.append(ertek)
            
            
for i in range(1,(utpernap[6]+1)):    
    for j in range(0,len(array)):
        szam = int(array[j][0])
        kukori =int(array[j][1])
        if(szam == 7 and kukori == i):
            ertek=int(array[j][2])
            newarray.append(ertek)
print(newarray)

penz = []

for i in range(0,len(newarray)):
    ertek=int(newarray[i])
    if(1 <= ertek <= 2):
        penz.append(500)
    if(3 <= ertek <= 5):
        penz.append(700)
    if(6 <= ertek <= 10):
        penz.append(900)
    if(11 <= ertek <= 20):
        penz.append(1400)
    if(21 <= ertek <= 30):
        penz.append(2000)
        
print(penz)
     
with open("dijazas2.txt", "w") as text_file:
    k=0
    for i in range(1,(utpernap[0]+1)):
        text_file.write("1.nap %d. ut: %d Ft\n" % (i,penz[k]))
        k=k+1
        
    for i in range(1,(utpernap[2]+1)):
        text_file.write("3.nap %d ut: %d Ft\n" % (i,penz[k]))
        k=k+1
        
    for i in range(1,(utpernap[3]+1)):
        text_file.write("4.nap %d ut: %d Ft\n" % (i,penz[k]))
        k=k+1 
        
    for i in range(1,(utpernap[4]+1)):
        text_file.write("5.nap %d ut: %d Ft\n" % (i,penz[k]))
        k=k+1  
        
    for i in range(1,(utpernap[6]+1)):
        text_file.write("7.nap %d ut: %d Ft\n" % (i,penz[k]))
        k=k+1   
text_file.close()   
      
#%%
"""
9. Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a heti
munkájáért! 
"""
zsozso = 0
for i in range(0,len(array)):
    bevitt_adat=int(array[i][1])
    
    if(1 <= bevitt_adat <= 2):
        zsozso = zsozso + 500 
    if(3 <= bevitt_adat <= 5):
        zsozso = zsozso + 700 
    if(6 <= bevitt_adat <= 10):
        zsozso = zsozso + 900 
    if(11 <= bevitt_adat <= 20):
        zsozso = zsozso + 1400 
    if(21 <= bevitt_adat <= 30):
        zsozso = zsozso + 2000 
    
print("9.feladat")
print("A kapott osszeg: %d Ft" % zsozso)
        

#%% MEGOLDÁSOK ÉRTÉKELÉSE
"""
Létezik a program futar néven, és az szintaktikailag helyes 1 pont
Üzenetek a képernyőn 2 pont
A bemeneti állomány feldolgozása 4 pont
Kiírta a hét első útjának hosszát 4 pont
Kiírta a hét utolsó útjának hosszát 5 pont
Szabadnapok kiírása 4 pont
Kiírta, hogy melyik nap volt a legtöbb fuvar 5 pont
Az egyes napokon megtett távok meghatározása 5 pont
Egy adott távhoz tartozó díjazás meghatározása 4 pont
dijazas.txt állomány létrehozása 8 pont
Heti munkadíj meghatározása 3 pont
Összesen: 45 pont 
"""