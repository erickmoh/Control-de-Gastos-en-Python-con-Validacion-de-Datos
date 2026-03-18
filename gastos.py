ingreso = float(input("Ingrese ingreso mensual: "))
renta = float(input("Ingrese renta: "))
comida = float(input("Ingrese comida: "))
transporte = float(input("Ingrese transporte: "))

gastos = renta + comida + transporte
restante = ingreso - gastos

print("Gastos totales:", gastos)
print("Dinero restante:", restante)