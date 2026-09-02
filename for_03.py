def revision_iventario ():
        
    # CASO EMPRESARIAL 03: Revisión de inventario
    alertas = 0

    print("=== REVISIÓN DE INVENTARIO (8 PRODUCTOS) ===")
    for i in range(1, 9):
        nombre = input(f"\nProducto {i} - Nombre: ")
        existencia = int(input(f"Producto {i} - Cantidad en existencia: "))
        
        if existencia < 10:
            print(f"⚠️ ¡ALERTA! El producto '{nombre}' tiene bajo stock ({existencia} unidades).")
            alertas += 1

    print("\n--- RESUMEN DE INVENTARIO ---")
    print(f"Total de productos en alerta (menos de 10 unidades): {alertas}")

if __name__ == "__main__":
    revision_iventario()