def inventarioPulperia():
    print("Una pulpería con crédito interno primero verifica si la persona está registrada. Solo entonces revisa su saldo pendiente.")

    registrado = input("el cliente esta registrado (si/no): ").strip().lower()
    if registrado in ["si", "sí"]:
        saldo = float(input("digite el saldo del cliente: "))
        if saldo >= 500:
            print("El cliente puede comprar, su saldo es:", saldo)
        else: 
            print("El cliente no puede comprar, su saldo es:", saldo)
    else:
        print("contado")

inventarioPulperia()

  
