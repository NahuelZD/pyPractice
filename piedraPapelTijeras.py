# Piedra papel o tijera muy básico
userOption = input('piedra, papel o tijeras: ')
npcOption = input('NPC: ')

if(userOption == npcOption):
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