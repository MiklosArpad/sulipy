
epizod = {}
epizodok = []

adatok = []
with open('lista.txt', 'r', encoding='utf=8') as file:
    for sor in file:
        adatok.append(sor.strip())
        if len(adatok) == 5:
            epizod['datum'] = adatok[0]
            epizod['sorozat'] = adatok[1]
            epizod['resz'] = adatok[2]
            epizod['hossz'] = int(adatok[3])
            if adatok[4] =='1':
                epizod['latta'] = True
            else:
                epizod['latta'] = False

            epizodok.append(epizod)
            epizod = {}
            adatok = []

#print(epizodok)

"""
2. feladat: Irassa ki képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl,
            amelynek ismert az adásba kerülési dátuma.
"""

print('2. feladat')

szamlalo = 0
for epizod in epizodok:
    if 'NI' not in epizod['datum']:
        szamlalo += 1

print(f'A listában {szamlalo} db vetitési dátummal rendelkező epizod van')


""" 
3. feladat: Határozza meg, hogy a fájlban lévő epizodok hány százalékát látta már a listát 
            rögzitő személy. A százalékértéket, két tizedesjeggyel jelelnítse meg.
"""

print('3. feladat')

szamlalo = 0
for epizod in epizodok:
    if epizod['latta']:
        szamlalo += 1
szazalek = szamlalo / len(epizodok) * 100
print(f'A listában lévő epitodok {szazalek:.2f}% -át látta.')

"""
4. feladat: Számítsa ki, hogy összesen mennyi időt töltött a személy az epizodok megnézésével.
            Az ererdményt a minta szerint nap, óra, perc formában adja meg.
"""

print('4.feladat')

perc_osszesen = 0
for epizod in epizodok:
    if epizod['latta']:
        perc_osszesen += epizod['hossz']
nap = perc_osszesen // (24 * 60)
ora = perc_osszesen % (24 * 60) // 60
perc = perc_osszesen % 60
print(f'Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött')

"""
5. feladat: Kérjen be a felhasználótol egy dátumot "éééé.hh.nn" formában. Határozza meg, hogy az adott dátumig
            megjelent epizódokból melyeket nem látta még. Az aznapi epizódokat is számolja bele. A feltételnek 
            megfelelő epitódok esetén írja a képernyőre tabulátorral elválasztva az évad-és epizódszámot, 
            valamint a sorozat címét a minta szerint.
"""

print('5.feladat')
#
# datum = input('Adjon meg egy dátumot! Dátum= ')
# for epizod in epizodok:
#     if epizod['datum'] <= datum and not epizod['latta']:
#         print(epizod['resz'] + '\t' + epizod['sorozat'])



"""
6. feladat: Készítse el az algoritmus alapján a hét napját meghatározó függvényt.
            A függvény neve Hetnapja legyen. A függvény az év, hónap, nap megadása után
            szöveges eredményként visszaadja, hogy az adott nep a hét melyok napja volt. 
"""

print('6.feladat')

def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sz', 'cs', 'p', 'sz']
    honapok =[0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if honap < 3:
        ev -= 1

    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[honap-1] + nap) % 7]
    return hetnapja


"""
7. feladat: Kérjen be a felhasználól egy napot az előző feladtban látható rövidített alakban.
            A napokat egy 1, 2 vahy 3 karakterrel adja meg. Határozza meg, hogy a fájlban lévő
            sorozatok közül melyiket vatÍtik az adott napon. A sorozatok nevét a minta szerint jelenítse meg.
            Ha az adott napon egy sorozatot sem adtak adásba, akkor ezt írassa ki üzenetben.  
"""

print('7.feladat')

vizsgalt_nap = input('Adja meg a hét egy napját! Nap=')
aznapi_sorozatok = set()
for epizod in epizodok:
    if 'NI' not in epizod['datum']:
        epizod_datuma = epizod['datum'].split('.')
        epizod_napja = hetnapja(int(epizod_datuma[0]), int(epizod_datuma[1]), int(epizod_datuma[2]))
    if vizsgalt_nap == epizod_napja:
        aznapi_sorozatok.add(epizod['sorozat'])
if len(aznapi_sorozatok):
    for elem in aznapi_sorozatok:
        print(elem)
else:
    print('Az adott napon nem kerül adásba sorozat')

"""
8. feladat: Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát.
            A számításnál vegy figyelembe a vetítési dátummal nem rendelkező epizódokat is. A megoldás során
            felhasználhatja, hogy rgy sorozat epizódjainak adatai egymást követik a forrásállományban. A listát
            írja ki a summa.txt fájlba. A fájl egy sorában a sorozat címe, az adott sorozatra vonatkozó összesített
            vetítési idő őercben és az epizódok száma szerepeljen, szóközze elválasztva.
"""

print('8.feladat')

sorozatok = {}
for epizod in epizodok:
    if sorozatok.get(epizod['sorozat'], 0):
        sorozatok[epizod['sorozat']]['darab_resz'] += 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] += epizod['hossz']
    else:
        sorozatok[epizod['sorozat']] = {}
        sorozatok[epizod['sorozat']]['darab_resz'] = 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] = epizod['hossz']

#print(sorozatok)
with open('summa.txt', 'w', encoding='utf-8') as summa:
    for kulcs in sorozatok:
        print(kulcs, sorozatok[kulcs]['ossz_hossz'], sorozatok[kulcs]['darab_resz'], file=summa)








