n = 1
while n < 3:
    m = n + 1
    while m < 4:
        print('Hello!')
        m += 1
    n += 1

print()

sor = 1
while sor <= 3:
    oszlop = 1
    while oszlop <= 5:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1
print()

darab_karakter = 1
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

print()

tantargyak = ['matek', 'töri', 'biologia', 'kémia', 'magyar', 'angol', 'info']

index = 1
for tantargy in tantargyak:
    print(index, tantargy)
    index += 1

print()
for index, tantargy in enumerate(tantargyak):
    print(index, tantargy)

print()

nyelvek = ['Python', 'C++', 'C#', 'Java', 'Angular', 'Kotlin', 'Python']
web = ['HTML', 'CSS', 'PHP', 'Json', 'JavaScript', 'Jquery']

if 'C' in nyelvek:
    print(nyelvek.index('C'))
else:
    print('Nem eleme.')

print(nyelvek.count('Python'))

nyelvek.extend(web)
nyelvek.append('COBOL')
nyelvek.insert(1, 'C')

nyelvek.pop(0)
nyelvek.remove('Java')
#nyelvek.clear()

print(nyelvek)

masolat = nyelvek.copy()
print(masolat)

print()
# list comprehensions

eredeti = [11, 19, 7, -3]
eredmény = []

for x in eredeti:
    eredmény.append(x * 2)
print(eredeti)
print(eredmény)

# ugyanez egyszerúbben

eredeti =[17, 39, 47, -36]
eredmény = [x *2 for x in eredeti]

print(eredmény)

print()

# csak a pozitív elemeket írja ki és szorozza meg 2 -vel
eredeti =[17, 39, 47, -36]
eredmény = [x * 2 for  x in  eredeti if x > 0]
print(eredmény)

print()

# csak a páros számokat emelje négyzetre
original = [10, 11, 12,  13, 14, 15, 16, 17, 18, 19, 20]
qube = [x * x for x in original if x % 2 == 0]
print(qube)

# csak a párosok kiiratása

original = [10, 11, 12,  13, 14, 15, 16, 17, 18, 19, 20]
pairs = [x for  x in  original if x % 2 == 0]

print(pairs)
print()

# eldöntés tétel

szamok = [2, 5, 4, 8, 9, 10, 11, 12]

talalat = False
index = 0
while index < len(szamok) and not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('van a listában hárommal osztható szám, az indexe: ', index - 1)
else:
    print('Nincs a listában hárommal osztható szám')

print()

szamok = [2, 5, 4, 8, 9, 10, 11, 12]

talalat = False
index = 0
while not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
    index = index + 1

print('van a listában hárommal osztható szám, az indexe: ', index - 1)


# megszámlálás tétel

szamok = [12, 11, 5, 4, 8, 9, 16, 6, 10, 21]
darab = 0
for szam in szamok:
    if szam % 3 ==0:
        darab += 1
print('A 3-al osztható számok darabszáma: ', darab)
print()


szavak = ['Elemér', 'tó', 'ajtó', 'róka', 'egér', 'Aladár', 'pingvin']
print(len('pingvin'))

darab = 0
for szo in szavak:
    if len(szo) > 4:
        darab += 1

print('A listában szereplő szavak amik több mint 4 betűből állnak: ', darab)

print()

# min és max keresések

szamok = [102, 77, 55, 4, -62, 10, 12, 6, 33, 56]

min = szamok[0]
max = szamok[0]
for szam in szamok:
    if szam < min:
        min = szam
    if szam > max:
        max = szam
print('A lista legkisebb és legnagyobb eleme: ', min, max)
print(f'A lista legkisebb: {min}, és  legnagyobb eleme: {max}')

print()

szavak = ['Elemér', 'tó', 'ajtó', 'róka', 'egér', 'Aladár', 'pingvin']
legrovidebb = szavak[0]
leghosszabb = szavak[0]
for szo in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo
    if len(szo) > len(leghosszabb):
        leghosszabb = szo
print('A lista legrövidebb és leghosszabb szava: ', legrovidebb, leghosszabb)


# eljárások pl: subrutin egy metódus egy helyen van a programban elhelyezve, és csak valahol hivatkozok rá
# és többszőr felhasználható

def hello():
    print('Wellcome!')

def hello_wihh_name(name):
    print('Hello ' + name + ', Wellcome!')
hello_wihh_name('Viktoria')

def hello_with_2_name(name1, name2):
    print('Hello ' + name1 + ' and ' + name2 + ', Wellcome!')
hello_with_2_name('Jack', 'Jill')


def osszead(x,y):
    eredmeny = x + y
    print('A két szám összege: ', eredmeny)
osszead(4+5, 7-1)

print()

def kiir():
    lokalis = 'alma'
    print(lokalis)

globalis = 'gyümölcs'
kiir()
print(globalis)

print()

def festek_kalkulator(x, y):
    t = x * y
    l = t * 0.13
    return l
    # vagy ez a tétel egy sorban is kiiratható   -- return x * y * 0.13 --

szelesseg = 12  #float(input('Add meg a fal szélességét! '))
magassag = 11  #float(input('Add meg a fal magasságát! '))

liter = festek_kalkulator(szelesseg, magassag)


ar = festek_kalkulator(szelesseg, magassag) * 700

print('A fal festéséhez kb. ' + str(liter) + ' liter festekre van szükség és ' + str(ar) + ' Ft. -ba kerül')

print()

def max_kereso(x, *args):
    max = x
    for szam in args:
        if szam > max:
            max = szam
    return max
print(max_kereso(1, 19, 11, 7, 17))

