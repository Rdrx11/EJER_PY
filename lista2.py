# crud de vegetable

vegetales={
    1:"Maracuya",
    2:"Pera",
    3:"cebolla",
    7:"papa"
}
def agregarVegetales():
    print("-"*40)
    agregar=input("ingrese un vegetal: ")
    nuevokey=list(vegetales.keys())[-1]
    vegetales[nuevokey+1]=agregar

def agregarProducto():
    print("cual es el nombre del producto?")
    nombre=input()
    print("cual es su valor?")
    precio=int(input())
    nuevokey=list(productosDicc.keys())[-1]
    productosDicc[nuevokey+1]={"nombre": nombre, "precio": precio }

def mostrarMenu():
    print("-"*40)
    for num, nombre in vegetales.items():
                print(f"{num}= {nombre}")

def mostrarProducto():
    for key, productos in productosDicc.items():
        print(f"{key} . {productos}")
    
def eleminarVegetal():
    mostrarMenu()
    borrar=int(input("que desea borrar?: "))
    del vegetales[borrar]

def eleminarProducto():
    mostrarMenu()
    borrar=int(input("que producto desea borrar?: "))
    del productosDicc[borrar]

def actualizarVegetales ():
    mostrarProducto()
    act=int(input("que desea actualizar?: "))
    vegetales[act]=input("ingrese el nuevo nombre: ")

def actualizarProducto():
    mostrarProducto()
    act=int(input("que producto desea actualizar?: "))
    Nombre=input("ingrese el nuevo nombre: ")
    precio=int(input("ingrese el nuevo precio: "))
    productosDicc[act]={"nombre": Nombre, "precio": precio}

# lista con diccionarios

productosDicc={
    1:{"nombre": "maracuya", "precio": 3000},
    2:{"nombre": "pera", "precio": 1500},
    3:{"nombre": "cebolla", "precio": 1200}
    }
productosDicc[4]={"nombre": "piña", "precio": 3500}
print(productosDicc[2]["precio"])
print(productosDicc[0]["nombre"])
for num, veg in productosDicc.items():
    print(f"{num}.-{veg}")


def VegetalesMENU():
    while True:
        try:
            print("1.-agregar vegetal")
            print("2.-eleminar vegetal")
            print("3.-actualizar vegetal")
            print("4.-mostrar el vegetal")
            print("5.-saliendo")
            op=int(input("seleccione una ocpcion: "))
            match op:
                case 1:
                    # agregarVegetales()
                    agregarProducto
                case 2:
                    # eleminarVegetal()
                    eleminarProducto()
                case 3:
                    # actualizarVegetales()
                    actualizarProducto()
                case 4:
                    # mostrarMenu()
                    mostrarProducto()
                case 5:
                    print("saliendo...")
                    break
        except:
            print("oh no hermano")
VegetalesMENU()

# actualizar su funcion




