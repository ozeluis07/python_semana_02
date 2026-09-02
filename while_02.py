def acceso_sistema ():
    # CASO EMPRESARIAL 02: Acceso al sistema
    clave_correcta = "1234"
    intentos = 1

    print("=== INICIO DE SESIÓN ===")
    clave_ingresada = input("Ingrese la clave de acceso: ")

    # Mientras la clave sea incorrecta, pedimos la clave de nuevo
    while clave_ingresada != clave_correcta:
        print("❌ Clave incorrecta. Intente de nuevo.")
        intentos += 1
        clave_ingresada = input("Ingrese la clave de acceso: ")

    print(f"\n¡Acceso concedido! Le tomó {intentos} intento(s).")

if __name__ == "__main__":
    acceso_sistema()