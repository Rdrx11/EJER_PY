# registro de juegos

# debe preguntar al usario Nombre del juego;
# -nodebe incluir espacios y todas Mayusculas
# preguntar precio
# -solo numeros enteros positivos
# -si vale mas de 20000 es indie pero menos de 40000
# -si vale 40000 o mas, es de estudio
# -Mostrar al final cuantos hay de cada categoria
# -E para todos
# - +12 para adolecentes
# - M para personas de mas de 18
# -mostrar resumen

# Hay 4 indies y 5 de estudio. solo 3 son clasifcacion E


# clas=0
# cjue=0
# print ("Nombre un juego:")
# jue1=input()
# while " " in jue1:
#     print("debe ir todo junto")
#     jue1=input()
# jue1=jue1.upper
# print("ponga el precio")
# precio=int(input())
# if 20000<precio<40000:
#   print("tu juego es un indie")
#   cjue+=1
# elif 40000>=precio:
#     print("tu juego es un AAA")
#     cjue+=1
# print ("seleccione una de estas opciones")
# print ("1.- E para todas las edades")
# print ("2.- +12 para adolecentes")
# print ("3.- para personas de mas 18")
# print ("4.- salir")
# clas=int(input())
# match clas:
#     case 1:
#       print("tu juego ahora es para todas las edades")
#       clas="E"
#     case 2:
#        print("tu juego ahora es para adolecentes")
#        clas="+12"
#     case 3:
#         print("tu juego ahora es para mayor de 18 años")
#         clas="M"
#     case 4:
#         print("saliendo")
#     case _:
#         print("opcion invalida")
# print(clas)


# almacenamiento de biblioteca
# Los espacios son noventa
# cada libro usa un espacio
# que diga menu principal
#  1.-espacio disponible
#  2.-poner libros
#  3.-sacar libros
#  4.-Historial de ocupaciones
#  5.-salir
# historial de ocupaciones
#  ==mostrar la cantidad de libros registrados en la biblioteca durante la sesion
#  ==cada registro (poner libros) debe aumenter el historial
#  ==cada retiro (sacar libros) debe disminuir el historial

espacio=90
histpl=0
histsp=0
op=0
while op!=5:
    print ("===MENU PRINCIPAL===")
    print("1.-espacio disponible")
    print("2.-poner libros")
    print("3.-sacar libros")
    print("4.-Historial de ocupaciones")
    print("5.-salir")
    while True:
        try:
            op=int(input("seleccione una opcion: "))
            break
        except:
            print("solo numeros enteros >:v")
    match op:
        case 1:
            print (f"hay en total de espacio {espacio}")
        case 2:
            print ("cuanto libros quiere ingresar")
            pl=int(input())
            if espacio<=90:
                print("lo siento no hay mas espacio disponible")
            else:
                print("gracias por los libros")
                espacio+=pl
                histpl=+1
        case 3:
            print("cuantos libros quieres sacar")
            sp=int(input())
            if espacio==0:
                print("lo siento, no hay mas libros")
            else:
                print("gracias, que disfrute de su lectura")
                espacio-=sp
            histsp+=1
        case 4:
            print(f"el historial de ingresar libros es: {histpl}")
            print(f"el historial de sacar libro es: {histsp}")
        case 5:
            print ("saliendo...")
            break
        case _:
            print("opcion invalida")