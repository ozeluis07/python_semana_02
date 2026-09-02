import os
## Una tienda de Masaya aplica una promoción simulada de 10% cuando la compra supera C$1,500. Solicita el monto y muestra el total.
def tiendamasaya ():
    os.system("cls")
    print("=======Bienvenidos a la tienda Masaya=======")
    monto = float(input("ingrese el monto de la compra: "))
    if monto >= 1500:
        descuento= monto * 0.10
        total= monto - descuento
        print("el monto de la compra con el descuento aplicado es de :", total)
    else:
        print("el monto de la compra no aplica para el descuento")
        print("el monto de la compra es de :", monto)

if __name__ == "__main__":
    tiendamasaya()
    print("gracias, vuelva pronto")

