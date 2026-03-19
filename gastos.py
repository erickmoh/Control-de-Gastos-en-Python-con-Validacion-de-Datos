def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def calcular_gastos(renta, comida, transporte):
    return renta + comida + transporte


def mostrar_resultados(ingreso, gastos):
    restante = ingreso - gastos
    print("\n--- RESULTADOS ---")
    print(f"Ingreso mensual: ${ingreso:.2f}")
    print(f"Gastos totales: ${gastos:.2f}")
    print(f"Dinero restante: ${restante:.2f}")

    if restante < 0:
        print("⚠️ Estás en déficit. Reduce gastos.")
    elif restante < ingreso * 0.2:
        print("⚠️ Poco ahorro. Considera ajustar gastos.")
    else:
        print("✅ Buen manejo financiero.")


def main():
    print("=== CONTROL DE GASTOS ===")

    ingreso = pedir_numero("Ingrese ingreso mensual: ")
    renta = pedir_numero("Ingrese gasto en renta: ")
    comida = pedir_numero("Ingrese gasto en comida: ")
    transporte = pedir_numero("Ingrese gasto en transporte: ")

    gastos = calcular_gastos(renta, comida, transporte)
    mostrar_resultados(ingreso, gastos)


if __name__ == "__main__":
    main()
