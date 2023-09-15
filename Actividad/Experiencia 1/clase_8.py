# matrizes 
import numpy as np # se importa la libreria numpy
# np.array() # se crea una matriz con la funcion array de numpy
# np.shape() # se obtiene la dimension de la matriz con la funcion shape de numpy
# Ejercicio 1

# cuales son las dimensiones de la matriz D 

"""
D =[ -7 , 24, 2
      1 , 15,11
     -9 , 12 ,0
      8, -3 , -1]
"""
D = np.array([[-7 , 24, 2],[1 , 15 ,11],[-9 , 12 ,0],[8, -3 , -1]]) # matriz D se crea con la funcion array de numpy es una matriz de 4x3

print(f"la matriz D es de {D.shape} dimensiones") # se imprime la dimension de la matriz D


# Ejercicio 2

# cuales son las dimensiones de la matriz E

"""
E = [[-2,6,1,3], [0,-8,3,10]]
"""

E = np.array([[-2,6,1,3], [0,-8,3,10]]) # matriz E se crea con la funcion array de numpy es una matriz de 2x4

print(f"la matriz E es de {E.shape} dimensiones") # se imprime la dimension de la matriz E

# Ejercicio 3

# cuales son las dimensiones de la matriz F

"""
F = [[-2,], [0], [10]]
"""

F = np.array([[-2,], [0], [10]]) # matriz F se crea con la funcion array de numpy es una matriz de 3x1

print(f"la matriz F es de {F.shape} dimensiones") # se imprime la dimension de la matriz F

# Ejercicio 4

# cuales son las dimensiones de la matriz G

"""
G = [[1,6,9,3], [2,5,8,1],[0,2,2,4]]
"""

G = np.array([[1,6,9,3], [2,5,8,1],[0,2,2,4]]) # matriz G se crea con la funcion array de numpy es una matriz de 3x4

print(f"la matriz G es de {G.shape} dimensiones") # se imprime la dimension de la matriz G

# Ejercicio 5

# cuales son las dimensiones de la matriz H

"""
H = [[8,-3]]
"""

H = np.array([[8,-3]]) # matriz H se crea con la funcion array de numpy es una matriz de 1x2

print(f"la matriz H es de {H.shape} dimensiones") # se imprime la dimension de la matriz H

# Ejercicio 6

# cuales son las dimensiones de la matriz I

"""
I = [[8,6,,9,-2],[8,-3,7,9],[-1,-9,5,1],[2,1,-9,3],[1,-3,8,-8]]
"""

I = np.array([[8,6,9,-2],[8,-3,7,9],[-1,-9,5,1],[2,1,-9,3],[1,-3,8,-8]]) # matriz I se crea con la funcion array de numpy es una matriz de 5x4

print(f"la matriz I es de {I.shape} dimensiones") # se imprime la dimension de la matriz I

# Ejercicio 7

# la matriz c es una matriz de 2x3 con c1,2 =6
A = np.array([[1,2],[6,4],[5,-2]]) 
B = np.array([[-9,6],[7,-3],[-3,5]])
C = np.array([[2,6,8],[7,-3,1]])
D = np.array([[2,10,8],[6,-3,1]])
print(f"la matriz A es de {A.shape} dimensiones") # se imprime la dimension de la matriz A

# Ejercicio 8
A= np.array([[2,-4,8],[1,5,-5],[-2,6,2]])

print(f"A(1,3) = {A[0,2]}") # se imprime el valor de la posicion 1,3 de la matriz A


# Ejercicio 9
B= np.array([[12,-2.3],[4.6,1.2]])

print(f"B(2,1) = {B[1,0]}")

# Ejercicio 10
A = np.array([[12,14,-3,6],[2,18,-10,12],[1,-9,40,-2],[3,3,6,1]])

print(f"A(2,4) = {A[1,3]}")

# Ejercicio 11
A = np.array([[-8,-4,13],[23,12,-7],[18,10,1]])

print(f"A(1,3) = {A[0,2]}")

# Ejercicio 12
A = np.array([[-3,3,-6,5,8],[12,35,13,14,2],[-6,8,9,-18,1],[-5,-3,-23,6,4],[4,-5,15,3,10]])

print(f"A(4,1) = {A[3,0]}")

# Ejercicio 13
A = np.array([[8,6,3,9,5],[2,1,-14,12,-4],[6,-18,3,-25,-1],[2,4,6,-8,10]])

print(f"A(3,5) = {A[2,4]}")

# Ejercicio 14 

from fractions import Fraction
M = np.array([[2, 4, 7], [-1, 0, -3]])
T = np.array([[2, 3.1, 5], [4.2, 7, 10], [6, 9, 14]])
N = np.array([[0.3, 1.7], [8.2, 4.5]])
K = np.array([[Fraction(3, 4), Fraction(1, 8), Fraction(2, 3)]])
S = np.array([[Fraction(3, 7), -1], [50, Fraction(1, 2)], [Fraction(5, 8), Fraction(-2, 5)]])
L = np.array([[6, 5], [11, 16], [8, 10], [3, 7]])
print(f"La posición destacada en M es M({M[0, 2]})")
print(f"La posición destacada en T es T({T[2, 1]})")
print(f"La posición destacada en N es N({N[1, 0]})")
print(f"La posición destacada en K es K({K[0, 2]})")
print(f"La posición destacada en S es S({S[2, 1]})")
print(f"La posición destacada en L es L({L[2, 1]})")

# Ejercicio 15
# La siguiente matriz [D] = (Di,j) nos indica la distancia, en kilometros, desde la ciudad i a la ciudad j.Donde las ciudades que se consideraron son: Arica(A), La Serena(L), Santiago(S), Concepcion(C).

"""
       A      L    S      C
D = [ [0,   1596, 2070, 2582],   A
      [1596,  0,  473,  989],  L
      [2070,  473,  0,  516],  S
      [2582,  989,  516,  0]]  C
"""
D = np.array([[0,   1596, 2070, 2582],[1596,  0,  473,  989],[2070,  473,  0,  516],[2582,  989,  516,  0]]) 


# A) Indique el orden de la matriz [D]

print(f"el orden de la matriz D es {D.shape}") 

# B) interprete el valor de D(2,4)

print(f"el valor de D(2,4) es {D[1,3]}")

# C) interprete el valor de D(4,3)

print(f"el valor de D(4,3) es {D[3,2]}")

# D) interprete el valor de D(1,2)

print(f"el valor de D(1,2) es {D[0,1]}")

# E) ¿Por que, en la matriz [D], Di,j = dj,i?

print("por que la distancia de la ciudad i a la ciudad j es la misma que la distancia de la ciudad j a la ciudad i")

# F) ¿Por que, en la matriz [D], Di,i = 0?

print("por que la distancia de la ciudad i a la ciudad i es 0")

# Ejercicio 16

# Analice las siguientes matrices e indique si existe igualdad entre los pares de matrices, justificando su respuesta.

# F = [[5.6,2.1,0.3], [4.8,1.9,3.7]]
# G = [[5.6,2.1], [4.8,1.9]]
# H = [[5.6,2.1,0.3], [4.8,1.9,2.7]]

F = np.array([[5.6,2.1,0.3], [4.8,1.9,3.7]])
G = np.array([[5.6,2.1], [4.8,1.9]])
H = np.array([[5.6,2.1,0.3], [4.8,1.9,2.7]])

# A) ¿F = G?

print(f"existe igualdad entre F y G {F.shape == G.shape}, por que no tienen la misma cantidad de columnas")

# B) ¿F = H?

print(f"existe igualdad entre F y H {F.shape == H.shape}, por que tienen la misma cantidad de filas y columnas")

# Ejercicio 17

# La compañia Eissenwagen entregan sus reportes de ventas mensuales. las filas, en orden, representan el numero de vehiculos vendidos segun los modelos: regular, lujo y extra lujo. Las columnas, en orden, dan el numero de unidades vendidas segun los colores: rojo solar (R), blanco (B), plateado (P) y negro (N). las matrices para abril [A] y mayo [M] son:

"""
        R  B  P  N
[A] =[ [2, 6, 1, 2], regular
       [0, 1, 3, 5], lujo
       [2, 7, 6, 0]] extra lujo

        R  B  P  N
[M] =[ [0, 2, 4, 4], regular
       [2, 3, 3, 2], lujo
       [4, 0, 2, 6]] extra lujo
"""

A = np.array([[2, 6, 1, 2],[0, 1, 3, 5],[2, 7, 6, 0]])

M = np.array([[0, 2, 4, 4],[2, 3, 3, 2],[4, 0, 2, 6]])

# A) En abril, ¿Cuantos Vehiculos modelo extra lujo blanco se vendieron? Responda utilizando notacion matricial 

print(f"En abril se vendieron {A[2,1]}")

# B) En mayo, ¿cuantos modelos de lujos blancos se vendieron? Responda utilizando Matricial 

print(f"En mayo se vendieron {M[1,1]}")

# C) ¿En que mes se vendieron mas modelos regulares negros?

print(f"En mayo se vendieron mas autos negros regulares")

# D) ¿De que modelo y color se vendio el mismo numero de unidades en ambos meses?
 
print(f" En ambos Meses se vendieron los autos de mismo modelo y color en la posicion {A[1,2]} y {M[1,2]}")

# E) ¿En que mes se vendieron mas modelos de lujos?

suma_modelos_de_lujo_A = np.sum(A[1, :]) # sumar filas en este caso la 2 fila
suma_modelos_de_lujo_M = np.sum(M[1, :]) # sumar filas en este caso la 2 fila 

if suma_modelos_de_lujo_A > suma_modelos_de_lujo_M:
    print(f"En el mes de Abril se vendieron más modelos de lujo con un total de {suma_modelos_de_lujo_A} unidades.")
elif suma_modelos_de_lujo_A < suma_modelos_de_lujo_M:
    print(f"En el mes de Mayo se vendieron más modelos de lujo con un total de {suma_modelos_de_lujo_M} unidades.")
else:
    print("En ambos meses se vendieron la misma cantidad de modelos de lujo.")

# F) ¿En que mes se vendieron mas articulos rojos 

suma_columnas_A = np.sum(A, axis=0) # esto es para sumar columnas
suma_columnas_M = np.sum(M, axis=0) # esto es para sumar columnas 

total_articulos_rojos_A = suma_columnas_A[0] # esto es para obtener el total de articulos rojos en el mes de abrilentre [] se define que columna se quiere obtener
total_articulos_rojos_M = suma_columnas_M[0] # esto es para obtener el total de articulos rojos en el mes de mayo entre [] se define que columna se quiere obtener

if total_articulos_rojos_A > total_articulos_rojos_M:
    print(f"En el mes de Abril se vendieron más artículos rojos con un total de {total_articulos_rojos_A} unidades.")
elif total_articulos_rojos_A < total_articulos_rojos_M:
    print(f"En el mes de Mayo se vendieron más artículos rojos con un total de {total_articulos_rojos_M} unidades.")
else:
    print("En ambos meses se vendieron la misma cantidad de artículos rojos.")

# G) Interprete los elementos matriciales A(3,2) y M(1,3).

print(f"En abril se vendieron {A[2,1]} autos de modelo extra lujo blanco")

print(f"En mayo se vendieron {M[0,2]} autos de modelo regular plateado")