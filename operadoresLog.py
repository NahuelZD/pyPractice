# Operadores lógicos Or y And
# And
print('AND')
print('True and True => ', True and True)
print('True and False => ', True and False)
print('False and True => ', False and True)
print('False and False => ', False and False)
# Sólo da True si ambos son True

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = int(input('Ingrese el número de stock: '))
print(stock >= 100 and stock <= 1000)

print('*' * 60)

# OR
print('OR')
print('True or True => ', True or True)
print('True or False => ', True or False)
print('False or True => ', False or True)
print('False or False => ', False or False)
# Da True si por lo menos uno de los dos es True

role = input('Digita el rol: ')
print(role == 'admin' or role == 'seller')

# NOT
print('NOT')
print('True not:', False)
print('False not: ', True)

print('NOT AND')
print('NOT (True and True) => ', not (True and True))
print('NOT (True and False) => ', not (True and False))
print('NOT (False and True) => ', not (False and True))
print('NOT (False and False) => ', not (False and False))

print('NOT OR')
print('NOT (True or True) => ', not (True or True))
print('NOT (True or False) => ', not (True or False))
print('NOT (False or True) => ', not (False or True))
print('NOT (False or False) => ', not (False or False))