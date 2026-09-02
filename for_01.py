import os 
def promedi_semanal():
    os.system("cls")
    print("sistema de venta de promedio semanal")
    ventasdia1=ventadia2=ventadia3=ventadia4=ventadia5=ventadia6=ventadia7=0
    for i in range(1,8):
        for j in range(1,4):
            semana=float(input(f"ingrese lo vendido {j} de hoy {i}:"))
            match i:
                case 1:
                    ventasdia1+=semana
                case 2:
                    ventadia2+=semana
                case 3:
                    ventadia3+=semana
                case 4:
                    ventadia4+=semana
                case 5:
                    ventadia5+=semana
                case 6:
                    ventadia6+=semana
                case 7:
                    ventadia7+=semana

    promedioo = ventasdia1+ventadia2+ventadia3+ventadia4+ventadia5+ventadia6+ventadia7

    print("promedio semanal:",promedioo)
    print("promedio de ventas del dia 1 es C$:",ventasdia1/3)
    print("promedio de ventas del dia 2 es C$:",ventadia2/3)
    print("promedio de ventas del dia 3 es C$:",ventadia3/3)
    print("promedio de ventas del dia 4 es C$:",ventadia4/3)
    print("promedio de ventas del dia 5 es C$:",ventadia5/3)
    print("promedio de ventas del dia 6 es C$:",ventadia6/3)
    print("promedio de ventas del dia 7 es C$:",ventadia7/3)


            


if __name__ == "__main__":
    promedi_semanal()