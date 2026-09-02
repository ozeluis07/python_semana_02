import os 


def main():
    ## limpiar consola 
    os.system("cls")

    ##varialble de asignatura de tipo str
    nombre_asingnatura = input("digite el nombre de la signatura:")

    ## variable de tipo activa es de tipo bool 
    activa_Asignatura= input("la asifgnatura esta activa (True/False):").strip().lower()
    activa = activa_Asignatura in ["true", "1", "t", "y", "yes" , "si", "s"]
    ## la variable nota 
    nota=float(input("digite la nota obtenidad:"))

    ## la variable de tipo credito
    credito=int(input("digite el numero de creditos "))

    print("=================================================================")

    ## vamos a imprimir el nombre de las variables asignatura
    print("el nombre de la asignatura es:", nombre_asingnatura)
    print("la asignatura esta activa:", activa_Asignatura )
    print("la nota obtenida es:", nota)
    print("el numero de creditos es:", credito)

    print("=================================================================")

    

main()


