import os 
## Un emprendimiento calcula una tarifa simulada según zona urbana o rural y, dentro de cada zona, según si el paquete supera 5 kg. Propón tarifas y calcula el total.

def emprendimiento():
    os.system("cls")
    paquete_peso=float(input("ingrese el peso del paquete:"))
    zona=input("elija su zona (rural)o(urbana)")
    rural=10
    urbana=5

    if zona=="rural":
        if paquete_peso >5 :
            tarifa=paquete_peso*rural
            print("precio total para el envio a zona rural es de:C$",tarifa)
        else:
            print("el envio nose se puede hacer por falta de peso")
    else:
        if paquete_peso >5 :
            tarifa=paquete_peso*urbana
            print("precio total para el envio a zona urbana es de:C$",tarifa)
        else:
            print("el envio nose se puede hacer por falta de peso")

if __name__ == "__main__":
    emprendimiento()

    


