import os 
##Un emprendimiento fija una meta diaria de C$4,000. Lee el total vendido e informa si se alcanzó; muestra cuánto faltó o cuánto se superó.
def metafija():
    os.system("cls")
    print("=======Bienvenidos al emprendimiento=======")
    meta = 4000
    total_vendido = float(input("ingrese el total vendido: "))
    if total_vendido >= meta:
        supero = total_vendido - meta
        print("la meta diaria fue superada por:", supero)
    else:
        faltante = meta - total_vendido
        print("la meta diaria no fue alcanzada, faltaron:", faltante)

if __name__ == "__main__":
    metafija()
    print("gracias, vuelva pronto")