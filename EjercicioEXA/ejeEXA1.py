# PRIMERO DONDE SALEN LOS A00 SON LAS ID ES IMPORTANTE


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
def mostrarAutos(diccio):
    for id, auto in diccio.items():
        print(f"{id}: {auto}")

def mostrarAutosVendidos(diccio):
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {auto}")

def  autos_vendidos_por_marca(diccio,marca):
    total=0
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if auto[0].lower()==marca.lower():
                total+=1
    print(f"el total de autos vendido es {total} en la marca es {marca}")

def busqueda_por_anio(anio_min, anio_max):
    listaAnios=[]
    for id, auto in autos.items():
        if anio_min<auto[2]<anio_max:
            listaAnios.append(f"{auto[0]}{auto[1]}--{id}")
    print(listaAnios)
# marca=input("ingrese la marca que desea ingresar: ")
# autos_vendidos_por_marca(autos,marca)

while True:
    try:
        mino=int(input("ingrese el año minimo: "))
        maxo=int(input("ingrese el año maximo: "))

        busqueda_por_anio(mino, maxo)
        break
    except Exception as e:
        print(e)