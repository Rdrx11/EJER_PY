# nombre=input("ingrese su nombre: ")
# nom=nombre.split()
# print (nom)

# n1=int(input("ingrese un numero: "))
# n2=int(input("ingrese un numero: "))

# def suma(n1,n2):
#     return n1+n2
# def resta(n1, n2):
#     return n1-n2
# def dividir(n1,n2):
#     return n1/n2
# def multiplicar(n1,n2):
#  return n1*n2

# cree una funcion para pedir notas
# y ponerlas en el argumento
# para sacar el promedio
cantNot=int(input("ingrese las cantidad de notas: "))
notas=[0]
for n in range(cantNot):
    nota=int(input(f"ingrese la nota {n+1}: "))
    notas.append(n)

def calculaProm(notas):
    return sum(notas)/len(notas)
print ("El promefdio es ", calculaProm(notas), notas)
        
