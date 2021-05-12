
furdo = {}
with open('baddaten.txt', 'r', encoding='utf-8') as file6:
    for sor in file6:
        #print(sor.strip())
        adatok = sor.strip().split()
        ido = int(adatok[3]) * 3600 + int(adatok[4]) * 60 + int(adatok[5])
        if int(adatok[0]) not in furdo:
            furdo[int(adatok[0])] = {}
            furdo[int(adatok[0])][int(adatok[1])] = []
            furdo[int(adatok[0])][int(adatok[1])].append(ido)
        else:
            if int(adatok[1]) not in furdo[int(adatok[0])]:
                furdo[int(adatok[0])][int(adatok[1])] = []
            furdo[int(adatok[0])][int(adatok[1])].append(ido)
print(furdo[145])


"""          
2. feladat:  Írassa ki. hogy az első és az utolsó vendég mikor lépett ki az öltözőből

"""

print('2.feladat')

# az idő perc és mpercre való átalakítása, vissza a síma intből, hogy ki lehessen íratni

def atvalt(sec):
    p, mp = divmod(sec, 60)
    o, p = divmod(p, 60)
    return f"{o}:{p}:{mp}"


meg_nem = True
utolso = None
for vendeg in furdo:
    if meg_nem:
        print(f"Az első vendég {atvalt(furdo[vendeg][0][0])} -kor lépett ki az öltözőből.")
        meg_nem = False
    utolso = furdo[vendeg][0][0]
print(f"Az utolsó vendég {atvalt(utolso)} -kor lépett ki az öltözőből.")

"""
3.feladat: Határozza meg és írassa ki, hogy hány olyan fürdővendég volt, aki az öltözőn kívül
           csak egy részlegen jáárt és azt azt a részleget csak egyszer használta. MEGSZÁMLÁLÁS
"""

print('3.feladat')

szamlalo = 0
for vendeg in furdo:
    egy_reszleg = True
    if len(furdo[vendeg]) == 2:
        for reszleg in furdo[vendeg]:
            if len(furdo[vendeg][reszleg]) != 2:
                egy_reszleg = False
    else:
        egy_reszleg = False
    if egy_reszleg:
        szamlalo += 1
print(f"A fürdőben {szamlalo} vendég járt csak egy részlegen.")


"""
4. feladat: Határozza meg, hogy melyik vendég töltötte a legtöbb időt a fürdőben. A vendég 
            azonosítóját és a fürdőben tartozkodás idejét írja ki a képernyőre! A fürdőben
            a legtöbb időt töltő vendégek közül elegendő egy vendég adatait megjeleníteni. MAXIMUM KERESÉS
"""

print('4.feladat')

max_ido = 0
max_vendeg = 0
for vendeg in furdo:
    if furdo[vendeg][0][1] - furdo[vendeg][0][0] > max_ido:
        max_ido = furdo[vendeg][0][1] - furdo[vendeg][0][0]
        max_vendeg = vendeg
print("A legtöbb időt eltöltő vendég:")
print(f" {max_vendeg}. vendeg {atvalt(max_ido)}")


"""
5. feladat: Készítsen statisztikát, hogy 06:00:00 - 08:59:59 óra között, 09:00:00 - 15:59:59 óra
            között és 16:00:00 - 19:59:59 között hány vendég érkezett a fürdőbe. Az eredményt írja ki.
"""

print('5.feladat:')

ora6_9 = 0
ora9_16 = 0
ora16_20 = 0
for vendeg in furdo:
    if 6 * 3600 <= furdo[vendeg][0][0] <= 9 * 3600:
        ora6_9 += 1
    elif 9 * 3600 <= furdo[vendeg][0][0] <= 16 * 3600:
        ora9_16 += 1
    else:
        ora16_20 += 1

print(f"6-9 óra között {ora6_9} vendég")
print(f"9-16 óra között {ora9_16} vendég")
print(f"16-20 óra között {ora16_20} vendég")



"""
6. feladat: Készítsen egy listát a szauna részlegen járt vendégekről és az általuk ott töltött időről.
            A vendág azonosítóját és a részlegen eltöltött időt a szauní.txt fájlba írja ki. A fájlban
            egy sorban a vendég azonosítója és szóközzel elválasztva a részlegen eltöltött idő szerepel-
            jen őóra:perc:másodperc formában. Egy vendég a szauna részlegen a nap folyamán többször is 
            járhatott.  
"""

print('6. feladat')

with open('szauna.txt', 'w', encoding='utf-8') as szauna:
    for vendeg in furdo:
        ido_szauna = 0
        if 2 in furdo[vendeg]:
            for index in range(0, len(furdo[vendeg][2])-1, 2):
                ido_szauna += furdo[vendeg][2][index+1] - furdo[vendeg][2][index]
            if ido_szauna:
                print(f'{vendeg} {atvalt(ido_szauna)}', file=szauna)


"""
7. feladat: Készítsen egy listát, amelyben megadja, hogy az egyes részlegeket hányan használták. Az 
            eredményt írja ki. Ha egy vendég egy részlegen többször is járt a nap folyamán, azt a 
            statisztikában csak egynek számolja.
"""


print('7feladat')

uszoda = 0
szaunak = 0
medencek = 0
starnd = 0

for vendeg in furdo:
    if 1 in furdo[vendeg]:
        uszoda += 1
    if 2 in furdo[vendeg]:
        szaunak += 1
    if 3 in furdo[vendeg]:
        medencek += 1
    if 4 in furdo[vendeg]:
        starnd += 1
print(f'uszoda: {uszoda}')
print(f'szaunak: {szaunak}')
print(f'medencek: {medencek}')
print(f'strand: {starnd}')
