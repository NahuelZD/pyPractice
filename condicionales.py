# Condicionales
if True:
    print('Debería ejecutarse')

if False:
    print('Nunca debe ejecutarse')
    

'''
mascota = input('Qué mascota tenés?')
if mascota == 'perro':
    print('Tenés buen gusto.')
if mascota == 'gato':
    print('Espero tengas suerte.')
'''

stock = int(input('Digite el stock: '))

if (stock >= 100 and stock <= 1000):
    print('El stock es correcto.')
else:
    print('El stock es incorrecto.')
    
mascota = input('Qué mascota tenés? ')
if mascota == 'perro':
    print('Tenés buen gusto.')
elif mascota == 'gato':
    print('Espero tengas suerte.')
else:
    print('No tenes ninguna mascota interesante.')