import os

from caso_empresarial01 import inventarioPulperia
from caso_empresarial02 import tiendamasaya
from caso_empresarial03 import metafija
from caso_empresarial04 import comedor
from caso_empresarial05 import bodega
from aninodado_01 import pulperia_credito
from aninodado_02 import emprendimiento
from aninodado_03 import cafe
from aninodado_04 import hospedaje_granada
from aninodados_05 import minorista_mayoristas
from for_01 import promedi_semanal
from for_02 import recepcion_cafe
from for_03 import revision_iventario
from for04 import combustible_reparto
from for_05 import evaluacion_de_revision
from while_01 import cierre_de_caja
from while_02 import acceso_sistema
from while_03 import cantidad_de_pedido
from while_04 import combustible_de_reparto
from while_05 import reposicion_existencias

def principal():
    os.system("cls")
    opc=0
    while opc != 21:
        print("***************menu*************")
        print("1-inventario de pulperia")
        print("2-promocion de tienda")
        print("3-meta fija")
        print("4-comedor")
        print("5-inventario de bodega")
        print("6-pulperia credito")
        print("7-empredimiento")
        print("8-cafe")
        print("9-hospedaje granada")
        print("10-mayorista y minorista")
        print("11-promedio semanal")
        print("12-recepcion de cafe")
        print("13-revision de inventario")
        print("14-reparto de combustible")
        print("15-evaluacion de revision")
        print("16-cierre de caja")
        print("17-acceso de sistema")
        print("18-cantidad de pedido")
        print("19-combustible de reparto")
        print("20-reporcicion de existencias")
        print("21-terminar")
        print("-"*39)
        try:
            opc=int(input("seleciones una opcion:"))
        except ValueError:
            print("debe ingresar un numero")
            continue
        print("-"*39)

        match opc:
            case 1:
                inventarioPulperia()
            case 2:
                tiendamasaya()
            case 3:
                metafija()
            case 4:
                comedor()
            case 5:
                bodega()
            case 6:
                pulperia_credito()
            case 7:
                emprendimiento()
            case 8:
                cafe()
            case 9: 
                hospedaje_granada()
            case 10:
                minorista_mayoristas()
            case 11:
                promedi_semanal()
            case 12:
                recepcion_cafe()
            case 13:
                revision_iventario()
            case 14:
                combustible_reparto()
            case 15:
                evaluacion_de_revision()
            case 16:
                cierre_de_caja()
            case 17:
                acceso_sistema()
            case 18:
                cantidad_de_pedido()
            case 19:
                combustible_de_reparto()
            case 20:
                reposicion_existencias()
            case 21:
                print("gracias por usara el menu")
            case _:
                print("opcion incorrecta")

    os.system("pause")

principal()