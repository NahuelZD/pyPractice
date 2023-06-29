# CRUD (Creeate, Read, Update, Delete)

numeros = [1, 2, 3, 4, 5]
print(numeros)
print(numeros[1])

numeros[-1] = 10 # Cambia el elemento de la última posición
print(numeros)

# Agregar un elemento al final de la lista
numeros.append(700)
print(numeros)

# Insertar un elemento
numeros.insert(0, 100) # Insertar al inicio de la lista
print(numeros)

numeros.insert(3, 'Change') # Insertar en la posición 3 (0,1,2,-3-,4,5)
print(numeros)

# Insertar lista en otra lista
tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3']
nuevaLista = numeros + tareas
print(nuevaLista)

# Buscar la posición de un elemento
index = nuevaLista.index('Tarea 2')
print(index)
nuevaLista[index] = 'Tarea cambiada'
print(nuevaLista)

# Remover o eliminar elementos de la lista
nuevaLista.remove('Tarea 1')
print(nuevaLista)

# Borra último elemento
nuevaLista.pop()
print(nuevaLista)

# Borrar elemento en particular
nuevaLista.pop(0) # Borra el primer elemento (100)
print(nuevaLista)

# Reverse (Dar vuelta la lista)
nuevaLista.reverse()
print(nuevaLista)

# Ordenar
numeros = [0, 11, 2, 33, 14, 54, 6]
print('Lista original -> ', numeros)
numeros.sort()
print('Lista ordenada -> ', numeros)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

# No se puede ordenar si tiene diferentes tipos de datos -> nuevaLista.sort() No existe