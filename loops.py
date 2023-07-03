matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Primera lista de la matriz -> ",matriz[0])
print("Primero elemento de la primera lista -> ",matriz[0][0])

for row in matriz:
    print(row)
    for column in row:
        print(column)
    