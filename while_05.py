def reposicion_existencias ():
    # CASO EMPRESARIAL 05: Reposición de existencias
    existencias = 3
    meta = 20

    print("=== REPOSICIÓN DE EXISTENCIAS ===")
    print(f"Existencias actuales: {existencias} | Meta: {meta}")

    # Se ejecuta hasta alcanzar o superar la meta de 20
    while existencias < meta:
        reposicion = int(input("Ingrese la cantidad a reponer: "))
        
        # Rechazar cantidades que no sean positivas
        if reposicion <= 0:
            print("❌ Debe ingresar una cantidad positiva (mayor a 0).")
        else:
            existencias += reposicion
            print(f"Existencias actualizadas: {existencias}")

    print(f"\n✅ Meta alcanzada o superada. Total en inventario: {existencias} unidades.")

if __name__ == "__main__":
    reposicion_existencias()