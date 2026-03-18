ingreso = float(input("Ingrese ingreso mensual: "))
renta = float(input("Ingrese renta: "))
comida = float(input("Ingrese comida: "))
transporte = float(input("Ingrese transporte: "))

gastos = renta + comida + transporte
restante = ingreso - gastos

print("\n--- RESULTADOS ---")
print(f"Gastos totales: ${gastos}")
print(f"Dinero restante: ${restante}")
