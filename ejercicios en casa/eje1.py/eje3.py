pacientes={
    1:{"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
    "temperatura":34.6, "grave": False},
    2:{"nombre": " Enrique Perez", "prevision": "Isapre", 
    "temperatura":37.6, "grave": False},
    3:{"nombre": " Gabriel Aguilar", "prevision": "Fodesa", 
    "temperatura":35.3, "grave": False}
    }

def ValidarEstado(temperatura):

    if temperatura>39:
        return True
    else:
        return False


def descuento():
    total=0
    mostrarPacientes()
    cobrar = int(input("¿A que paciente le va a cobrar?: "))
    prevision = pacientes[cobrar]["prevision"]
    if cobrar not in pacientes:
        print("Paciente no encontrado.")
    if prevision.lower() == "fonasa":
        total = 25000 * 0.46
    if prevision.lower() == "isapre":
        total = 25000 * 0.73
    if prevision.lower() == "fodesa":
        total = 25000 * 0.875
    else:
        print("Prevision invalida")
    return total

def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        print("\n--- Lista de Pacientes ---")
        for p in pacientes:
            print(f"{p} .- {pacientes[p]['nombre']} ({pacientes[p]['prevision']})")

def AgregarPacientes():
    nombreP=input("Ingrese el nombre del paciente:  ")
    Prevision=input("Ingrese la prevision del paciente: ")
    temperatura=float(input("Ingrese la Temperatura: "))
    pacientes[list(pacientes.keys())[-1]+1]={"nombre": nombreP, "prevision": Prevision, 
                                             "temperatura": temperatura}
    nueva_llave = list(pacientes.keys())[-1] if pacientes else 1
    pacientes[nueva_llave] = {
        "nombre": nombreP, 
        "prevision": Prevision,
        "temperatura": temperatura,
        "grave": ValidarEstado(temperatura)
    }
    print("Paciente agregado con éxito.")

def eleminarPaciente():
    mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci)
    print("Paciente eliminado")

def tomarTemperatura():
    mostrarPacientes()
    paciente=int(input("Qué paciente le tomará la temperatura?: "))
    temperatura=float(input("Ingrese la temperatura del paciente: "))
    pacientes[paciente-1]["temperatura"]=temperatura
    pacientes[paciente-1]["grave"]=ValidarEstado(temperatura)
    print("Temperatura y estado actualizado")

def menu():
    while True:
        print("-"*30)
        print("---Menu Principal---")
        print("1.- Agregar Pacientes")
        print("2.- Eleminar Pacientes")
        print("3.- Tomar temperatura")
        print("4.- cobrar por la atencion")
        print("5.- Salir")
        print("-"*30)
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                AgregarPacientes()
            case 2:
                eleminarPaciente()
            case 3:
                tomarTemperatura()
            case 4:
                print(f"El total a pagar es: {descuento()}")
            case 5:
                print ("salir")
                break
            case 8:
                mostrarPacientes()
            case _:
                print("OPCION INVALIDA")
            
menu()