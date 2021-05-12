
#  - minden elem csak egyszer fordulhat elő
#  - rendezetlen
#  - többféle típust tárolhat, akár egyszerre is
#  - az elemket nem lehet megváltoztatni
#  - unio, metszet, különbség

reggeli = {'vaj', 'tea', 'kifli'}
ebed = set()
ebed = set(['pecsenye', 'krumpli', True])

print(type(ebed))
print(ebed)

ebed.remove('krumpli')
ebed.add('tea')
print(ebed)

print(reggeli & ebed)  # két halmaz metszete
print(reggeli | ebed)  # ez it az unio
print(reggeli - ebed)  # két halmaz különbsége
print(reggeli ^ ebed)  # csak az egyik vagy másik halmaz eleme

gyumolcskosar = ['eper', 'szeger', 'alma', 'körte', 'szeder', 'eper', 'ribizli', 'körte']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)