def cierre_de_caja ():

    # CASO EMPRESARIAL 01: Cierre de caja
    total_recaudado = 0
    cantidad_ventas = 0

    print("=== CIERRE DE CAJA ===")
    monto = float(input("Ingrese el monto de la venta (o 0 para terminar): "))

    # Mientras el monto no sea 0, seguimos sumando
    while monto != 0:
        total_recaudado += monto
        cantidad_ventas += 1
        monto = float(input("Ingrese el monto de la venta (o 0 para terminar): "))

    print("\n--- RESUMEN DE CAJA ---")
    print(f"Total recaudado: ${total_recaudado:.2f}")
    print(f"Cantidad de ventas realizadas: {cantidad_ventas}")

if __name__ == "__main__":
    cierre_de_caja()
