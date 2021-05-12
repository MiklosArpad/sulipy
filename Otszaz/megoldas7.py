vasarlasok = []
kosar = {}
with open('penztar.txt', 'r', encoding='utf-8') as file7:
    for sor in file7:
        #print(sor.strip())
        if sor.strip() == 'F':
            vasarlasok.append(kosar)
            kosar = {}
        else:
            if sor.strip() not in kosar:
                kosar[sor.strip()] = 1
            else:
                kosar[sor.strip()] += 1
print(vasarlasok)

"""
2. feladat: Határozza meg, hphy hányszor fizettek a pénztárnál.
"""

print('2.feladat')

print(f'A fizetések száma: {len(vasarlasok)}')


"""
3. feladat: Írja ki, hogy az első vásárlónak hány darab árúcikk volt a kosarában.
"""

print('3.feladat')

szamlalo = 0
for arucikk in vasarlasok[0]:
    szamlalo += vasarlasok[0][arucikk]
print(f'Az első vásárló {szamlalo} darab árúcikket vásárolt.')


"""
4. feladat: Kérje be a felhasználótól egy vásárlás sorszámát, egy árúcikk nevét és egy darabszámot.
            Feltételezheti, hogy a program futtatásakor csak a bemeneti állományban rögzített adatoknak
            megfelelő vásárlási sorszámot és árúcikknevet ad meg a felhasználó.
"""

print('4.feladat')

sorszam = 2  #int(input('Adja meg egy vásárlás sorszámát. '))
aru = 'kefe' #int(input('Adja meg egy árúcikk nevét. '))
darab = 2 #int(input('Adja meg a vásárolt darabszámpt. '))



"""
5. feladat: Határozza meg. hogy a bekért árúcikkből
                - melyik vásárláskor vettek előszőr, és melyiknél utoljára
                - összesen hány alkalommal vásároltak
"""

print('5.feladat')

meg_nem = True
szamlalo = 0
utolso = 0
for index, kosar in enumerate(vasarlasok):
    for arucikk in kosar:
        if arucikk == aru and meg_nem:
            print(f'Az első vásárlás sorszáma: {index + 1}')
            meg_nem = False
        if arucikk ==aru:
            szamlalo += 1
            utolso = index
print(f'Az utolsó vásárlás sorszáma: {utolso + 1}')
print(f'{szamlalo} vásárlás során vettek belőle.')


"""
6. feladat: Határozza meg, hogy a bekért darabszámotvásárolva egy termékből mennyi a fizetendő
            összeg. A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz
            a fizetendő összeget rendeli.
"""

print('6.feladat')

def ertek(db):
    if db == 1:
        return 500
    elif db == 2:
        return 500 + 450
    else:
        return 500 + 450 + (db-2) * 400
print(f'2 darab vételkor fizetendő: {ertek(2)}')


"""
7. feladat: Határozza meg, hogy a bekért sorszámú vásárláskor mely árúcikkekből és milyen mennyi-
            ségben vásároltak. Az árúcikkek nevét tetszőleges sorrendben megjelenítheti.
"""

print('7.feladat')

for arucikk in  vasarlasok[sorszam-1]:
    print(f'{vasarlasok[sorszam-1][arucikk]} {arucikk}')


"""
8. feladat: Készítse el az osszeg.txt fájlt. amelybe soronként az egy-egy vásárlás alkalmával
            fizetendő összeg kerüljön.
"""

print('8.feladat')

with open('osszeg.txt', 'w', encoding='utf-8') as osszeg:
    for index, kosar in enumerate(vasarlasok):
        fizetendo = 0
        for arucikk in kosar:
            fizetendo += ertek(kosar[arucikk])
        print(f'{index + 1}: {fizetendo}', file=osszeg)