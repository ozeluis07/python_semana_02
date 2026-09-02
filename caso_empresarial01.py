## La pulpería La Esquina necesita reponer un producto cuando quedan menos de 5 unidades. Solicita el nombre y la existencia; muestra una alerta cuando corresponda.
import os

def inventarioPulperia():
    os.system("cls")

    print("=======Bienvenidos ala pulperia de la esquina=======")

    nombre_productos = input("Ingrese el nombre del producto: ")

    existencia = int(input("Ingrese la existencia del producto: "))
    print("*******************************************************************************************")

    if existencia < 5:

        print(" El producto ", nombre_productos, " tiene muy poca existencia, solo quedan ", existencia, "se tendra que reponer pronto")

    else:

        print(" El producto ", nombre_productos, " tiene buena existencia, quedan ", existencia)


if __name__ == "__main__":
    inventarioPulperia()
    print("gracias, vuelva pronto")