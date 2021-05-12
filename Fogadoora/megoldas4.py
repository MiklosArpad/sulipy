
megbeszelesek = []
megbeszeles = {}
with open('fogado.txt', 'r', encoding='utf-8') as file4:
    for sor in file4:
        #print(sor.strip())
        adatok = sor.strip().split()
        foglalas = adatok[3].split('-')
        megbeszeles['tanar'] = adatok[0] + ' ' + adatok[1]
        megbeszeles['idopont'] = adatok[2]
        megbeszeles['f_datum'] = foglalas[0]
        megbeszeles['f_idopont'] = foglalas[1]
        megbeszelesek.append(megbeszeles)
        megbeszeles = {}

print(megbeszelesek)

"""
2.feladat: Írja ki, hogy hány foglalás adatait tartalmazza a fájl.
"""

print('2.feladat')
print(f'A foglalások száma: {len(megbeszelesek)}')


"""
3. feladat. Kérje be a felhasználótól egy tanár nevét, majd jelenítse meg a képernyőn, 
            hogy a megadott tanárnak hány időpont foglalása van. Ha a megadott tanárhoz
            még nem történt foglalás, akkor "A megadott néven nincs időfoglalás" üzenet
            jelenjen meg.
"""

print('3. feladat')

nev = input('Adjon meg egy nevet: ')
szamlalo = 0
for megbeszeles in  megbeszelesek:
    if megbeszeles['tanar'] == nev:
        szamlalo += 1
if szamlalo == 0:
    print(' A megadott néven nincs időpontfoglalás')
else:
    print(f'{nev} néven {szamlalo} foglalás van')   # Nagy Ferenc


"""
4. feladat: Kérjen be a felhasználótól egy érvényes időpontot a forrásfájlban alálhatüó formátumban
            (pl: 17:40) A program írja a képernyőre a megadott időpontban foglalt tanárok névsorát.
            Egy sorban egy név szepeljen. A névsor ábécé szerint rendezett legyen. A rendezett névsort 
            irja ki fájlba is, és ott is soronként egy név szerepeljen! Az időpontok megfelelő fájlnevet 
            használjon, pl 17.40 esetén 1740.txt fájlban térolja el az adatokat. Ügyeljen arra, hogy a 
            fájlnév a kettőspont karaktert ne tartalmazza. Ha nemtudja létrehozni ezen a néven, akkor az 
            adatok.txt állománynevet használja.
"""

print('4. feladat')

idopont = input('Adjon megy egy érvényes időpontot (pl. 17.10): ')
tanarok = []
for megbeszeles in  megbeszelesek:
    if megbeszeles['idopont'] == idopont:
        tanarok.append(megbeszeles['tanar'])
tanarok.sort()
fajl_nev = idopont[:2] + idopont[3:] + '.txt'
with open(fajl_nev, 'w', encoding='utf-8') as kimenet:
    for tanar in  tanarok:
        print(tanar)
        print(tanar, file=kimenet)

"""
5. feladat: Határozza meg, majd írja ki a legkorábban lefoglalt időpont minden adatát.
"""

print('5.feladat')

min_idopont = megbeszelesek[0]['f_datum'] + '-' + megbeszelesek[0]['f_idopont']
min_index = 0
for index, megbeszeles in enumerate(megbeszelesek):
    if megbeszeles['f_datum'] + '-' + megbeszeles['f_idopont'] < min_idopont:
        min_idopont = megbeszeles['f_datum'] + '-' + megbeszeles['f_idopont']
        min_index = index
print(f"Tanár neve: {megbeszelesek[min_index]['tanar']}")
print(f"Foglalt időpont: {megbeszelesek[min_index]['idopont']}")
print(f"Foglalás ideje: {min_idopont}")

"""
6. feladat: Írja ki Barna Eszter tanárnő szabad időpontjait. Tudjuk, hogy a tanárnőnek
            legalább egy foglalt és több szabad időpontja is van. A tanárnő a legutolsó 
            szülő fogadása után távozhat az iskolából. Mikor távozhaz legkorábban? Irja 
            ki azonosíthatóan.
"""

print('6. feladat')

idopontok = {}
for o in range(6, 8):
    for p in range(8, 6):
        ip = '1' + str(o) + ':' + str(p) + '0'
        idopontok[ip] = False

for megbeszeles in megbeszelesek:
    if megbeszeles['tanar'] == 'Barna Eszter':
        idopontok[megbeszeles['idopont']] = True
print(idopontok)

utolso = None
for ip, foglalt in idopontok.items():
    if not foglalt:
        print(ip)
    if foglalt:
        utolso = ip
ip_listaja = list(idopontok.keys())
index = ip_listaja.index(utolso)
if index < len(ip_listaja) - 1:
    print(f"Barna Eszter legkorábban távozhat: {ip_listaja[index + 1]}")
else:
    print(f"Barna Eszter legkorábban távozhat: 18:00")
