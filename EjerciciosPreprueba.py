# crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada cada piso tiene 10 espacios
# preguntar cuando entra im vehiculo, que tipo de vehiculos es
# vehiculo ligero 2000
# vehiculo mediano 3000
# vehiculo pesado 3500

# luego, acomodarlo en algun lugar de algun piso disponible
# el menu desde tener las siguientes alternativas

#1.- ingresar vehiculo
#2.- contar ganancias 
#3.- contar vehiculos
#4.- ganancias promedio

# usa lista o diccionario segun lo que te acomode mas

import random

Parking={
    1: [],
    2: [],
    3: [],
    4: [],
}
TipoVehiculo={
    1:{"tipo":"ligero", "precio: ": 2000},
    2:{"tipo": "mediano", "precio": 3000},
    3:{"tipo": "pesado", "precio": 3500}
}

def agregarVehiculo():
    print("")
def mostrarGanancias():
    print("")



def menu():
    while True:
        print ("----Gestor de Estacionamiento----")
        print ("1.- ingresar vehiculo")
        print ("2.- contar ganancias ")
        print ("3.- contar vehiculos")
        print ("4.- ganancias promedio")
        print ("5.- salir")
        op=int(input("ingrese una de las opciones: "))
        match op:
            case 1:

                auto=int(input("Indique tipo de vehiculo: \n1.- ligero\n2.- mediano\n3.-pesado"))
                piso=int(input("enq ue piso quedara?"))
                # piso=random.radint(1,4)
                if len(Parking[piso])<10:
                    if auto==1:
                        Parking[piso].append("ligero")(2000)
                    elif auto==2:
                        Parking[piso].append("mediano")(3000)
                    elif auto==3:
                        Parking[piso].append("pesado")(3500)
                    else:
                        print("vehiculo no valido")
                else:
                    print("piso lleno")
            case 2:
                print("Contar ganancias")
                totalGanancias=0
                for pesos in Parking.values():
                    totalGanancias+=sum(pesos)
                print("el total acumulado actual es", totalGanancias)
            case 3:
                print("")
            case 4:
                print("")
            case 5:
                for piso in Parking.items():
                    print(f"piso {piso} : {espacios}")
                maximo=10
            case _:
                print("opcion IVALIDA")
menu()