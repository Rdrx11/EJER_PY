autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
    'A007' : ['Chevrolet', 'Impreza',1999,4],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
    'A007' : ['01-03-2021','24-09-2025'],
}
print(operaciones["A002"][1])
# crear un a funcion para mostrar todos los autos

def mostrarAutos(diccio):
    for id, auto in diccio.items():
        print(f"{id}: {auto}")

def mostrarAutosVendidos(diccio):
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {auto}")

# Solucion 1

def autos_vendidos_por_marca(diccio,marca):
    total=0
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if auto[0].lower()==marca.lower():
                total+=1
    print(f"El total de autos vendidos es {total} en la marca {marca}")



def busqueda_por_anio(anio_min, anio_max):
    listaAnios=[]
    for id, auto in autos.items():
        if anio_min<auto[2]<anio_max:
            listaAnios.append(f"{auto[0]} {auto[1]}--{id}")
    print(listaAnios)

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        autos[id_auto]=nueva_fecha
        return True
    else:
        return False

mostrarAutos(autos)    
print("-"*50)
mostrarAutosVendidos(autos)
# crear una funcion que muestre solo los autos vendidos
marca=input("Ingrese la marca a buscar: ")
autos_vendidos_por_marca(autos,marca)
