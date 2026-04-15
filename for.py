#ejemplo y explicacion de for
# for I in range(5):
#     print(I+1)
#     print(I+1)

#Pedir un numero al usuario
#mostrar un saludo en esa cantidad de veceses
# num=int(input("ingrese un numero: "))
# for I in range(num):
#     print("hola perro")

#Pedir un numero al usuario
#y mostrar la tabla de multiplicar
#de ese numero hasta 10.
# N=int(input("ingrese un numero: "))
# for I in range(10):
#     print(N ,"x", I+1,"=", N*(I+1))
#     print(N ,"/", I+1,"=", N/(I+1))

#Pedir un numero al usuario
#y mostrar la suma desde el 1
#hasta ese numero
#ej--> 1+2+3=6

# N=int(input("ingrese un numero: "))

# for i in range(N):
#    suma=suma+i+1
# print("el resultado de la suma es: ", suma)

#perdir la cantidad de notas al usuario
#luego pedir cada nota individialmente
#calcular el promedio de todas las notas
#mostrar si aprueba o no

# N=int(input("ingrese la cantidad de notas: "))
# suma=0
# for i in range (N):
#     N=float(input("Ingrese la nota"))
#     suma=suma+1
# prom= suma/N
# print("El promedio es", prom)

# if prom>=4:
#     print ("alumno aprovado")
# else:
#     print("no aprobo")
# cant=0

# nombre=input(("ingrese su nombre: "))
# for i in nombre:
#     print(i)
#     cant=cant+1
# print ("la cantidad de letras es", cant)

# nombre=input(("ingrese su nombre: "))
# vol=0
# cons=0
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU":
#         vol=vol+1
#     elif I==" ":
#         print (" ")
#     else:
#         cons=cons+1
# print ("la cantidad de Vocales es", vol)
# print ("la cantidad de Vocales es", cons)

#pida la cantidad de alumnos
#por cada alumno pida la cant
#de notas , Saque el promedio
#muestre la cantidad de alumnos
#aprovados o no

Alum=int(input("ingrese la cantidad de alumnos: "))
print ("la cantidad de alumno es: ", Alum)
prom=0
for prom in range (Alum):
    print ("la cantidad de alumno es: ", Alum)