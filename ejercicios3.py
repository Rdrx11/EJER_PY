#PuntosAcumulados
sw = 1
puntos = 100000
while sw==1:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        match op:
            case 1:
                print(f"Tiene un total de {puntos} puntos")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            case 2:
                if puntos==0:
                    print("ya no tiene mas puntos")
                else:
                    print("1.- Gift Card de $10.000, valor de 10.000 puntos")
                    print("2.- Secadora de pelo, valor de: 25.000 puntos")
                    print("3.- Disco duro portátil, valor de: 30.000 puntos")
                    op2=int(input("Seleccione una opción: "))
                    match op2:
                        case 1:
                            if puntos<10000:
                                print("puntos insuficientes")
                            else:
                                puntos = puntos-10000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        case 2:
                            if puntos<25000:
                                print("puntos insuficientes")
                            else:
                                puntos = puntos-25000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        case 3:
                            if puntos<30000:
                                print("puntos insuficientes")
                            else:
                                puntos = puntos-30000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        case _:
                            print("opcion invalida")
            case 3:
                print("saliendo...")
                sw=0
            case _:
                print("opcion invalida")
                print("mondongo")
    except:
        print("Ingreso Erróneo")
