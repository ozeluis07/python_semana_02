import os 
## Una pulpería vende al crédito solo a clientes registrados. Si lo están, revisa que su saldo pendiente no supere C$500. Diseña los mensajes para todos los casos

def pulperia_credito():
    os.system("cls")
    # Pedimos los datos al usuario
    registrado = input("¿El cliente está registrado? (si/no): ")
    saldo = float(input("¿Cuánto debe actualmente en C$? "))
    # Estructura con IF Anidados
    if registrado == "si":
        if saldo <= 500:
            print("Venta aprobada: Crédito autorizado.")
        else:
            print("Venta denegada: El saldo supera los C$500.")
    else:
        print("Venta denegada: El cliente no está registrado.")
if __name__ == "__main__":
    pulperia_credito()
 

    
