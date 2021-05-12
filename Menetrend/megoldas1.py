
menetrend = {}
with open('vonat.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        #print(sor.strip())
        adatok = sor.strip().split()
        for index, elem in enumerate(adatok):
            if index != 4:
                adatok[index] = int(elem)

        if adatok[0] not in menetrend:
            menetrend[adatok[0]] = {}
        if adatok[1] not in menetrend[adatok[0]]:
            menetrend[adatok[0]][adatok[1]] = {}
        if adatok[4] == 'I':
            menetrend[adatok[0]][adatok[1]]['indulas'] = adatok[2] * 60 + adatok[3]
        else:
            menetrend[adatok[0]][adatok[1]]['erkezes'] = adatok[2] * 60 + adatok[3]

print(menetrend)

"""
2. feladat: Írja ki a képernyőre a fájlban tárolt vonatok és állomáspk darabszámait - 
            a kezdő és végállomást is beleértve.
"""

print('2.feladat')

print(f'A vonatok száma: {len(menetrend)}')
print(f'Az állomások száma: {len(menetrend[1])}')


"""
3. feladat: Határozza meg, hogy melyik állomáson állt a vonat legtöbbet. Adja meg a vonat és állomás 
            azonosítóját, valamint az állás idejét. Ha több ilyen volt, elég csak az egyiket megoldania.
"""

print('3.feladat')

maximum = {'allasido': menetrend[1][1]['indulas'] - menetrend[1][1]['erkezes'], 'vonat': 1, 'allomas': 1}
for vonat in menetrend:
    for allomas in  range(1, len(menetrend[vonat])-1):
        if menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes'] > maximum['allasido']:
            maximum['allasido'] = menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes']
            maximum['vonat'] = vonat
            maximum['allomas'] = allomas
print(f"A(z) {maximum['vonat']}. a(z) {maximum['allomas']}. állomásom {maximum['allasido']} percer állt.")

"""
4. feladat: olvassa be egy vonat azonosítóját, valamint egy időpont óra perc értékét. A későbbi feladatokban
            használja ezeket
"""

print('4.feladat')

vizsgalt_vonat = 2 # int(input('Adja meg egy vonat azonosítóját!'))
ora_perc = '7 16' # input('Adjon meg egy időpontot(óra perc)!')


"""
5. feladat: Ezen a vonalon az előírt menetidő 2 óra 22 perc. Írja ki a képernyőre, hogy a beolvasott azonosítójú
            vonat hány perccewl tért el ettől.
"""

print('5.feladat')

eloirt = 2 * 60 + 22
elteres = eloirt - (menetrend[vizsgalt_vonat][len(menetrend[vizsgalt_vonat]) -1]['erkezes']- menetrend[vizsgalt_vonat][0]['indulas'])
if elteres < 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel rövidebb volt a előírtnál.')
elif elteres == 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja pontosan az előírt ideig tartott.')
else:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel hosszab volt az előírtnál.')




"""
6. feladat: Írja a hadX.txt fájlba a beolvasott azonosítójú vonat melyik állomásra, mikor érkezett.
            A fájlnévben az x helyére a beolvasott vonatazonosító kerüljön.
"""
# print('6.feladat')

def valto(m):
    return str(m // 60) + ':' + str(m % 60)

filenev = 'halad' + str(vizsgalt_vonat) + '.txt'
with open(filenev, 'w') as halad:
    for allomas in range(1, len(menetrend[vizsgalt_vonat])):
        print(f"{allomas}. {valto(menetrend[vizsgalt_vonat][allomas]['erkezes'])}", file=halad)



"""
7. feladat: Adja meg, hogy a beolvasott időpontbanúton lévő, azaz a már elidúlt, de a végállomást
            még el nem érő vonatok közűl melyik hol tartott. A tesztelés során a következő időpontokra
            érdemes figyelni 6.50, 8:45, 9:05, 10.04, 10:20
"""

print('7.feladat')

idopont = int(ora_perc.split()[0]) * 60 + int(ora_perc.split()[1])
for vonat in menetrend:
    if menetrend[vonat][0]['indulas'] < idopont < menetrend[vonat][1]['erkezes']:
        print(f"a(z) {vonat}. vonat a 0. és az 1. állomás között járt.")
    for allomas in  range(1, len(menetrend[vonat])-1):
        if menetrend[vonat][allomas]['erkezes'] <= idopont <= menetrend[vonat][allomas]['indulas']:
            print(f"A(z) {vonat}. vonat a {allomas}. állomáson állt.")
        if menetrend[vonat][allomas]['indulas'] < idopont < menetrend[vonat][allomas + 1]['erkezes']:
            print(f"A(z) {vonat}. vonat a {allomas}. és a {allomas + 1}. állomás között járt.")





