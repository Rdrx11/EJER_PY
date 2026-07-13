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

def mostrar_autos(diccio):
    for id, auto in diccio.items():
        print(f"{id}: {auto}")
    print("-"*30)

mostrar_autos(autos)
mostrar_autos(operaciones)

def mostrarAutos_Vedidos(diccio):
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {auto}")
    print("-"*30)

mostrarAutos_Vedidos(autos)
mostrarAutos_Vedidos(operaciones)

def AutosVendidosPor_Marca(diccio, marca):
    total=0
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if auto.lower()==marca.lower:
                total+=1
    print(f"total de autos vendidos {auto} marca {marca}")

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        autos[id_auto]=nueva_fecha
        return True
    else:
        return False
# marca=input("marca: ")
# AutosVendidosPor_Marca(autos, marca)

def busquedaPor_Año(añoMIN, añoMAX):
    listaAÑO=[]
    for id, auto in autos.items():
        if añoMIN<auto[2]>añoMAX:
            listaAÑO.append(f"{auto[0]} | {auto[1]} | {id} | {auto[2]} ")
    print (listaAÑO)

while True:
   try:
        Min=int(input("ingrese el año minimo: "))
        Max=int(input("ingrese el año maximo: "))
        if Min>Max:
            print ("No se debe pasar mas alla del año maximo")
            continue
        busquedaPor_Año(max, min)
        break
   except Exception as e:
       print(e)

while True:
    try:
        id_auto=input("ingrese el id del auto: ")
        nueva_fecha=input("ingrese la fecha de venta: ")

        if actualizar_fecha_venta(id_auto, nueva_fecha):
            print("Fecha de venta actualizada")
        else:
            print("El auto no existe")
        next=input("Desea actualizar otro vehiculo? s/n: ")
        if next=="n":
            break

    except Exception as e:
        print(e)


def validar_dato_id(id):
    if not id or id.strip() == "":
        return False
    if id in autos:
        return False
    return True

def validar_dato_texto(texto):
    if not texto or texto.strip() == "":
        return False
    return True

def validar_dato_año(año):
    try:
        val=int(año)
        return val>1900
    except ValueError:
        return False

def validar_dato_ranking(rank):
    try:
        val=int (rank)
        return 1<=val<=5
    except ValueError:
        return False

def registrar_auto():
    id=input("ingrese la nueva id para el nuevo auto (ej: A008): ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    Marca=input("ingrese la marca para el nuevo auto: ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    Modelo=input("ingrese el modelo para el nuevo auto: ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    año=input("Ingrese Año (mayor a 1900): ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    ranking = input("Ingrese Ranking (1 al 5): ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    fecha_ingreso = input("Ingrese Fecha de Ingreso (DD-MM-AAAA): ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    fecha_venta = input("Ingrese Fecha de Venta (o presione Enter para 'Pendiente'): ")
    if not validar_dato_id(id):
        print("❌ Error: El ID está vacío o ya existe en el sistema. Registro abortado.\n")
        return
    autos[id]= [Marca, Modelo, int(año), int(ranking)]
    operaciones[id] = [fecha_ingreso, fecha_venta]

def eleminar_auto(id):
    if id in autos and id in operaciones:
        del autos[id]
        del operaciones[id]
        return True
    return False

registrar_auto()

idAUTO=input("Ingrese el ID del vehículo que desea eliminar (ej: A001): ")
if eleminar_auto(idAUTO):
    print(f" Éxito: El vehículo '{idAUTO}' ha sido eliminado correctamente de ambos diccionarios.")
else:
    print(f" Error: El identificador '{idAUTO}' no fue encontrado en el sistema.")
