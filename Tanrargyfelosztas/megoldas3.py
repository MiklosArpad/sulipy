
tantargyfelosztas = []
ora = {}
adatok = []
with open('beosztas.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        #print(sor.strip())
        adatok.append(sor.strip())
        if len(adatok) == 4:
            ora['tanar'] = adatok[0]
            ora['tantargy'] = adatok[1]
            ora['osztaly'] = adatok[2]
            ora['oraszam'] = int(adatok[3])
            tantargyfelosztas.append(ora)
            ora = {}
            adatok = []
print(tantargyfelosztas)

"""
2. feladat: Hány bejegyzés található az állományban? Az eredmény irassa ki
"""

print('2. feladat')

print(f'A fájlban {len(tantargyfelosztas)} bejegyzés található')

"""
3. feladat: A fenntartó számára fontos információ, hogy az iskolában hetente összesen hány 
            tanítási óra van. Határozza meg ezt az adatot, és irassa ki.
"""

print('3. feladat')

ossz_oraszam = 0
for ora in tantargyfelosztas:
    ossz_oraszam += ora['oraszam']
print(f'Az iskolában a heti összóraszám: {ossz_oraszam}')

"""
4. feladat: Kérje be a felhasználótol egy tanár nevét, és irassa ki, hogy hetente hány órában tanít.
"""

print('4.feladat')

#tanar = input('Kérem a tnár nevét= ')
#szamlalo = 0
#for ora in tantargyfelosztas:
   # if ora['tanar'] == tanar:
       # szamlalo += ora['oraszam']
#print(f'A tanár heti óraszáma: {szamlalo}')


"""
5. feladat: Készítse el az of.txt fájlt, mely az osztályfőnök nevét tartalmazza osztályonként 
"""

print('5.felaadat')

with open('of.rxt', 'w', encoding='utf-8') as of:
    for ora in tantargyfelosztas:
        if ora['tantargy'] == 'osztalyfonoki':
            print(f"{ora['osztaly']} - {ora['tanar']}", file=of)


"""
6. feladat: Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkoe az 
            adott tantárgyra és osztályra két bejegyzésst is tartalmaz a tantárgyfelosztás. Kérje be
            egy osztály azonosítóját, valamint egy tentárgy nevét, írassa ki, hogy az adott osztály
            a megadott tantárgyat cspoortbontásban vagy osztályszinten tanulja-e.
"""

print('6.feladat')

osztaly = input('Osztály= ')
tantargy = input('Tantárgy= ')
szamlalo = 0
for ora in tantargyfelosztas:
    if ora['osztaly'] == osztaly and ora['tantargy'] == tantargy:
        szamlalo += 1
if szamlalo > 1:
    print('CSoportbontásban tanulják.')
else:
    print('Osztályszinten tanulják.')


"""
7. feladat: A fenntartó számára az is fontos információ, hogy hány tanár dolgozik a iskolában. írassa ki.
"""

print('7.feladat')

tanarok = set()
for ora in tantargyfelosztas:
    tanarok.add(ora['tanar'])
print(f'Az iskolában {len(tanarok)} tanár tanít. ')

