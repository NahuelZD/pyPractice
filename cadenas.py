# Strings
name = "Nahuel"
lastName = "Zelaya"

print(name)
print(lastName)

fullName = name + " " + lastName

print(fullName)

# Frase
quote = "I'm Nahuel." # Comillas dobles para poner simples adentro
print(quote)

quote2 = 'She said "Hello".' # Comillas simples para poner dobles adentro
print(quote2)

# Format
template = "Hola, mi nombre es " + name + " y mi apellido es " + lastName
print(template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastName)
print(template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {lastName}"
print(template3)
