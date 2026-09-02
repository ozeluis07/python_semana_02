import os 
## Una cooperativa primero verifica si la humedad está entre 10% y 12%. Si cumple, clasifica el lote según los defectos reportados. Propón categorías claras
def cafe():
    os.system("cls")
    humedad=float(input("ingrese la humedad reportada porfavor:"))

    if  10< humedad <13 :
        valor=input("ingrese como observa el lote (bueno)(malo):")
        if valor=="bueno":
            print("el porcentaje de humedad % :",humedad)
            print("con un estado de calidad:",valor)
        else:
            print("el porcentaje de humedad % :",humedad)
            print("con un estado de calidad:",valor)
    else: 
        print("el programa nose podra usar ya que los indices de huemedad no son los requerido %:",humedad)

if __name__ == "__main__":
    cafe()

