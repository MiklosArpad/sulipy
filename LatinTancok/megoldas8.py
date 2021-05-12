
tanc = {}
tancok = []
adatok = []
with open('danceprogramme.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        #print(sor.strip())
        adatok.append(sor.strip())
        if len(adatok) == 3:
            tanc['nev'] = adatok[0]
            tanc['lany'] = adatok[1]
            tanc['fiu'] = adatok[2]
            tancok.append(tanc)
            tanc = {}
            adatok = []
print(tancok)

"""
2 .feladat: Írassa ki, hogy melyik volt az elsőként és melyik az utolsóként bemutatott tánc.
"""

print('2 feladat')

print(f"Az elsőként bemutatott tánc: {tancok[0]['nev']}")
print(f"Az utolsóként bemutatott tánc: {tancok[-1]['nev']}")

"""
3. feladat: Hány pár mutatta be a szambát? Írassa ki.
"""

print('3 feladat')

szamlalo = 0
for tanc in tancok:
    if tanc['nev'] == 'samba':
        szamlalo += 1
print(f'A samba-t összesen {szamlalo} pár mutatta be.')


"""
4. feladat: Írassa ki, hogy Vilma mely táncokban szerepelt.
"""

print('4 feladat')

print('Vilma az alábbi táncokban szerepelt:')
for tanc in tancok:
    if tanc['lany'] == 'Vilma':
        print(tanc['nev'], end=' ')


"""
5. feladat: Kérje be egy tánc nevét, majd írassa ki, hogy az adott táncot Vilma kivel 
            mutatta be. Pl. ha a bekért tánc a samba, és Vilma párja Bertalan volt, 
            akkor "A samba bemutatóján Vilma párja Bertalan volt." szöveg szerepeljen.
            Ha Vilma az adott tánc bemutatóján nem szerepelt, akkor azt írja ki, hogy
            "Vilma nem táncolt samba-t."
            
"""


print('5. feladat')

tanc_neve = input('Tánc neve: ')
volt_ilyen = False
for tanc in tancok:
    if tanc['nev'] == tanc_neve and tanc['lany'] == 'Vilma':
        print(f"A {tanc['nev']} bemutatóján Vilma párja {tanc['fiu']} volt.")
        volt_ilyen = True
if not volt_ilyen:
    print(f"Vilma nem táncolt {tanc_neve}-t.")



"""
6. feladat: Készítsen listát a bemutatón részt vett fiúkról és lányokról. A lány szereplok.txt
            nevű szöveges állományba mentse el. A neveket vesszők válasszák el, az utolsó ne 
            legyen írásjel.

"""

print('6 feladat')

with open('szereplok.txt', 'w', encoding='utf-8') as szereplok:
    fiuk = set()
    lanyok = set()
    for tanc in tancok:
        fiuk.add(tanc['fiu'])
        lanyok.add(tanc['lany'])
    elvalaszto = ', '
    print('Lányok: ', elvalaszto.join(lanyok), file=szereplok)
    print('Fiúk: ', elvalaszto.join(fiuk), file=szereplok)


"""
7. feladat: Írja ki a képernyőre, hogy melyik fiú szerepelt a legtöbbszőr a fiúk kötűl, és melyik
            melyik lány a lányok közűl. Ha több fiú, vagy több lány is megfelel a feltételeknek,
            akkor valamennyi fiú, illetve lány nevét írja ki.    
"""

print('7. feladat')

fiuk = {}
lanyok = {}

for tanc in tancok:
    if tanc['fiu'] not in fiuk:
        fiuk[tanc['fiu']] = 1
    else:
        fiuk[tanc['fiu']] += 1
    if tanc['lany'] not in lanyok:
        fiuk[tanc['lany']] = 1
    else:
        fiuk[tanc['lany']] += 1

print('A legtöbbszőr szereplő fiú(k):')
max_fiu = 0
for fiu in fiuk:
    if fiuk[fiu] > max_fiu:
        max_fiu = fiuk[fiu]
for fiu in fiuk:
    if fiuk[fiu] == max_fiu:
        print(fiu)

print('A legtöbbszőr szereplő lány(ok):')
max_lany = 0
for lany in lanyok:
    if lanyok[lany] > max_lany:
        max_lany = lanyok[lany]
for lany in lanyok:
    if lanyok[lany] == max_lany:
        print(lany)