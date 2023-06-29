text = 'Ella sabe Python'

# Los textos tienen un indicador
print(text[0]) # Muestra el primer caracter
print(text[5]) # Sexta posicion

# Si pongo no existe la posición me larga un error
size = len(text)
print(size) # El resultado es 16 pero la última posición es size - 1, o sea 15
print('Tamaño real del string: ', size)
print('Posición del último caracter del string: ', size - 1)

print(text[-1]) # -1 indica el último caracter del string

# Slicing
# Desda la posición 0 hasta la 5 cortar el string

print(text[0:5]) # Ella
print(text[10:16]) # Python

# Si siempre empieza en cero, podemos obviar el 0
print(text[:10])

# Cortar desde una posición dada hasta el final
print(text[5:])

# Saltos (Inicio y fin y puedo enviarle un tercer valor)
print(text[10:16:1]) # Me da: Python
print(text[10:16:2]) # Me da: Pto

# Ir del inicio al final y saltear de a 2 elementos
print(text[::2])