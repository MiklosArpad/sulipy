
diak = {
    'vezeteknev' : 'Kiss',
    'keresznev' : 'Péter',
    'osztaly' : '10.A',
    'eletkor' : 17,
    'kollegista' : True,
    'info_fakt' : False,
    'matek_jegyek0' : [5, 4, 4, 3, 5, 5]
}

print(diak['eletkor'])
print(diak.get('eletkor'))

print(diak.get('szakkor', 'nincs adat'))

# ha le akarom ellenőrizni, hogy a lekérdezésem tárgya létezik-e, akkor az alábbi verzióval tudok kérni
# ha nincs ilyen akkor false-ot ad.

print('szakkor' in diak)

# utólag is létrehozhatok egy elemet

diak['szakkor'] = True
print(diak)

# felülírása egy elem értékének

diak['eletkor'] = 20
print(diak)

for kulcs in diak:
    print(kulcs, diak[kulcs])

print(diak.values())
for ertek in diak.values():
    print(ertek)

print(diak.items())
for kulcs, ertek in diak.items():
    print(kulcs, ertek)

