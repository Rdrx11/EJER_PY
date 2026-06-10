productosDicc={
    1:{"nombre": "RTX5090", "precio": 565000},
    2:{"nombre": "Crash Bandicoot 4 PS5", "precio": 80000},
    3:{"nombre": "Cable type C", "precio": 6750}
    }
productosDicc[4]={"nombre": "Steam Deck Oled", "precio": 718000}
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
    try:
        comprar=int(input("Cual producto desea comprar ?: "))
        if comprar in productosDicc:
            print(f"Usted ha comprado {productosDicc[comprar]['nombre']} por un valor de {productosDicc[comprar]['precio']}")
            carrito.append(productosDicc[comprar])
        else:
            print("Producto no existe")
    except ValueError:
        print("Debe ingresar un número válido")
def boleta():
    total=0
    for p in carrito:
        try:
            total+=int(p["precio"])  
        except (ValueError, TypeError):
            print(f"Precio inválido para {p.get('nombre','?')}, contando como 0")
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")    
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