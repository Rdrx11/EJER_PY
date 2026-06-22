habitacios={
    1:[],
    2:[],
    3:[]
}

def registroMascota():
    valor=0
    tipo=int(input("\n1.-Perro\n2.-Gato\n3.-Exotico \nQue animal es?: "))
    match tipo:
        case 1:
            valor+=5000
            print("ha seleccionado perro")
        case 2:
            valor+=4000
            print("ha seleccionado gato")
        case 3:            
            valor+=3000
            print("ha seleccionado animal exotico")     
        case _:
            print("tipo invalido")                   
    piso=int(input("En que habitacion va?: "))        
    if piso in [1,2,3] and valor>0 :
        if len(habitacios[piso])<10:
            habitacios[piso].append(valor)
            print("Agregado a la Habitaciones", piso)
        else:
                print("habitacion llena")
    else:
        print ("habitacion invalida")

def gananciaTotales():
    totalGanancias=0
    print("Contando Ganancias")
    for piso in habitacios.values():
        totalGanancias+=sum(piso)
    print(f"El total recudado es {totalGanancias}")

def ConteoDeMascotas():
    for h, t in habitacios.items():
        print(h, ".- ", t)

def menu():
    while True:
        valor=0
        print("---Bienvenido al consultorio de tus mascotas---")
        print("1.-Registrar ingreso de mascotas")
        print("2.-Calcular ganancias totales")
        print("3.-Contar huepsedes por tipo")
        op=int(input("ingrese una elleccion: "))
        match op:
            case 1:
                registroMascota()
            case 2:
                gananciaTotales()
            case 3:
                ConteoDeMascotas()
            case 4:
                print("saliendo...")
                break
            case _:
                print("opcion invalida")

menu()