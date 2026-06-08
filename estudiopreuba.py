# sp=1
# TEe=0
# TEmas7=0
# Re=0
# cdur=0
# ldur=0
# cpel=0
# while sp==1:
#     print("Ingrese el nombre de su pelicula")
#     pnom=input()
#     while " " in pnom:
#         print("debe ir todo junto")
#         pnom=input()
#     cpel+=1
#     pnom=pnom.lower()
#     print(pnom)
#     try:
#         print("ingrese la duracion de la pelicula")
#         duracion=int(input())
#         if duracion<90 and duracion>0:
#             print("su pelicula es una corta/media duracion")
#             cdur+=1
#         elif duracion>=90:
#             print("su pelicula es de larga duracion")
#             ldur+=1
#         else:
#             print("No se aceptan numeros negativos")
#     except:
#         print ("solo numeros positivos y enteros")
#     print("seleccione su clasificacion para el publico")
#     print("1.- TE para todo espectador")
#     print("2.- TE+7 mayores de 7 años")
#     print("3.- R restringido para todo publico")
#     op=int(input())
#     match op:
#         case 1:
#             print ("su pelicula es para todo publico")
#             TEe+=1
#         case 2:
#             print ("su pelicula es para mayores de 7 años")
#             TEmas7+=1
#         case 3:
#             print("su pelicula es para mayores de 18 años")
#             Re+=1
#         case _:
#             print("opcion invalida")
    
#     print("¿desea continuar?")
#     print ("1.- si")
#     print ("2.- no")
#     resp=int(input())
#     match resp:
#         case 1:
#             sp=1
#         case 2:
#             sp=0
# print("----sus resultados finales----")
# print(f"cantidad de peliculas: {cpel}")
# print(f"cantidad de clasificacion de peliculas: TE {TEe}, T+7 {TEmas7}, R {Re}")
# print(f"cantidad de duracion corta/media: {cdur}")
# print(f"cantidad de duracion larga: {ldur}")




cupos=150
personas=0
Ihisto=0
Shisto=0
while True:
    print ("---MENU---")
    print("1.- cupos disponibles")
    print("2.- ¿cuantas personas van entrar?")
    print("3.- ¿cuantas personas salen del recinto?")
    print("4.- historial de entrada/salida")
    print("5.- Salir...")
    op=int(input())
    match op:
        case 1:
            print(f"sus cupos disponibles son: {cupos}")
        case 2:
            ipersona=int(input("ingrese la cantidad de personas que entran: "))
            if personas+ipersona>cupos:
                print("debe ingresar solo numeros positivos o enteros")
            else:
                print("se ha registrado con exito")
                Ihisto+=ipersona
                cupos-=ipersona
        case 3:
            Spersona=int(input("ingrese la cantidad de personas que Salen del recinto: "))
            if 0>Spersona:
                print("debe ingresar solo numeros positivos o enteros")
            elif cupos>150:
                print("Solo hay 150 espacios dispnibles, no mas de eso")
            else:
                print("se ha registrado con exito")
                Shisto+=Spersona
                cupos+=Spersona
        case 4:
            print(f"historial de quienes ingresan: {Ihisto}")
            print(f"historial de quienes salen: {Shisto}")
        case 5:
            print("saliendo...")
            break
        case _:
            print("opcion invalida")