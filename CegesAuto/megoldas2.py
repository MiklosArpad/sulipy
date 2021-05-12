
athaladas = {}
athaladasok = []

with open('autok.txt', 'r', encoding='utf-8') as file2:
    for sor in file2:
        # print(sor.strip())
        adatok = sor.strip().split()
        athaladas['nap'] = int(adatok[0])
        athaladas['idopont'] = adatok[1]
        athaladas['rendszam'] = adatok[2]
        athaladas['szemely'] = adatok[3]
        athaladas['km'] = int(adatok[4])
        if adatok[5] == '0':
            athaladas['ki'] = True
        else:
            athaladas['ki'] = False
        athaladasok.append(athaladas)
        athaladas = {}

# print(athaladasok)


""" 
2. feladat:  Adja meg, hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának megfelelően
             írja ki a képernyőre!   
"""

print('2.feladat')

utolso_kilepes = 0
for index, athaladas in enumerate(athaladasok):
    if athaladas['ki']:
        utolso_kilepes = index
print(f"{athaladasok[utolso_kilepes]['nap']}. nap rendszám: {athaladasok[utolso_kilepes]['rendszam']}")

"""
3. feladat: Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és hozták vissza
            az adott napon!
"""

print('3.feladat')

nap = int(input('Nap: '))
print(f"Forgalom az {nap}. napon:")
for athaladas in athaladasok:
    if athaladas['nap'] == nap:
        irany = 'ki' if athaladas['ki'] else 'be'
       # print(f"{athaladas['idopont']} {athaladas['rendszam']} {athaladas['szemely']} {irany}")


"""
4. feladat: Adja meg, hogy mennyi autó nem volt bent a hónap végén a parkolóban!
"""

print('4.feladat')


kint_van = set()
for athaladas in  athaladasok:
    if athaladas['ki']:
        kint_van.add(athaladas['rendszam'])
    else:
        kint_van.remove(athaladas['rendszam'])

print(f'A hónap végén {len(kint_van)} autót nem hozták vissza.')

"""
5. feladat: Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban
            megtett távolságot kilóméterben! A hónap végén még kint lévő autók esetén az utolsó rögzített
            kilóméterállással számoljon! A kiírásban az autók sorrendje tetszőleges lehet.
"""

print('5.feladat')


megtett_km = {}
for athaladas in athaladasok:
    if megtett_km.get(athaladas['rendszam'], 0):
        megtett_km[athaladas['rendszam']]['aktualis km'] = athaladas['km']
    else:
        megtett_km[athaladas['rendszam']] = {}
        megtett_km[athaladas['rendszam']]['kezdo km'] = athaladas['km']
        megtett_km[athaladas['rendszam']]['aktualis km'] = athaladas['km']

print(megtett_km)
for rendszam in megtett_km:
   print(rendszam, megtett_km[rendszam]['aktualis km'] - megtett_km[rendszam]['kezdo km'])

"""
6. feladat: Határozza meg melyik személy volt az, aki az autó elvitele alatt a leghosszabb távolságot
            tette meg. A személy azonosítóját és megtett kilómétert a mointa szerint irja a képernyőre.
"""

print('6.feladat')

max_km = 0
max_szemely = None
for index, athaladas in enumerate(athaladasok):
    if not athaladas['ki']:
        vissza_index = index - 1
        while athaladas['rendszam'] != athaladasok[vissza_index]['rendszam']:
            vissza_index -= 1
        if athaladas['km'] - athaladasok[vissza_index]['km'] > max_km:
            max_km = athaladas['km'] - athaladasok[vissza_index]['km']
            max_szemely = athaladas['szemely']
print(f'leghosszabb út: {max_km} km, személy: {max_szemely}')


"""
7.feladat: Az autók esetén egy havi menetlevelet kell készíteni. Kérjen be a felhasználótol egy rendszámot. 
            készítsen egy x_menetlevel.txt állományt, melybe elkészíti az adott rendszámú autó menetlevelét.
            (Az x helyére az autó rendszáma kerüljön) A file-ba soronként tabulátorral elválasztva a személy
            azonosítóját, a kivitel időpontját (nap, óra, perc), a kilóméterszámláló állását,a visszahozatal
            időpontját (nap, óra, perc), és a kilóméter állását irja a minta szerint. A TAB kódja ASCII : 9
"""

print('7. feladat')

rendszam = input('Rendszám: ')
filenev = rendszam + '_menetlevel.txt'
with open(filenev, 'w', encoding='utf-8') as menetlevel:
    for athaladas in  athaladasok:
        if athaladas['rendszam'] == rendszam:
            if athaladas['ki']:
                print(athaladas['szemely'] + '\t' + str(athaladas['nap'])
                      + '\t' + athaladas['idopont'] + '\t'
                      + str(athaladas['km']) + 'km\t', end='', file=menetlevel)
            else:
                print(str(athaladas['nap'])
                      + '\t' + athaladas['idopont'] + '\t'
                      + str(athaladas['km']) + 'km\t', file=menetlevel)

print('Menetlebél kész.')