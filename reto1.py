enero = float(input("Presupuesto de enero: "))
febrero = float(input("Presupuesto de febrero: "))
marzo = float(input("Presupuesto de marzo: "))

template = f"Mi dinero en enero es de: USD {enero}, en febrero es de: USD {febrero} y en marzo es de: USD {marzo}. El promedio es de USD {(enero + febrero + marzo) / 3}"

print(template)