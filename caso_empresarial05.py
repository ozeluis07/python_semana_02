import os 
##Una bodega espera sacos de 46 kg. Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.
def bodega():
    peso = float(input("digite el peso del saco: "))
    if peso == 46:
        print("el saco cumple con el peso esperado")
    elif peso < 46:
        print("el saco debe revisarse por estar debajo del valor esperado")
    else:
        print("el saco cumple con el peso esperado")

if __name__ == "__main__":
    bodega()
    print("gracias por su visita")
