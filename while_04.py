def combustible_de_reparto ():

    # CASO EMPRESARIAL 04: Combustible de reparto
    combustible = 8.0

    print("=== CONTROL DE COMBUSTIBLE DE REPARTO ===")

    # Se ejecuta mientras quede combustible
    while combustible > 0:
        print(f"\nCombustible disponible: {combustible:.1f} litros")
        consumo = float(input("Litros consumidos en este recorrido: "))
        
        # Evitar restarle más de lo que tiene disponible
        if consumo > combustible:
            print("❌ No puedes consumir más combustible del que te queda.")
        else:
            combustible -= consumo
            
            # Alerta si le queda 1 litro o menos (pero más de 0)
            if 0 < combustible <= 1:
                print("⚠️ ¡ALERTA! Te queda 1 litro o menos de combustible.")

    print("\n🚨 El tanque está completamente vacío. Fin de los recorridos.")

if __name__ == "__main__":
    combustible_de_reparto()
