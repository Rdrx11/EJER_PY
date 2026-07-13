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

def Mostrar_Autos(Diccio):
    for id, auto in Diccio.items():
        print(f"{id}: {auto}")
    print("-"*30)

def mostrarAutosVendidos(Diccio):
    for id, auto in Diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {auto}")
    print("-"*30)

mostrarAutosVendidos(autos)
mostrarAutosVendidos(operaciones)

def AutosVendidosPor_Marca(diccio, marca):
    total=0
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if auto[0].lower()==marca.lower:
                total+=1
    print(f"total de autos vendidos {total} marca {marca}")

marca=input("marca: ")
AutosVendidosPor_Marca(autos, marca)

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        autos[id_auto]=nueva_fecha
        return True
    else:
        return False


def busquedaPor_Año(añoMIN, añoMAX):
    listaAÑO=[]
    for id, auto in autos.items():
        añoAuto= auto[2]
        estado_venta= operaciones[id][1]
        if (añoMIN<=añoAuto<=añoMAX) and (estado_venta=="Pendiente"):
            marca= auto[0]
            modelo= auto[1]
            listaAÑO.append(f"{marca} {modelo}--{id}")
    listaAÑO.sort()
    if listaAÑO:
        for item in listaAÑO:
            print (item)
            print ("-"*30)
    else:
        print("No se encontraron vehículos disponibles en ese rango de años.")

while True:
    try:
        min_año=int(input("Ingrese el año minimo no menos de 1900: "))
        max_año=int(input("ingrese el año maximo: "))
        if min_año>=max_año:
            print("el año minimo debe ser mayor que el maximo")
            continue
        busquedaPor_Año(min_año, max_año)
        break
    except ValueError:
        print("Error: Los años deben ser números enteros válidos. Intente de nuevo.")

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        autos[id_auto]=nueva_fecha
        return True
    else:
        return False

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