Beyblade = {
    'A001' : ['Croc','Blitz', 2344],
    'A002' : ['Dran', 'Sword', 1234],
    'A003' : ['Dran', 'Buster', 3453],
    'A004' : ['Wolf', 'Silver', 2323],
    'A005' : ['Drake','Impact', 1002],
    'A006' : ['Dragoon', 'Meteor', 1245],
    'A007' : ['Shark', 'Scale', 2025]}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
    'A007' : ['01-03-2021','24-09-2025']}

def mostrarBeyblade(diccio):
    for id, Beyblades in diccio.items():
        print(f"{id}: {Beyblades}")
    print("-"*30)

# mostrarBeyblade(Beyblade)
# mostrarBeyblade(operaciones)

def mostrarBeybladesVendidos(diccio):
    for id, Beyblades in diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {Beyblades}")
    print("-"*30)
# mostrarBeybladesVendidos(operaciones)

def  Beyblades_vendidos_por_modelo(diccio,modelo):
    total=0
    for id, Beyblades in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if Beyblades[0].lower()==modelo.lower():
                total+=1
        print(f"el total de beyblades vendidos son {total} en el modelo {modelo}")
# modelo=input("ingrese el modelo que desea buscar: ")
# Beyblades_vendidos_por_modelo(Beyblade,modelo)

def actualizar_fecha_venta(id_Beyblade, nueva_fecha):
    if id_Beyblade in Beyblade:
        Beyblade[id_Beyblade]=nueva_fecha
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