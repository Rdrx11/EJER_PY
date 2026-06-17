pacientes={
    1:{"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
    "temperatura":34.6, "grave": False},
    2:{"nombre": " Enrique Perez", "prevision": "Isapre", 
    "temperatura":37.6, "grave": False},
    3:{"nombre": " Gabriel Aguilar", "prevision": "Fonasa", 
    "temperatura":35.3, "grave": False}
    }

def ValidarEstado(temperatura):

    if temperatura>39:
        return True
    else:
        return False


def descuento():
    atencion=25000
    fonasa=0.54
    Isapre=0.24
    fodesa=0.125
    if pacientes==fonasa:
        Descuento=atencion*54/100
        print(f"el precio final tras el descuento es: {Descuento}")
    elif pacientes==Isapre:
        Descuento=atencion*24/100
        print(f"el precio final tras el descuento es: {Descuento}")
    elif pacientes==fodesa:
        Descuento=atencion*12.5/100
        print(f"el precio final tras el descuento es: {Descuento}")

def AgregarPacientes():
    nombreP=input("Ingrese el nombre del paciente: ")
    Prevision=input("Ingrese la prevision del paciente: ")
    temperatura=float(input("Ingrese la Temperatura: "))
    pacientes[list(pacientes.keys())[-1]+1]={"nombre": nombreP, "previcion": Prevision,
                "temperatura": temperatura}

def menu():
    while True:
        print("-"*30)
        print("---Menu Principal---")
        print("1.- Agregar Pacientes")
        print("2.- Eleminar Pacientes")
        print("3.- Mostrar Pacientes")
        print("4.- descuentos que deben aplicarse")
        print("5.- Salir")
        print("-"*30)
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                AgregarPacientes()
            case 2:
                Nombrepa=("Que paciente desea eleminar?: ")
                pacientes.pop
            case 3:
                print("")
                pacienteTEMP=int(input("A que paciente le tomamos la temperatura?: "))
                tomarTemp=float(input("Ingrese la nueva temperatura: "))
                pacientes[pacienteTEMP-1]["temperatura"]=tomarTemp
                pacientes[pacienteTEMP-1]["grave"]=ValidarEstado(tomarTemp)
                
            case 4:
                # descuento()
                pa=int(input("que paciente va a pagar?: "))
                if pacientes[pa-1]["prevision"].lower()=="Fonasa":
                    pagar=25000*0.46
                elif pacientes[pa-1]["prevision"].lower()=="Isapre":
                    pagar=25000*0.73
                elif pacientes[pa-1]["prevision"].lower()=="Fodesa":
                    pagar=25000*0.875
                else:
                    print("prevision incorrecta")
                print("Su total a paragar es: ", pagar)
            case 5:
                print ("salir")
                break
            case _:
                print("OPCION INVALIDA")
menu()