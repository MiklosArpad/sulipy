
adatok = []
with open('forras.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        #print(sor.strip())
        adatok.append(sor.strip())
print(adatok)

diak = {}
diakok = []
for elem in adatok:
    diak_adatok = elem.split()
    diak['vezeteknev'] = diak_adatok[0]
    diak['keresztnev'] = diak_adatok[1]
    diak['kor'] = int(diak_adatok[2])
    diak['osztaly'] = diak_adatok[3]
    if diak_adatok[4] == '1':
        diak['kollegista'] = True
    else:
        diak['kollegista'] = False
    diakok.append(diak)
    diak = {}

print(diakok)

"""
1. feladat: 
10.A osztályoa tanulók neveinek kiiratása
"""
print('\n------------------> 1. feladat <-----------------')
print('10.A osztályos diákok')
for diak in diakok:
    if diak['osztaly'] == '10.A':
        print(diak['vezeteknev'] + ' ' + diak['keresztnev'])

"""    
2. feladat: 
10.B osztályoa tanulók kigyűjtése litába
"""
print('\n------------------> 2. feladat <-----------------')
print('10.B osztályos diákok listában')

osztaly_10B = [diak for diak in diakok if diak['osztaly'] == '10.B']
print(osztaly_10B)


"""    
3. feladat: 
A diákok átlag életkora
"""
print('\n------------------> 3. feladat <-----------------')
osszeg = 0
for diak in diakok:
    osszeg += diak['kor']
atlag = osszeg / len(diakok)
print(f"A diákok átlagéletkora: {atlag:.2f}")


"""    
4. feladat: 
A legidősebb diák neve és kora
"""
print('\n------------------> 4. feladat <-----------------')
max_index = 0
max_kor = diakok[0]['kor']
for index, diak in enumerate(diakok):
    if diak['kor'] > max_kor:
        max_kor = diak['kor']
        max_index = index
print(f"A legidősebb diák életkora: {max_kor}, neve: {diakok[max_index]['vezeteknev']} {diakok[max_index]['keresztnev']}")

