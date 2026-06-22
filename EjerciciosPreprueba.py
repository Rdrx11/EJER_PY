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

Parking={
    1: [],
    2: [],
    3: [],
    4: [],
}
def agregarVehiculo():
    valor=0
    print("Ingresar vehiculo nuevo")
    tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado: "))
    if tipo==1:
        valor=2000
    elif tipo==2:
        valor=3000
    elif tipo==3:
        valor=3500
    else:
        print("Vehiculo invalido")
    piso=int(input("En que piso va?: "))
    if piso in [1,2,3,4] and valor>0 :
        if len(Parking[piso])<10:
            Parking[piso].append(valor)
            print("Agregado al piso", piso)
        else:
            print("Piso lleno")
    else:
        print("Piso no válido")
def mostrarGanancias():
    totalGanancias=0
    print("Contando Ganancias")
    for piso in Parking.values():
        totalGanancias+=sum(piso)
    print(f"El total recudado es {totalGanancias}")
def cuentAutos():
    totalAutos=0
    for piso in Parking.values():
        totalAutos+=len(piso)
    print("El total de autos en el parking es:", totalAutos)
def muestrAutos():
    for h, t in Parking.items():
        print(h, ".- ", t)
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
                agregarVehiculo()
            case 2:
                mostrarGanancias()
            case 3:
                cuentAutos()
            case 4:
                muestrAutos()
            case 5:
                print("saliendo")
                break
            case _:
                print("opcion IVALIDA")
menu() 