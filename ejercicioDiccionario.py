# productosDicc={
#     1:{"nombre": "maracuya", "precio": 3000},
#     2:{"nombre": "pera", "precio": 1500},
#     3:{"nombre": "cebolla", "precio": 1200}
#     }
# productosDicc[4]={"nombre": "tomate", "precio": 1500}
# list(productosDicc.keys())[-1]

# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
# for i in productosDicc.values():
#     print(i,["nombre"], " ", i["precio"])
# for i, d in productosDicc.items():
#     print(d["nombre"], d["precio"])
# print(productosDicc[2]["precio"])
# print(productosDicc[3]["nombre"])

# Pokemon={
#     {"nombre": "speon"},
#     {"nvl": 32},
#     {"hp":102},
#     {"atk":
#        {
#            1:{"nombre":"placaje", "daño": [16-24]},
#            2:{"nombre":"placaje", "daño": [16-24]},
#            3:{"nombre":"placaje", "daño": [16-24]},
#            4:{"nombre":"placaje", "daño": [16-24]},
#     }}
#     "def":10,

#     }
productosDicc={
    1:{"nombre": "maracuya", "precio": 3000},
    2:{"nombre": "pera", "precio": 1500},
    3:{"nombre": "cebolla", "precio": 1200}
    }
productosDicc[4]={"nombre": "tomate", "precio": 1500}
list(productosDicc.keys())[-1]

carrito=[]
def agregaProducto():
    nombreP=input("Ingrese el nombre del Producto: ")
    precioP=int(input("Ingrese el precio del Producto: "))
    productosDicc[list(productosDicc.keys())[-1]+1]={"nombre": nombreP, "precio": precioP} 
def muestraProducto():
    print("-"*30)
    for nombre, precio in productosDicc.items():
        print(f"{nombre} .-  {precio}")
    print("-"*30)
def eliminaProducto():
    muestraProducto()
    borra=int(input("Cual desea eliminar?: "))
    del productosDicc[borra]
def actualiazaProducto():
    muestraProducto()
    actualiza=int(input("Cual producto desea actualizar?: "))
    nuevonombre=input("ingrese el nuevo nombre") 
    nuevoPRECIO=input("ingrese el nuevo precio") 
    productosDicc[actualiza]={"nombre":nuevonombre , "precio": nuevoPRECIO}
def comprar():
    muestraProducto()
    while True:
        try:
            comprar=int(input("Cual producto desea comprar? (0 para salir): "))
            if comprar==0:
                break
            elif comprar in productosDicc:
                print(f"Usted ha comprado {productosDicc[comprar]['nombre']} por un valor de {productosDicc[comprar]['precio']}")
                carrito.append(productosDicc[comprar])
            else:
                print("Producto no existe")
        except ValueError:
            print("Debe ingresar un número válido")
def boleta():
    print("-"*30, "0", "-"*30)
    total=0
    for p in carrito:
            print (p["nombre"], "___$", p["precio"])
            total+=int(p["precio"])
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
    print("-"*30, "0", "-"*30)
def productosMenu():
    while True:
        try:
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Producto")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaProducto()
                case 2:
                    eliminaProducto()
                case 3:
                    actualiazaProducto()
                case 4:
                    muestraProducto()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)
productosMenu()