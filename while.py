''' While
while True:
    print('Se ejecuta')
'''

'''
count = 0

while count < 10:
    count += 1
    print(count)
'''
'''
count = 0

while count < 20:
    count +=1
    if count == 15:
        break # Rompemos el flujo de manera forzada
    print(count)
'''

count = 0

while count < 20:
    count +=1
    if count < 15:
        continue
    print(count)