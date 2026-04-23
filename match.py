# ejemplo
op=0
total=0

# while op!=4: 
#     print("1.- radio esterio $70000")
#     print("2.- lgtv 55 pulgadas super gamer $500000")
#     print("3.- ps5 $580000")
#     print ("4.- salir")
#     print("seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print ("ha selecionado la radio esterio", 70000*1.9)
#             total+=70000*1.9
#         case 2:
#             print ("seleccionado la lgtv 55 pulgadas super gamer", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print ("seleccionado la ps5", 580000*1.19)
#             total+=580000*1.19
#         case 4:
#             print("saliendo...")
#         case _:
#             print ("opcion invalida") #opcion por defecto

# op=0
# while op!=5:
#     print("1.- suma")
#     print("2.- resta")
#     print("3.- multiplicar")
#     print ("4.- dividir")
#     print("seleccione una opcion")
#     op=int(input())

#     match op:
#         case 1:
#             n1=int(input("ingrese un numero: "))
#             n2=int(input("ingrese un numero: "))
#             print(f"el resultado es {n1+n2}")
#         case 2:
#                 n1=int(input("ingrese un numero: "))
#                 n2=int(input("ingrese un numero: "))
#                 print(f"el resultado es {n1-n2}")
#         case 3:
#                n1=int(input("ingrese un numero: "))
#                n2=int(input("ingrese un numero: "))
#                print(f"el resultado es {n1*n2}")
#         case 4:
#                 n1=int(input("ingrese un numero: "))
#                 n2=int(input("ingrese un numero: "))
#                 print(f"el resultado es {n1/n2}")
            


# def saludo():
#     print ("hola como rod")
# saludo
# name="rod"
# def adios():
#     print(f"ya nos vamos?"{ name})
# adios()
# def suma():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese un numero: "))
#     print(f"el resultado es: (n1+n2)")
# op=0
# while op!<=5:
name="rod"
def saludo():
    print(f"hola {name}")
def adios():
    print(f"adios {name}")

def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese un numero: "))
    print(f"el resltado es: {n1+n2}")
def resta():
        n1=int(input("ingrese un numero: "))
        n2=int(input("ingrese un numero: "))
        print(f"el resltado es: {n1-n2}")
def multiplicar():
         n1=int(input("ingrese un numero: "))
         n2=int(input("ingrese un numero: "))
         print(f"el resltado es: {n1*n2}")
def dividir():
          n1=int(input("ingrese un numero: "))
          n2=int(input("ingrese un numero: "))
          print(f"el resltado es: {n1/n2}")
op=0
while op!=4:
  print ("seleccione un porgrama")
  print ("1.- suma")
  print ("2.- resta")
  print ("3.- multiplicar")
  print ("4.- dividir")
  op=int(input())
  match op:
        case 1:
            saludo()
            suma()
            adios()
        case 2:
              saludo()
              resta ()
              adios ()
        case 3:
              saludo()
              multiplicar()
              adios()
        case 4:
              saludo ()
              dividir ()
              adios ()