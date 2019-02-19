import sys



def main():
    print("\n1.feladat\n")    
    array=function_A()
        
    print("\n2.feladat\n")
    function_B(array)
    
    print("\n3.feladat\n")
    function_C(array)
    
    print("\n4.feladat\n")
    function_D(array)
    
    print("\n5.feladat\n")
    function_E(array)
    
    print("\n6.feladat\n")
    function_F(array)
    
    print("\n7.feladat\n")
    function_G(array)
    
    print("\n8.feladat\n")
    function_H(array)
    
    print("\n9.feladat\n")
    function_I(array)
    
    
    
"""
1. Olvassa be a tavok.txt állományban talált adatokat, s annak felhasználásával oldja meg
a következő feladatokat! 
"""
def function_A():
    
    with open("tavok.txt", "r") as filepointer:
        array = []
        for line in filepointer:
            info = line.replace('\n','').split(' ')
            array.append(info)
    filepointer.close()
    
    #optional
    """
    print(array)
    print(array[0][0])
    print(array[0][1])
    print(array[0][2])
    """
    return array #így adunk vissza értéket!



"""
2. Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben! Figyeljen arra,
hogy olyan állomány esetén is helyes értéket adjon, amiben például a hét első napján
a futár nem dolgozott! 
"""
def function_B(array):
    
    legkisebbnap = 8 #szélsőértékdefiníció
    for i in range(0,len(array)):
        hasonlito=int(array[i][0])
        if( hasonlito < legkisebbnap):
            legkisebbnap = hasonlito
    print("A het legelso utja %s km volt" % array[legkisebbnap][2]) # %s, mert sztringet iratunk ki
    
    

"""
3. Írja ki a képernyőre, hogy mekkora volt a hét utolsó útja kilométerben! 
"""        
def function_C(array):
    
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
        
    print("A het utolso utja: %d km volt" % (utolsout))
        
        
    
"""
4. Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot. Írja ki a képernyőre,
hogy a hét hányadik napjain nem dolgozott a futár! 
"""        
def function_D(array):
    
    munka = [0,0,0,0,0,0,0]
    for i in range(0,len(array)):
        cucc = int(array[i][0])
        ujrair = cucc-1
        munka[ujrair]=1
    for k in range(0,len(munka)):
        if(munka[k]==0):
            print("A %d. napon nem dolgozott a futar" % (k+1))
    
    
"""
5. Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar! Amennyiben több nap
is azonos, maximális számú fuvar volt, elegendő ezek egyikét kiírnia. 
"""       
def function_E(array):
    
    legtobbfuvarnap = 8
    legtobbfuvar = 0
    for i in range(0,len(array)):   
        szam= int(array[i][1])
        if(legtobbfuvar < szam):
            legtobbfuvar=szam
            legtobbfuvarnap=int(array[i][0])

    print("A het legtobb fuvaros napja: %d" % legtobbfuvarnap)


"""
6. Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon hány
kilométert kellett tekerni! 

    1. nap: 124 km
    2. nap: 0 km
    3. nap: 75 km
    ...
"""        
def function_F(array):
    
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
def function_G(array):
    
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
        
    
    
"""
8. Határozza meg az összes rögzített út ellenértékét! Ezeket az értékeket írja ki
a dijazas.txt állományba nap szerint, azon belül pedig az út sorszáma szerinti
növekvő sorrendben az alábbi formátumban:
1. nap 1. út: 700 Ft
1. nap 2. út: 900 Ft
1. nap 3. út: 2000 Ft
… 
"""        
def function_H(array):
    
    utpernap = [0,0,0,0,0,0,0]

    for i in range(0,len(array)):
        #cica = int(array[i][1])
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
      
    
    
"""
9. Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a heti
munkájáért! 
"""
def function_I(array):
    
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
    
    print("A kapott osszeg: %d Ft" % zsozso)



if __name__ == "__main__":
    main()