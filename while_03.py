def cantidad_de_pedido():
    # CASO EMPRESARIAL 03: Cantidad de un pedido
    precio_por_unidad = 10  # Precio de ejemplo

    print("=== PEDIDO DE UNIDADES ===")
    cantidad = int(input("Ingrese la cantidad deseada (de 1 a 100): "))

    # Repite si está fuera del rango (menor que 1 o mayor que 100)
    while cantidad < 1 or cantidad > 100:
        print("❌ Cantidad no válida. Debe ser entre 1 y 100.")
        cantidad = int(input("Ingrese la cantidad deseada (de 1 a 100): "))

    total = cantidad * precio_por_unidad

    print("\n--- RESUMEN DEL PEDIDO ---")
    print(f"Cantidad aceptada: {cantidad} unidades")
    print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    cantidad_de_pedido()