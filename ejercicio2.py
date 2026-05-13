# Fabrica de enlatados
# Se necesita hacer el algoritomo de productos enlatados
# Se debe consultar el peso del producto( en gramos) ( solo valores positivos)
# El porcentaje de sodio en él ( solo valores entre 1 y 100)
# y si se va a vender nacional o internacionalmente
# Considerar los criterios en la siguiente tabla

# menos de 500 grs, lata normal
# 501 hassta 1500 bgr, lata mediana
# 1501 y mas , lata grande
# si el sodio es menos de 5%, lata queda igual
# si es entre 5% y 8% lata especial
# si tiene 9% o mas, lata acorazada
# a las latas internacionales, se le debe pegar 
# in sticker de validacion sanitaria

# Ej:800, 7%, 2==> lata mediana espacial con sticker sanitario


# peso=int(input("ingrese el peso: "))
# while peso<1:
#     print("ingrese solo numeros positivos")
#     peso=int(input("ingrese el peso: "))

# sodio=int(input("ingrese el porcetaje de sodio: "))
# while sodio<1 and sodio>100:
#     print ("el porcentaje debe estar, entre el 1 y el 100")
#     sodio=int(input("ingrese el porcetaje de sodio: "))
# print ("1.- mercado nacional")
# print ("2.- mercado internacional")
# mercado=int(input("ingrese una de las opciones:"))
# match mercado:
#     case 1:
#         print ("ha seleccionado el mercado nacional")
#     case 2:
#         print ("ha seleccionado el mercado internacional")
#     case _:
#         print("opcion invalida")
# if peso<500:
#     lata="Lata normal"
# elif 500<peso<1501:
#     lata="Lata mediana"
# elif peso>1500:
#     lata="Lata grande"

# if sodio<5:
#     sod=""
# elif 5<sodio<=8:
#     sod="especial" 
# elif sodio>8:
#     sod="acorazada"

# if mercado==1:
#     sticker=""
# else:
#     sticker="con sticker sanitario"

# print(f"{lata} {sod} {sticker}") 

# simula un cajero automatico con un saldo inicial de $100.000
# spñp se íede sacar/ingresar montos por $5.000
# el usuario puede:
# consultar saldo
# retirar dinero
# depositar dinero
# salir

# debes usar el try except para manejar:

# montos invalidos
# retiro por mayor al saldo disponible
# opciones incorrectas
# entradas no numericas



Monto=100000
op=0
while op!=4:
    print ("1.- consultar saldo")
    print ("2.- retirar dinero")
    print ("3.- depositar dinero")
    print ("4.- salir")
    try:
        opcion=int(input("ingrece una opcion: "))
    except:
        print("solo numeros enteros")

    match opcion:
        case 1:
            print(f"su saldo es ${Monto}")
        case 2:
            
                print("cuanto quiere retirar?")
                try:
                    retiro=int(input())
                
                    if retiro>Monto:
                        if retiro%5000==0:
                            Monto-=retiro
                    else:
                        print("solo multiplos de $5000")
                except ValueError as e:
                    print("solo numeros enteros")
        case 3:
            print("cuanto quiere ingresar?")
            deposito=int(input())
            Monto+=deposito
        case 4:
            print("saliendo")
        case _:
            print("opcion invalida")

