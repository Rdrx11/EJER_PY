# print ("hola Gerges")

# #creando variables

# titulo= "clima de hoy" #tipo string
# deiadelmes=13 # int
# mes=4 # int

# temperatura=22.3 # float

# llueve=False # boolean

# print(titulo)
# print("temperatura actual", temperatura, "grados")
# print(deiadelmes, "-", mes)

# if llueve:
#     print("tiene que llevar paraguas")
# else:    
#     print("puede llevar polera sin mangas")


# pedir password y pin
# pida el password en palabra que debe ser "temu"
# ademas pida el pin que debe ser 3435
# los dos debem estar correctos para acceder al sistema  


# pin=3435
# print("ingrese la palabra secreta")
# password=input()
# if password=="temu":
#     print("has pasado la primera parte, ingrese el pin")
#     int(input())
#     if pin==3435:
#         print("has ingresado al completo")
# else:
#     print("incorrecto intentelo de nuevo")


ingreso=int(input("hola bienvenido, su ingreso: "))
edu=int(input("ingrese su edacucacion nacional"))
print("1.- baico")
print("2.-medio")
print("3.-superior")
nacionalidad=input("ingres su nacionalidad chile/otra:")
credito=0
if ingreso>500000 and ingreso<1000000:
    credito=credito+300000
elif ingreso>1000001 and 1500000:
    credito=credito+650000
elif ingreso>1500001:
    credito=credito+1000000
else:
    print("No le da el sueldo")

if edu==1:
    print("")
elif edu==2:
    credito=credito*1.3
elif edu==3:
    credito=credito*1.5


if nacionalidad=="chilena":
    credito=credito+300000
else:
    print("no tiene bono de nacionalidad")

print("su puntaje de credito es:", credito)