# registro de juegos

# debe preguntar al usario Nombre del juego;
# -no debe incluir espacios y todas Mayusculas
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


# sl=1
# indie=0
# estudios=0
# e = 0
# mas12 = 0
# m = 0
# while sl==1:
#     print ("Nombre un juego:")
#     jue1=input()
#     while " " in jue1:
#         print("debe ir todo junto")
#         jue1=input().strip
#     jue1=jue1.upper()
#     print(jue1)
#     try:
#        print("ponga el precio")
#        precio=int(input())
#     except Exception:
#         print("solo numeros enteros")
#     if 20000<precio<40000:
#         print("tu juego es un indie") 
#         indie+=1
#     elif 40000<=precio:
#       print("tu juego es un AAA")
#       estudios+=1
#     else:
#         print("tu juego es un indie")
#         indie+=1
#     print ("seleccione una de estas opciones")
#     print ("1.- E para todas las edades")
#     print ("2.- +12 para adolecentes")
#     print ("3.- para personas de mas 18")
#     print ("4.- salir")
#     clas=int(input())
#     match clas:
#         case 1:
#             print("tu juego ahora es para todas las edades")
#             e +=1
#         case 2:
#             print("tu juego ahora es para adolecentes")
#             mas12 +=1
#         case 3:
#             print("tu juego ahora es para mayor de 18 años")
#             m +=1
#         case 4:
#             print("saliendo")
#             sl=0
#         case _:
#             print("opcion invalida")
# print("\n" + "="*40)
# print("resumuen de los juegos")
# print("="*40)
# print(f"total de juegos resgistrados: {indie + estudios}")
# print(f"indies: {indie}")
# print(f"De estudio (AAA): {estudios}")
# print(f"clasificacion E: {e}")
# print(f"clasificacion +12: {mas12}")
# print(f"clasificacion M: {m}")
# print(f"="*40)

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

# espacio=90
# histpl=0
# histsp=0
# op=0
# while op!=5:
#     print ("===MENU PRINCIPAL===")
#     print("1.-espacio disponible")
#     print("2.-poner libros")
#     print("3.-sacar libros")
#     print("4.-Historial de ocupaciones")
#     print("5.-salir")
#     while True:
#         try:
#             op=int(input("seleccione una opcion: "))
#             break
#         except:
#             print("solo numeros enteros >:v")
#     match op:
#         case 1:
#             print (f"hay en total de espacio {espacio}")
#         case 2:
#             print ("cuanto libros quiere ingresar")
#             pl=int(input())
#             if espacio<=sp:
#                 print("lo siento no hay mas espacio disponible")
#             else:
#                 print("gracias por los libros")
#                 espacio+=pl
#                 histpl=+1
#         case 3:
#             print("cuantos libros quieres sacar")
#             sp=int(input())
#             if sp > espacio:
#                 print(f"lo siento, no puedes sacar tantos libros. Solo quedan {espacio}")
#             else:
#                 print("gracias, que disfrute de su lectura")
#                 espacio-=sp
#             histsp+=1
#         case 4:
#             print(f"el historial de ingresar libros es: {histpl}")
#             print(f"el historial de sacar libro es: {histsp}")
#         case 5:
#             print ("saliendo...")
#             break
#         case _:
#             print("opcion invalida")