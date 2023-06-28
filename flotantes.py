# Float
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y)

# Strings
y_str = format(y, ".2g") # .2g => Que sólo tenga 2 dígitos como resultado
print('str => ',y_str)
print(y_str == str(x))

#Matemáticas
print('*' * 50)

tolerancia = 0.00001
print(abs(x - y) < tolerancia)

# Redondeo
y = round(y,1)
print(y)

print(x == y)