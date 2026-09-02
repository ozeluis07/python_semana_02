import os
## Un comedor realiza entrega sin recargo desde C$300. Indica si la entrega es gratuita o suma un recargo simulado de C$40.
def comedor():
    os.system("cls")
    print("=======Bienvenidos al comedor=======")
    monto = int(input("ingrese el monto de la compra: "))
    plus= 40 

    if monto >= 300:
        print("la entrega es gratuita felicidades")
        print("el monto de la compra es de :", monto)
    else:
        total= monto + plus
        print("la entrega tiene un recargo de C$40, el monto total es de :", total)

if __name__ == "__main__":
    comedor()
    print("gracias, vuelva pronto")
