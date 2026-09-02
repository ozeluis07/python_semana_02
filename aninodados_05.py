import os 
## Una ferretería distingue mayoristas y minoristas. Para cada tipo, el descuento depende de un monto mínimo diferente. Propón porcentajes y explica tus reglas.
def minorista_mayoristas():
    os.system("cls")

    nombredelcliente=input("ingrese el nombre del cliente:")
    numerosdeproductos=float(input("cuantos productos desea comprar:"))
    cliente=input("el cliente es mayorista o minorista : ")

    if cliente == "mayorista":
        
        if 12 <= numerosdeproductos <= 24:
            print("ha aplicado al %15 de descuento")
            precioindividual=float(input("los precios de los productos son:C$"))
            cuantosson=float(input("cuantos productos son en total:"))
            total= precioindividual*cuantosson
            oferta= total*0.85
            print("el precio con el descuento incluido es de :C$",oferta)
        elif 25 <= numerosdeproductos <= 36:
             print("ha aplicado al %20 de descuento")
             precioindividual=float(input("los precios de los productos son:C$"))
             cuantosson=float(input("cuantos productos son en total:"))
             total= precioindividual*cuantosson
             oferta= total*0.80
             print("el precio con el descuento incluido es de :C$",oferta)
        elif numerosdeproductos >= 37:
            print("ha aplicado al %25 de descuento")
            precioindividual=float(input("los precios de los productos son:C$"))
            cuantosson=float(input("cuantos productos son en total:"))
            total=precioindividual*cuantosson
            oferta= total*0.75
            print("el precio con el descuento incluido es de :C$",oferta)
        else :
            print("se equivoco posiblemente de menu ")
    else:
        print("Bienvenido al menu minorista")
        mino=float(input("ingrese el precio del producto:"))
        cuanto=float(input("cuantos son:"))
        stotal= mino*cuanto

        print("su total seria : C$",stotal)
    
    print("nombre:", nombredelcliente)

if __name__ == "__main__":
    minorista_mayoristas()

