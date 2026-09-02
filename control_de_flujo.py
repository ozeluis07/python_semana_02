compra = float(input("Ingrese el valor de la compra: "))

if compra >= 1500:
    descuento = 0.10
elif compra >= 500:
    descuento = 0.05
else:
    descuento = 0

descuento= compra-compra * descuento
print("El valor de la compra con descuento es:", descuento)