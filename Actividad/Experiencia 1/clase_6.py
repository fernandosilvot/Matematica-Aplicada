import numpy as np
# Ejercicio 1

# Utilizando notacion de sumatorias, exprese las siguientes sumas.

# A) a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13

print(f"a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 = {sum([i for i in range(5, 14)])}")

# B) b38 + b39 + b40 + b41 + b42 + b43 + b44 + b45 + b46 + b47 + b48

print(f"b38 + b39 + b40 + b41 + b42 + b43 + b44 + b45 + b46 + b47 + b48 = {sum([i for i in range(38, 49)])}")

# C) c21 + c22 + c23 + c24 + ... + c91 + c92 + c93

print(f"c21 + c22 + c23 + c24 + ... + c91 + c92 + c93 = {sum([i for i in range(21, 94)])}")

#Ejercicio 2

# Sea la sucesion An=3*n**2+7 determine
# nota : utilice la notacion de sumatorias al expresar cada resultado

# A) la suma de los 4 primeros terminos 

for i in range(1, 5):
    an = 3 * i ** 2 + 7
    print(f"a{i} = {an}")


#Ejercicio 3

# Un nuevo canal de Youtube registra 50 visitas la primera semana de funcionamiento, registra 66 visitas la segunda, 82 la tercera y asi sucesivamente. Representado por Vi la cantidad de visitas en la semana i,

# A) Escriba la expresion algebraica para el termino Vi
q1= 50
q2= 66
q3= 82
d = q2 - q1
d2 = q3 - q2
if d == d2:
    print(f"Vi = 50 + (n-1) * {d}")

# B) Escriba la expresion algebreaica para el numero total de visitas durante las n primeras semanas

print(f"n/2*(2*{q1}+(n-1)*{d})")

#Ejercicio 4

# Diego decide ahorrar en dólares para un viaje durante dos años y medio. El primer mes ahorra 900 dólares, el segundo mes 810 dólares, el tercer mes 729 dólares, y así sucesivamente. Represente por d; la cantidad de dólares que ahorra Diego en el mes i.

# A) Escriba la expresion algebraica para el termino di

q1= 900
q2= 810
q3= 729

if q2/q1 == q3/q2:
    r = q2/q1
    print(f"di = {q1} * {r} ** (n-1)")

# B) Escriba la expresion algebraica que calcula el total de dinero ahorrado por 

print(f"{q1} * (({r} ** n) - 1) / (1 - {r})")