import numpy as np
# ejercicio 1

X = np.array([[4, 16], [10, 22]])
Y = np.array([[1, 15], [6, 3]])
res = X + Y
print(f"en la posicion 1,1 el resultado es {res[0,0]}")

# ejercicio 2

X = np.array([[1, 2], [0, 4], [-1,-1]])
Y = np.array([[-1, -1], [4, 1], [3, 1]])
res = X + Y
print(f"en la posicion 1,1 el resultado es {res[0,0]}")

# ejercicio 3

# Encontrar la matriz (G)                       G = E + F

E = np.array([[8,2,1], [-5,6,7]])
F = np.array([[3,4,0], [4,-3,9]])
G = E + F
print(f"la matriz G es {G}")

# ejercicio 4

# Encontrar la matriz (J)                       J = E + F

E = np.array([[8,2,1], [-5,6,7]])
F = np.array([[3,4,0], [4,-3,9]])
J = E + F
print(f"la matriz J es {J}")

# ejercicio 5

#En una academia de baile tiene una sede en Santiago y Rancagua. En ambas academias se arman por niveles desde 1°  a 4° nivel. Ellos cuentan con tres cursos por nivel, MAÑANA, TARDE Y VESPERTINO.

S = np.array([[33,28,28], [39,36,28], [35,40,35], [36,10,11]])
R = np.array([[33,39,33], [30,15,10], [20,12,25], [4,15,11]])

# a) Indique el orden de cada matriz 
print(f"el orden de la matriz S es {S.shape}")
print(f"el orden de la matriz R es {R.shape}")

# b) Calcular la matriz F = [R]+[S] total de estudiantes por nivel y curso.
F = R + S
print(f"la matriz F es {F}")

# c) Interprete cualquier elemento de la matriz F.
print(f"el elemento de la matriz F en la posicion 1,1 es {F[0,0]}")

# ejercicio 6

# EL año 2020 y el año 2021 dos empresas sacaron sus estados financieros de sus ventas en (miles $) para saber si quedaron con utilidades.

A = np.array([[104],[23],[450],[180],[100]])
B = np.array([[50],[100],[90],[110],[25]])

# a) ¿Cuál es el total de productos vendidos en la comuna de la florida?
total_folrida = A + B

print(f"el total de productos vendidos en la comuna de la florida es {np.sum(total_folrida)}")

# b) Indicar cual producto se fue el más vendido, interpretar resultados.
print(f"el producto mas vendido en total de la comuna de la florida es {np.max(total_folrida)}")

# ejercicio 7

#   ENCONTRAR EL TOTAL DE AUTOS VENDIDOS

#              R B P N
A = np.array([[2,6,1,2], # Regular
              [0,1,3,5], # Lujo
              [2,7,6,0]]) # extra lujo

#              R B P N
M = np.array([[0,2,4,4], # Regular
              [2,3,3,2], # Lujo
              [4,0,2,6]]) # extra lujo

total_autos = A + M

print(f"el total de autos vendidos es {np.sum(total_autos)}")

# ejercicio 8

# La matriz A, da cuenta del número de alumnos y de alumnas que obtuvieron un cuatro o más en la prueba 1, prueba 2 y prueba 3 de cierta asignatura en estudio. Por otro lado la matriz B corresponde al número de alumnos y de alumnas que obtuvieron menos de un cuatro en la prueba 1. prueba 2 y prueba 3 de la misma asignatura.

A = np.array([[90, 100, 110], [130, 140, 150]])
B = np.array([[70, 60, 50], [50, 40, 30]])

# a) Determine cuantas alumnas obtuvieron un cuatro o más en la prueba 2 y cuantos alumnos obtuvieron menos de un cuatro en la prueba 3.

print(f"la cantidad de alumnas que obtuvieron un cuatro o más en la prueba 2 es {A[0,1]+A[1,1]}")

print(f"la cantidad de alumnos que obtuvieron menos de un cuatro en la prueba 3 es {B[0,2]+B[1,2]}")

# b) interprete a1.3

print(f"el elemento de la matriz A en la posicion 1,3 es {A[0,2]}")
