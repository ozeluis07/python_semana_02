import os

def hospedaje_granada():
    os.system("cls")

    reservacion=input("el cliente tiene reservacion en el hotel:")
    dias_de_reservacion=float(input("cuantos dias se hospedara:"))



    if reservacion == "si":
        if dias_de_reservacion >3:
            
            precio=float(input("el precio por noche en el hotel es de:"))
            precioF= precio*dias_de_reservacion
            total=precio*0.90
            print("gracias por preferirnos como su hospedaje en la ciudad donde la gente come vigoron al media noche(granada) su total seria de :C$",total)
            print("se aplico el %10 de descuento")
        else:
            precio=float(input("el precio por noche en el hotel es de:"))
            print("el total de reservacion es de:C$",precio)
    else :
        print("se podra en el hotel pero con el precio mas elevado")

if __name__ == "__main__":
    hospedaje_granada()


