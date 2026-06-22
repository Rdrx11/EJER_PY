acaparete={
    1:[],
    2:[],
    3:[],
    4:[]
}

def agregarJuguete():
    valor=0
    print("Ingresar vehiculo nuevo")
    tipo=int(input(" \n1.-Cartas Pokemon\n2.-Barbie\n3.-Beyblade x \n4.-capitan american \n Que jueguete es?: "))
    match tipo:
        case 1:
            valor=5000
        case 2:
            valor=8000
        case 3:
            valor=20000
        case 4:
            valor=14000
    estante=int(input("En que estante va?: "))
    if estante in [1,2,3,4] and valor>0 :
        if len(acaparete[estante])<10:
            acaparete[estante].append(valor)
            print("Agregado al piso", estante)
        else:
            print("Estante lleno")
    else:
        print("Estante no válido")

def gananciasDeVentas():
    totalGanancias=0
    print("Contando Ganancias")
    for estante in acaparete.values():
        totalGanancias+=sum(estante)
    print(f"El total recuado es {totalGanancias}")

def cantidadDeJuguetes():
    totalJuguetes=0
    for estante in acaparete.values():
        totalJuguetes+=len(estante)
    print("El total de juguestes en los estantes es:", totalJuguetes)




def menu():

    while True:
        print(
            "\n 1.- Agregar juguetes a la estanteria \n 2.- Ganancias de las ventas \n 3.- Cuantos juguetes hay \n 4.- Salir"
        )
        op=int(input("ingrese una opcion: "))
        match op:
            case 1:
                agregarJuguete()
            case 2:
                gananciasDeVentas()
            case 3:
                cantidadDeJuguetes()
            case 4:
                print("saliendo")
                break
            case _:
                print("opcion invalida")
menu()
