# Diccionario (key - value)
miDiccionario = {}
print(miDiccionario)

miDiccionario = {
    'avion': "blablabla",
    'name': "Nahuel",
    'surname': "Zelaya",
    'anios': 30
}
print(miDiccionario)

# Elementos dentro del dicci
print(len(miDiccionario))

# Leer dicci
print(miDiccionario['name'])
print(miDiccionario['anios'])
print(miDiccionario.get('anio')) # Si no existe, devuelve 'none'.. Del otro modo da error
print('avion' in miDiccionario)
print('avios' in miDiccionario)

# ------------- Eliminar y añadir elementos ------------------

person = {
    'name': "Nahuel",
    'surname': "Zelaya",
    'langs': ['python', 'JS'],
    'age': 30
}

print(person)

person['name'] = 'Francisco'
print(person)

person['age'] -= 12
print(person)

person['langs'].append('rust')
print(person)

# Eliminar
del person['surname']
print(person)

person.pop('age') # En diccionario si o si se pone argumento en pop()
print(person)

# Obtener items del dicci
print(person.items())
print(person.keys())
print(person.values())