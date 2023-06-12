import os 
import numpy as np


casillero = np.zeros((3,5), dtype=int)
venta_super = 0
venta_grande = 0
venta_pequeña = 0
dinero_ventas= 0
numero_ventas= venta_super + venta_grande + venta_pequeña

menu = 1
def compra_casillero(tamaño):
    os.system('cls')
    if tamaño == 1:
        print ("El precio seria $2000, ingrese su rut sin numero verificador:")
        rut = int(input())
        print ("Selecione el casillero que desea (Solo se pueden elegir los que tengan '0')")
        print ("Para elegir seleccione un numero del 1 al 5")
        print (casillero[0,0], casillero[0,1],casillero[0,2], casillero[0,3],casillero[0,4])
        lugar = int(input()) - 1
        if lugar >=0 and lugar <=4:

            if casillero[0,lugar] == 0:
                casillero[0,lugar]= rut
                print ("Se registro el arriendo, presione enter para continuar")
                input()
                return 1
            else:
                print ("El casillero ingresado esta ocupado vuelva a intentarlo")
        else:
            print("El numero ingresado no es valido, vuelva a intentarlo")
            input("Presione enter para continuar")

    elif tamaño ==2:
        print ("El precio seria $1000, ingrese su rut sin numero verificador:")
        rut = int(input())
        print ("Selecione el casillero que desea (Solo se pueden elegir los que tengan '0')")
        print ("Para elegir seleccione un numero del 1 al 5")
        print (casillero[1,0], casillero[1,1],casillero[1,2], casillero[1,3],casillero[1,4])
        lugar = int(input()) - 1
        if lugar >= 0 and lugar <=4:
            if casillero[1,lugar]== 0:
                casillero[1,lugar] = rut
                print ("Se registro el arriendo, presione enter para continuar")
                input()
                return 1
            else: 
                print ("El casillero ingresado esta ocupado vuelva a intentarlo")
        else:
            print("El numero ingresado no es valido, vuelva a intentarlo")
            input("Presione enter para continuar")

    
    elif tamaño==3:
        print ("El precio seria $500, ingrese su rut sin numero verificador:")
        rut = int(input())
        print ("Selecione el casillero que desea (Solo se pueden elegir los que tengan '0')")
        print ("Para elegir seleccione un numero del 1 al 5")
        print (casillero[2,0], casillero[2,1],casillero[2,2], casillero[2,3],casillero[2,4])
        lugar = int(input()) - 1
        if lugar >= 0 and lugar <=4:
            if casillero [2,lugar]==0:
                casillero[2,lugar]= rut
                print ("Se registro el arriendo, presione enter para continuar")
                input()
                return 1
            else:
                print ("El casillero ingresado esta ocupado vuelva a intentarlo")
        else:
            print("El numero ingresado no es valido, vuelva a intentarlo")
            input("Presione enter para continuar")


    else:
        print ("El numero seleccionado no es valido vuelva a intentarlo")

def desocupar_casillero(rut):
    os.system('cls')
    for i in range(3):
            for j in range(5):
                if casillero[i,j] == rut:
                    print ("El casillero ha sido desocupado con exito")
                    casillero [i,j] = 0


while menu == 1:
    os.system('cls')
    print ("Arriendo de casilleros")
    print ("(1) Registro de Arriendo")
    print ("(2) Listar casilleros")
    print ("(3) Totalizar las ventas hasta el momento")
    print ("(4) Desocupar un casillero")

    print ("Ingrese una opcion")
    opcion = (int(input()))
    os.system('cls')
    if opcion == 1:
        print ("¿Que tipo de casillero desea?")
        print ("(1) Super Grande")
        print ("(2) Grande")
        print ("(3) Pequeño")
        tamaño = int(input())
        if tamaño >=1 and tamaño <=3:
            compra= compra_casillero(tamaño)
            if compra ==1:
                if tamaño == 1:
                    venta_super = venta_super +1
                    dinero_ventas = dinero_ventas +2000
                elif tamaño == 2:
                    venta_grande = venta_grande + 1
                    dinero_ventas = dinero_ventas +1000
                elif tamaño == 3:
                    venta_pequeña = venta_pequeña +1
                    dinero_ventas = dinero_ventas +500
        else:
            print("El numero ingresado no es valido, vuelva a intentarlo")
            print ("Presione enter para continuar")
            input()

    elif opcion ==2:
        print ("Lista de casilleros")
        print ("Casillero super grandes:", casillero[0,0], casillero[0,1],casillero[0,2], casillero[0,3],casillero[0,4])
        print ("Casillero grandes:", casillero[1,0], casillero[1,1],casillero[1,2], casillero[1,3],casillero[1,4])
        print ("Casilleros pequeños:", casillero[2,0], casillero[2,1],casillero[2,2], casillero[2,3],casillero[2,4])
        print ("Presione enter para continuar")
        input()
    elif opcion ==3:
        print ("Las ventas hasta el momento han sido: ")
        print ("Numero de ventas de casilleros super grandes:", venta_super)
        print ("Numero de ventas de casilleros grandes:", venta_grande)
        print ("Numero de ventas de casilleros pequeñas:", venta_pequeña)
        print ("Numero de ventas de casilleros totales: ", numero_ventas)
        print ("Dinero hecho con ventas:", dinero_ventas)
        input()            
    elif opcion ==4:
        print ("Ingrese su rut sin guion para desocupar su casillero")
        print ("El rut debe ser el mismo que ingreso a la hora de registrar casillero")
        rut = int(input())
        desocupar_casillero(rut)
        print ("Presione enter para continuar")
        input()
    else:
        print("El numero ingresado no es valido, vuelva a intentarlo")
        print ("Presione enter para continuar")
        input()



