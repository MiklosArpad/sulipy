
"""
1. feladat: Szimuláljon egy pénzfeldobást, ahol azonos esélye van a feknek és az írásnak is.
            Az eredményt írassa ki.
"""

import random

def dob():
    return "I" if random.randint(1, 2) == 1 else "F"

print('1.feladat')
print(f'A pénz feldobás eredménye: {dob()}')


"""
2. feladat: Kérjen be a felhsználó egy tippet, majd szimuláljon egy pénzfeldobást. Írassa ki a felhsználó
            tippjét és a dobás eredményét is, majd tájékoztassa a felhasználót az eredményről.
"""




print('2. feladat')
tipp = input('Tippeljen! (F/I)= ')
print('Az őn által megadott tipp: ', tipp)
if tipp == dob():
    print('Ön eltalálta.')
else:
    print('Ön nem találta el.')



"""
3. feladat: Állapítsa meg, hogy hány dobásból állt a kisérlet, és a választ írassa ki.
"""

print('3. feladat')

with open('kiserlet.txt', 'r') as file:
    szamlalo = 0
    for sor in file:
        szamlalo += 1
    print(f'A kisérlet {szamlalo} dobásból állt.')


"""
4. feladat: Milyen relatív gyakorisággal dobtunk a kisérlet során fejet? ( A fej relatív
            gyakorisága a fejet eredményező dobások és az összes dobás hányadosa.) A relatív
            gyakoriságot két tizedesjegy pontossággal, százalék formátumban írassa ki.
"""


print('4.feladat')

with open('kiserlet.txt', 'r') as file:
    szamlalo = 0
    fej = 0
    for sor in file:
        if sor.strip() == 'F':
            fej += 1
        szamlalo += 1
    print(f'A kisérlet során a fej relatív gyakorisága {fej / szamlalo * 100:.2f} % volt.')

"""
5. feladat. Hányszor fordult elő ebben a kisérletben, hogy egymás után pontosan két fejet dobtunk?
            A választ írassa ki. (min 3 dobás)
"""

print('5.feladat')

with open('kiserlet.txt', 'r') as file:
    szamlalo = 0
    ablak = ''
    for sor in file:
        if len(ablak) == 3 and ablak == 'FFI':
            szamlalo += 1

        if len(ablak) == 4:
            ablak = ablak[1:] + sor.strip()
            if ablak == 'IFFI':
                szamlalo += 1
        else:
            ablak += sor.strip()

    if ablak[1:] == 'IFF':
        szamlalo += 1
print(f'A kisérlet során összesen {szamlalo} alkalommal dobttak pontossan két fejet egymás után.')


"""
6. feladat: Milyen hosszú volt a leghosszabb, csak fejekből álló részsorozat? Írassa ki a választ.
            Adja meg egy ilyen részsorozat első tagjának helyét is.
"""

print('6. feladat')

with open('kiserlet.txt', 'r', encoding='utf-8') as file:
    tarolo = ''
    max_hossz = 0
    max_index = 0
    for index, sor in enumerate(file):
        if sor.strip() == 'F':
            tarolo += sor.strip()
            if len(tarolo) > max_hossz:
                max_hossz = len(tarolo)
                max_index = index - len(tarolo) +2
        else:
            tarolo = ''
        print(index, sor.strip())
print(f'A leghosszabb tiszta fej sorozat {max_hossz} tagból áll, kezdete, a(z) {max_index}. dobás')


"""
7. feladat: Állítson elő és tároljon a memóriában 1000 db négy dobásbó álló sorozatot. Számolja meg,
            hány esetben követett ehy háromtagú "tiszta fej" sorozatot fej, illetve hány esetben írás.
            Az eredményt írassa ki a dobasok.txt állományba úgy, hogy at első sorba kerüljön az eredmény,
            a második sorban pedig egy -egy szóközzel elválasztva egyetlen sorban szerepeljenek a 
            dobássorozatok.
"""

print('7feladat')

raktar = []
for index in range(1000):
    sorozat = ''
    for doobas in range(4):
        sorozat += dob()
    raktar.append(sorozat)
i_db = 0
f_db = 0
for sorozat in raktar:
    if sorozat == 'FFFI':
        i_db += 1
    if sorozat == 'FFFF':
        f_db += 1
with open('dobasok.txt', 'w') as dobasok:
    print(f'FFFi: {i_db} FFFF: {f_db}', file=dobasok)
    for sorozat in raktar:
        print(sorozat, end=' ', file=dobasok)
