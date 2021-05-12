
naplo = {}
with open('naplo.txt', 'r', encoding='utf-8') as fajl4:
    for sor in fajl4:
        #print(sor.strip())
        if sor[0] == '#':
            datum_sor = sor.strip().split()
            datum = datum_sor[1] + ' ' + datum_sor[2]
            naplo[datum] = []
        else:
            bejegyzes = sor.strip().split()
            naplo[datum].append([bejegyzes[0] + ' ' + bejegyzes[1], bejegyzes[2]])
print(naplo)

"""
2. feladat: Határozza meg és irassa ki, hogy hány sor van fájlban, ami hiányzást rögzít.
"""

print('2.feladat')
szamlalo = 0
for datum in naplo:
    szamlalo += len(naplo[datum])
print(f'A naplóban {szamlalo} bejegyzés van.')


"""
3.feladat: Számolja meg és irassa ki, hogy hány óra igazolatlan hiányzás volt a félév során.
"""

print('3.feladat')
igazolt = 0
igazolatlan = 0
for datum in naplo:
    for bejegyzes in naplo[datum]:
        igazolt += bejegyzes[1].count('X')
        igazolatlan += bejegyzes[1].count('I')

print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlan {igazolatlan} óra')


"""
4. feladat: Készítsen függvényt hetnapja néven, amely a paraméterként megadott dátumhoz
            megadja, hogy az a hét melyik napjára esik. Tudjuk, hogy az adott év nem volt
            szökóév, továbbá azt is, hohy január elseje hétfóre esett. Használja a a tömbök 
            indexelését 0-val kezdődő, de ettől eltérő megoldású függvényt is készíthet.
"""

print('4.feladat')

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 273, 304, 335]
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]


"""
5. feladat: Kérjen be egy dátumot(hónap, nap), és a hetnapja függvény felhasználásával
            írassa ki, hogy az a hét melyik napjára esett.
"""

print('5.feladat')
honap_ssz = int(input('A hónap sorszáma='))
nap_ssz = int(input('A nap sorszáma='))
print(f'Azon a napon {hetnapja(honap_ssz, nap_ssz)} volt')

"""
6. feladat: Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítési óra óraszámát (pl kedd  3)
            Írassa ki, hogy a félév során az adott tanítási órára összesen hány hiányzás jutott.
"""

print('6.feladat')
nap_neve = input('A nap neve=')
ora = int(input('Az ora sorszáma='))
hianyzas = 0
for datum in naplo:
    if hetnapja(int(datum[:2]), int(datum[3:])) == nap_neve:
        for bejegyzes in naplo[datum]:
            if 'X' in bejegyzes[1][ora-1] or 'I' in bejegyzes[1][ora-1]:
                hianyzas += 1
print(f'Ekkor összesen {hianyzas} óra hiányzás történt.')


"""
7. feladat: Írassa ki a legtöbb órát hiányzó tanuló nevét. Ha több ilyen tanuló van, akkor mindenki jelenjen 
            meg szóközzel elválasztva. 
"""

print('7.feladat')
hianyzasok = {}
for datum in naplo:
    for bejegyzes in naplo[datum]:
        hianyzas = bejegyzes[1].count('X') + bejegyzes[1].count('I')
        if bejegyzes[0] in hianyzasok:
            hianyzasok[bejegyzes[0]] += hianyzas
        else:
            hianyzasok[bejegyzes[0]] = hianyzas
max_hianyzas = 0
for diak in hianyzasok:
    if hianyzasok[diak] > max_hianyzas:
        max_hianyzas = hianyzasok[diak]
for diak in hianyzasok:
    if hianyzasok[diak] == max_hianyzas:
        print(diak, end=' ')
