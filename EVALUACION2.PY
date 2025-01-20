fondoCambio = 40000
opc = 0
auto = 2000
camioneta = 3000
camion = 4000
motocicleta = 890
correo = ""
ingresoMonto = 0
totalPagar = 0
vuelto = 0
totalRecaudado = 0
opc2= 0
codigoAdmin = 3312

while True:
    print("---MENU---")
    print("1)Auto: $2.000 ")
    print("2)Camioneta: $3.000 ")
    print("3)Camion: $4.000")
    print("4)Motocicleta: $890 ")

    try:
        ocp = int(input("ingrese una opcion: "))

    except ValueError:
           ("porfavor vuelva a intentar")
           continue
    
   
    if opc == 1:
            auto
            totalPagar = auto
            print("Monto a pagar: ", totalPagar)

    elif ocp == 2:
            camioneta
            totalPagar =  camioneta
            print("Monto a pagar: ", totalPagar)

    elif ocp == 3:
            camion
            totalPagar =  camion
            print("Monto a pagar: ", totalPagar)

    elif ocp == 4:
            motocicleta
            totalPagar =  motocicleta
            print("Monto a pagar: ", totalPagar)

    
    while True:
        correo = str(input("Ingrese su correo: "))
        if len(correo) <30:
            print("correcto")
        else: 
            print("Ingrese un correo valido, entre 5 y 30 caracteres")

                #for correo in range(@):
                #print
        
        try:
            ingresoMonto = int(input("Ingrese monto: "))
            if ingresoMonto > totalPagar and ingresoMonto == totalPagar:
                print("correcto")
                vuelto = (ingresoMonto - totalPagar)
                fondoCambio += totalPagar
                print(" su vuelto : ",vuelto)
                
            elif ingresoMonto < totalPagar and ingresoMonto > 10000:
                print(" porfavor ingrese el monto correspondiente hasta $10.000")
        except ValueError: 
            print("porfavor vuelva a intentar")
            continue



        print("---BOLETA---")
        print("total pagado: ", totalPagar)
        print("su vuelto: ", vuelto)

        totalRecaudado+= totalPagar


    
        print("1) Volver al menu")
        print("2) Salir")

        try:
            opc2 = int(input(" Ingrese una opcion: "))
            if opc == 2:
                codigoAdmin = int(input("Ingrese el codigo Administrador: "))
                if codigoAdmin == 3312:
                    print("---RESUMEN TOTAL---")
                    print("total dinero recaudado: ",totalRecaudado )
                    print("fondo de cambio: ", fondoCambio)
                    exit()
                
                elif opc != 1:
                        print("opcion no valida")
        except ValueError:
                    print("volviendo al menu")










            






