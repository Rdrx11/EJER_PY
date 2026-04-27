# uso y explicacion de ramdom

# import random as rd

# print(rd.randint (1, 10))


# import random
# num= random.randint(1, 10)
# for i in range (num):
#     print("hola")


# import random
# strike=random.randint(10,70)

# if strike>50:
#     print("fue mucho damage:", strike)
# else:
#     print("no fue mucho damage:", strike)

# 3 personas jeuga golf
# cada persona tiene posibilidad de golpear
# y la dsitancia varia entre 60 y 190
# mostrar el golpe mas fuerte

# import random
# j1=random.randint(60, 90)
# j2=random.randint(60,90)
# j3=random.randint(60, 90)

# print(f"el jugador 1 golpeo la pelota a {j1}")
# print(f"el jugador 1 golpeo la pelota a {j1}")
# print(f"el jugador 1 golpeo la pelota a {j1}")
# if j1>j2 and j1>j3:
#     print("gano j1")
# elif j2>j3:
#     print ("gano j2")
# else:
#     print("gano j3")

# killer instic

# dos peleadores se piden de la pelea
# cada peleador inicia con 100 de HP
# se debe hace una pelea por turnos
# y cada golpe  varoa entre 7 y 18
# se termina el match cuando uno de los 2
# tiene su HP menor o igual a 0
# se deebe mostrar el ganador al final
# Bonus: mostrar al barras de vida de cada peleador

import random
import time
p1=100
p2=100
j1=input("ingrese el nombre del peleador: ")
j2=input("ingrese el nombre del peleador: ")
turno=random.randint(1,2)
while p1>0 or p2>0:
    if turno%2==0:
        print(f"turno de {j1}")
        damage=random.randint(7,18)
        print(f"el {j1} ataca con {damage}")
        p2-=damage
        print(f"el hp de {j2} es {p2}")
        time.sleep(1)
    else:
        print(f"turno de {j2}")
        damage=random.randint(7,18)
        print(f"el {j2} ataca con {damage}")
        p1-=damage
        print(f"el hp de {j1} es {p1}")
        time.sleep (1)
    turno+=1
print(p1," "*p1)
print(p2," "*p2)
if p1>p2:
    print("el ganador es ", p1)
else:
    print("el ganador es ", p2)