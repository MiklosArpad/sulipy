
# lista a listában - kétdimenziós liták

pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]

homersekletek = []

homersekletek.append(pentek)
homersekletek.append(szombat)
homersekletek.append(vasarnap)
homersekletek.append(hetfo)

for nap in homersekletek:
    print(nap)

print(homersekletek[0][2])

for na in  homersekletek:
    for meres in nap:
        print(meres)
    print('-----')

homersekletek.insert(1, [11, 11, 11])
print(homersekletek)

del  homersekletek[1][0]
print(homersekletek)

x = homersekletek[1].pop(1)
print(homersekletek)
print(x)