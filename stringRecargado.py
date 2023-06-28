text = 'Ella sabe programar en Python'
textDos = 'este es otro texto'
mayus = 'HOLA CAPO'

# Buscar si la palabra está dentro del texto.
print('Javascript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste Python')
else:
    print('Elegiste JS')
    
# Contar caracteres en el texto
size = len(text)
print(size)

# Métodos
# Todo a mayúsculas
print(text.upper())

# Todo en minúsculas
print(mayus.lower())

# Contar caracteres
print(text.count('a'))

# Cambiar caracteres de mayuscula a minuscula y al contrario
print(text.swapcase())

# Si un texto inicia con algo en especifico
print(text.startswith('Ella'))

# Si un texto termina con algo en espeficico
print(text.endswith('Roll'))

# Reemplazar palabra o letra
print(text.replace('Python', 'JS'))

# Primer caracter en mayuscula
print(textDos.capitalize())

# Inicio de cada palabra en mayuscula
print(textDos.title())

# Texto es un dígito
print(textDos.isdigit())

textDos = '3665'

print(textDos.isdigit())