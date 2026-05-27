# explicacion del uso de listas
# lista=[8, 20, 12, 87, 1024]
# #      0, 1,   2, 3, 4
# print(lista)
# print(lista [3])

# for elemento in lista:
#     print("Numero: ", elemento)

# frutas=["Uva", "Pera", "Naranja", "Piña"]
# print(frutas [1])
# Vocales="aeiouAEIOU"
# for fruta in frutas:
#     if fruta[0] in Vocales:
#         print(f"la fruta {fruta} empieza por vocal")
#     else:
#         print(f"la fruta {fruta} no empieza con vocal")

# hacer una lista de nombres y otra de apellidos
# mostar la listas como si fueran nombre

# Nombres="Benito", "Franklin", "Wiston"
# Apellidos= "Musollini", "Roosevelt", "Churshill"
# for N in range (3):
#     print (Nombres[N], Apellidos[N])



# Las listas pueden tener tipos de datos dispares
# Datos=[4, 5.9, "Alonsonic", False]

# for d in Datos:
#     print(d)


# matrix=[[5,8,3], [79,34,24]]
# print(matrix)
# print(matrix [1])
# print(matrix [1][0])

# modificar el pograma del carrito de comprar
# para actualizar poder actualizar listas
# 

producto=[]
while True:
    print("1.- agregar producto")
    print("2.- mostrar producto")
    print("3.- eleminar producto")
    print("4.- salir")
    op=int(input("seleccione una opcion: "))
    match op:
        case 1:
            nombre=input("ingrese el nombre del producto: ")
            precio=int(input("ingrese el precio del producto"))
            nuevo_producto={"nombre": nombre, " precio": precio}
            producto.append()
        case 2:
            print(producto)
        case 3:
            print("oh no hermano")
        case 4:
            print("saliendo")
            break