# sin argunmento y sin retorno
def saludo():
    print("hola que tal?")
# sin argumento y con retorno
def suma():
    num1=3
    num2=5
    return(num1+num2)

def esMayor():
    edad=24
    if edad>=18:
        return True
    else:
        return False

# resultado=suma()
# print(resultado*2)

# print (esMayor())


# con argumento y sib retorno
def saludame(name):
    print ("hola", name)
# saludame ("Yoshi")

def calculaIVA(neto):
    print(f"el precio con iva es {neto*19}")
# calculaIVA(5000)

# con argumento y con retorno
def sumaca(n1,n2):
    return(n1+n2)


def calculaIVAca(neto):
    print(f"el precio con iva es {neto*19}")
# print ("el resultado es:", (7,10))
# # print ("el total del iva es:", calculaIVAca(10000))



# v=int(input("Ingrese el valor neto: "))
# print("el total con iva es:" (v))

def calculaDescuento(valor,desc):
    return 