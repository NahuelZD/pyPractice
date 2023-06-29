numeros = (1, 2, 3, 5)
strings = ('Nico', 'Nahuel', 'José', 'Nahuel')

print(numeros)
print('Elemento en la posición 0 -> ', numeros[0])
print('Elemento en la última posición -> ', numeros[-1])
print(type(numeros))

print(strings)
print(type(strings))

# Las tuplas no pueden ser modificadas. Si quiero hacer un append, no puedo hacerlo. Ni hacer numeros[0] = 0
# Las tuplas son sólo de lecturas

# Posición de elementos
print(strings.index('Nahuel'))

# Contar cuantos elementos hay en la tupla
print(strings.count('Nahuel'))

# Transformaciones - Transformar a lista y modificar
miLista = list(strings)

print(miLista)
print(type(miLista))

miLista[1] = 'Meli'

miTupla = tuple(miLista)

print(miTupla)
print(type(miTupla))