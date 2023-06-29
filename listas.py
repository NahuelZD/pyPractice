numeros = [1, 2, 3, 4]
print(numeros)
print(type(numeros))

tareas = ['Lavar platos', 'Jugar videojuegos']
print(tareas)

tipos = [1, True, 'hola']
print(tipos)

print(numeros[0])
print(tareas[0])
texto = 'Hola' # No se puede hacer texto[0]

# Cambiar algo dentro de una lista
tareas[0] = 'Hacer la comida'
print(tareas)

# Slicing
print(numeros[:3])

# Buscar elementos en la lista
print(True in tipos)
print(1 in numeros)