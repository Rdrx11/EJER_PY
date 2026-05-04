# saldo=1000
# print("Saldo inicial: ", saldo)
# op=0
# while op!=4:
#     print ("1.- retirar")
#     print ("2.- depositar")
#     print ("3.- consultar saldo")
#     print ("4.- salir")
#     op=int(input())
#     match op:
#       case 1:
#             print("cuanto desea retirar")
#             retiro=int(input())
#             if retiro>saldo:
#                 print("no tienes suficiente dinero")
#             else:
#                 saldo-=retiro
#                 print("retiro exitoso") 
#       case 2:
#             print("cuanto desea depositar")
#             deposito=int(input())
#             saldo+=deposito
#             print("deposito exitoso")
#       case 3:
#             print("tu saldo es: ", saldo)
#       case 4:            
#               print("gracias por usar el cajero")
#       case _:
#             print ("opcion invalida")

# Instrucciones:

# El programa genera un número secreto entre 1 y 20 usando random.randint.
# El usuario debe intentar adivinarlo.
# El bucle while debe seguir pidiendo números hasta que el usuario acierte.
# Dentro del bucle, usa if para decirle si el número secreto es mayor o menor al que escribió.

# import random
# num=random.randint(1, 20)
# pos=1
# r=int(input("adivine el numero: "))
# while pos<5 and r!=num:
#     if r>num:
#         print("te pasaste")
#         r=int(input("ingrese de nuevo un numero: "))
#     else:
#         print("el numero es mayor al que dijiste")
#         r=int(input("ingrese de nuevo un numero: "))
#         pos+=1
# if r==num:
#     print("ehorabuena lo ha adivinado")
# else:
#     print("jajajaja perdiste que pendeyo")


# Pide al usuario un número de inicio y un número de fin.
# Usa un bucle for con range para recorrer desde el inicio hasta el fin.
# Para cada número, usa el operador módulo % para saber si es par o impar.
# Al final, imprime cuántos pares y cuántos impares hubo en total.

# inicio=int(input("ingrese su numero de inicio: "))
# fin=int(input ("ingrese su numero de fin: "))
# pares=0
# impares=0
# for numeros in range (inicio, fin+1 ):
#     if numeros % 2==0:
#         pares+=1
#     else:
#         impares+=1
# print("Cantidad de pares:", pares)
# print("Cantidad de impares:", impares)

# Crea un programa que pida al usuario cuántas temperaturas quiere ingresar.
# Usa un range() para que el for se repita esa cantidad de veces.
# Dentro del for, pide la temperatura actual.
# Al final del bucle, el programa debe mostrar:
# Cuántas temperaturas fueron bajo cero (menores a 0).
# Cuántas temperaturas fueron normales (entre 0 y 30).
# Cuántas fueron "Ola de calor" (mayores a 30)

# cantidad=int(input("¿que temperatura quiere ingresesar?:  "))
# bajocero=0
# normal=0
# oladecalor=0


# for i in range (cantidad):
#     tem=float(input(f"ingrese una temperatura #{i+1}: "))
#     if tem<0:
#         bajocero+=1
#     elif 0<=tem<=30:
#         normal+=1
#     else:
#         oladecalor+=1
# print ("resultado: ")
# print("Bajo cero:", bajocero)
# print("Normales:", normal)
# print("Ola de calor:", oladecalor)
# Pide al usuario un número inicial (ejemplo: 10).

# El programa debe contar hacia atrás desde ese número hasta el 0.
# Regla especial: Si el número es impar, el programa debe imprimir "¡Ignición parcial!" en lugar del número.
# Al final (fuera del for), debe imprimir "¡DESPEGUE! ".

cont = int(input("Ingrese el número inicial: "))

for i in range(cont, -1, -1):  
    if i % 2 != 0: 
        print("¡Ignición parcial!")
    else:
        print(i)

print("¡DESPEGUE!")