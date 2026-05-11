
# while True:
#     try:
#         edad=int(input("ingresa tu edad: "))
#         break
#     except ValueError as mostrarError:
#         print("solo debes ingresar numeros enteros")
#         print(mostrarError)

# while True:
#     try:   
#         num=int(input("ingrese su edad: "))#si aparece un error
#         # salta a la linea 15 (o sea salta a la linea 6) donde esta except para manejar e error
#         break#sirve para termminar el proceso
#     except ValueError as e:
#         print("solo se aceptan numeros enteros")
#         print(e)
# print("su edad es", num)

#ingrese numeros de manera indefinidamente
# hasta que ponga el numero 0
# #y sumelos

# n2=0
# while True:
#     try:
#         for i in range(10):
#             n1=int(input("ingrese un numero: "))
#             n2+=n1
#             if n1==0:
#                 break
#     except:
#             print("Solo numeros enteros")

# print("el total es:", n2)

# op=0
# total=0
# cantprod=0
# while op!=4: 
#     try:
#         print("1.- radio esterio $70000")
#         print("2.- lgtv 55 pulgadas super gamer $500000")
#         print("3.- ps5 $580000")
#         print("4.- salir")
#         print("seleccione una opcion")
#         op=int(input())
#         match op:
#             case 1:
#                 print ("ha selecionado la radio esterio", 70000*1.9)
#                 total+=70000*1.9
#                 cantprod+=1
#             case 2:
#                 print ("seleccionado la lgtv 55 pulgadas super gamer", 500000*1.19)
#                 total+=500000*1.19
#                 cantprod+=1
#             case 3:
#                 print ("seleccionado la ps5", 580000*1.19)
#                 total+=580000*1.19
#                 cantprod+=1
#             case 4:
#                 print("saliendo...")
#             case _:
#                 print ("opcion invalida") #opcion por defecto
           
#     except:
#         print("Solo debe ingresar numeros enteros")


# porc=int(input("ingrese el porcentaje: "))
# if porc>0 and porc<100:
#     print("porcentaje es correcto")
# else:
#     print("porcentaje fuera de rango")

# toon1=input("ingrese el toon 1")
# toon2=input("ingrese el toon 2")
# v1=0
# v2=0
# while True:
#     try:
#         cant=int(input("cuantos votantes son? "))
#         break
#     except:
#         print("solo puedes ingresar valores positivos")
# le falta desarrollo
