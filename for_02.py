def recepcion_cafe():
    # CASO EMPRESARIAL 02: Recepción de café
    peso_total = 0

    print("=== REGISTRO DE RECEPCIÓN DE CAFÉ ===")
    for saco in range(1, 6):
        peso = float(input(f"Saco N° {saco} - Ingrese el peso (kg): "))
        peso_total += peso

    print("\n--- RESUMEN DE RECEPCIÓN ---")
    print(f"Peso total de los 5 sacos recibidos: {peso_total:.2f} kg")

if __name__ == "__main__":
    recepcion_cafe()