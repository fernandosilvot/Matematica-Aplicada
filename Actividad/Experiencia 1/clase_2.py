# sea la sucsion, definida por su termino general, Gn = 5*n**3
# calcular los 4 primeros terminos de la sucesion
lista_primeros_terminos = []
for i in range(1,5):
    gn = 5*i**3
    lista_primeros_terminos.append(gn)
print(f"Los {len(lista_primeros_terminos)} primeros terminos de la sucesion son: {lista_primeros_terminos}")

# los 4 terminos que vienen inmediatamente despues del 8vo termino

lista_terminos = []
for i in range(9,13):
    gn = 5*i**3
    lista_terminos.append(gn)
print(f"Los {len(lista_terminos)} terminos que vienen inmediatamente despues del 8vo termino son: {lista_terminos}")

# ¿el termino 40000 pertenece a la sucesion?
# el index() devuelve el indice de un elemento en una lista

lista_terminos = []
for i in range(1,40001):
    gn = 5*i**3
    lista_terminos.append(gn)
print(f"El termino 40000 pertenece a la sucesion: {40000 in lista_terminos} y es el termino {lista_terminos.index(40000)+1} de la sucesion")

# determine si el termino 100 pertenece a la sucesion Sn = 3*n**2+1

lista_terminos = []
for i in range(1,101):
    sn = 3*i**2+1
    lista_terminos.append(sn)
print(f"El termino 100 pertenece a la sucesion: {100 in lista_terminos}")


# sea la sucesion, definida por su termino general, An = 1/n
# determine los terminos: A10, A100, A1000, A10000

lista_terminos = []
for i in range(1,100001):
    an = 1/i
    lista_terminos.append(an)
print(f"Los terminos A10, A100, A1000, A10000 son: {lista_terminos[9]}, {lista_terminos[99]}, {lista_terminos[999]}, {lista_terminos[9999]}, {lista_terminos[99999]}")

# despues de calcular los terminos anteriores ¿que tipo de sucesion es An?

print("Es una sucesion decreciente,")

#sea la sucecion definida por su termino general, Bn = (1+(1/n))**n
# determine los terminos: B10, B100, B1000, B10000 y B100000

lista_terminos = []
for i in range(1,100001):
    bn = (1+(1/i))**i
    lista_terminos.append(bn)
print(f"Los terminos B10, B100, B1000, B10000 y B100000 son: {lista_terminos[9]}, {lista_terminos[99]}, {lista_terminos[999]}, {lista_terminos[9999]}, {lista_terminos[99999]}")

#despues de calcular los terminos anteriores ¿que tipo de sucesion es Bn?

print("Es una sucesion creciente")

#¿que sucede con los terminos de esta sucesion al compararlos con el numero de Euler?

from math import e
if lista_terminos[99999] < e:
    print(f"Se acercan al numero de Euler, pero no lo alcanzan, el numero de Euler es {e}")
else:
    print("alcanzan al numero de Euler")

# considere las sucesiones (Tn)=(2,5,,10,17,26,37,...), (Un)=(0,3,8,15,24,35,...) y (Vn)=(10,40,90,160,250,360,...)
# para cada sucesion, determine la expresion algebraica que define del termino de lugar n

lista_terminos = []
for i in range(1,100001):
    tn = i**2+i+1
    lista_terminos.append(tn)
print(f"Los terminos de la sucesion Tn son: {lista_terminos[0]}, {lista_terminos[1]}, {lista_terminos[2]}, {lista_terminos[3]}, {lista_terminos[4]}")

lista_terminos = []
for i in range(1,100001):
    un = i**2-1
    lista_terminos.append(un)
print(f"Los terminos de la sucesion Un son: {lista_terminos[0]}, {lista_terminos[1]}, {lista_terminos[2]}, {lista_terminos[3]}, {lista_terminos[4]}")

lista_terminos = []
for i in range(1,100001):
    vn = i**3
    lista_terminos.append(vn)
print(f"Los terminos de la sucesion Vn son: {lista_terminos[0]}, {lista_terminos[1]}, {lista_terminos[2]}, {lista_terminos[3]}, {lista_terminos[4]}")
