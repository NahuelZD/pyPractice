# Piedra papel o tijera muy básico
import random
opciones = ('piedra', 'papel', 'tijera')

userOption = input('piedra, papel o tijeras: ').lower()
npcOption = random.choice(opciones)

print('NPC -> ', npcOption)
print('Tú elección -> ', userOption)

if not userOption in opciones:
    print('Esa opción no es válida, pescao!')
elif(userOption == npcOption):
    print('Empate')
elif(userOption == 'papel'):
    if(npcOption == 'piedra'):
        print('Ganaste: Papel gana a piedra')
    else:
        print('Perdiste: Tijera gana a papel')
elif(userOption == 'tijera'):
    if(npcOption == 'piedra'):
        print('Perdiste: Piedra gana a tijera')
    else:
        print('Ganaste: Tijera gana a papel')
else:
    if(npcOption == 'papel'):
        print('Perdiste: Papel gana a piedra')
    else:
        print('Ganaste: Piedra gana a tijera')