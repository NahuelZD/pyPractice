# Piedra papel o tijera muy básico
import random
opciones = ('piedra', 'papel', 'tijera')

rounds = 1
stats = [0, 0, 0]
history = []

count = int(input('Cantidad de rounds -> '))

while count >= rounds:
    
    print('*' * 10)
    print('* ROUND ',rounds)
    print('*' * 10)
    
    userOption = input('piedra, papel o tijeras: ').lower()
    npcOption = random.choice(opciones)

    print('NPC -> ', npcOption)
    print('Tú elección -> ', userOption)

    if not userOption in opciones:
        print('Esa opción no es válida, pescao!')
        rounds -= 1
    elif(userOption == npcOption):
        print('Empate')
        stats[2] += 1
        history.append('Empate')
    elif(userOption == 'papel'):
        if(npcOption == 'piedra'):
            print('Ganaste: Papel gana a piedra')
            stats[0] += 1
            history.append('Usuario')
        else:
            print('Perdiste: Tijera gana a papel')
            stats[1] += 1
            history.append('CPU')
    elif(userOption == 'tijera'):
        if(npcOption == 'piedra'):
            print('Perdiste: Piedra gana a tijera')
            stats[1] += 1
            history.append('CPU')
        else:
            print('Ganaste: Tijera gana a papel')
            stats[0] += 1
            history.append('Usuario')
    else:
        if(npcOption == 'papel'):
            print('Perdiste: Papel gana a piedra')
            stats[1] += 1
            history.append('CPU')
        else:
            print('Ganaste: Piedra gana a tijera')
            stats[0] += 1
            history.append('Usuario')
    
    rounds += 1

print('*' * 20)
print('Cantidad de veces que ganaste -> ',stats[0])
print('Cantidad de veces que ganó el CPU -> ', stats[1])
print('Cantidad de empates -> ', stats[2])
print('Historial -> ',history)