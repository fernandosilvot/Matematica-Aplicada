# suma y resta de matrices
import numpy as np
# ejercicio 1

# Podemos encontar C - D al restar las entradas correspondientes de C y D. ESto se muestra a continuación:

C = np.array([[2, 8], [0, 9]])
D = np.array([[5, 6], [11, 3]])
print(C - D)

# ejercicio 2

A = np.array([[5, 2], [0, 1], [1, 9]])
B = np.array([[2, 3], [4, 1], [0, 2]])
print(f"La suma de A+B en 1,1: \n{A[0,0]+B[0,0]}")

# ejercicio 3

A = np.array([[-10, 12], [-6, 3]])
B = np.array([[-1, 4], [22, 7]])
print(f"La suma de A+B en 1,1: \n{A[0,0]+B[0,0]}")

# ejercicio 4

Y = np.array([[4, 16], [10, 22]])
X = np.array([[1, 15], [6, 3]])
print(f"La resta de Y-X en 1,1: \n{Y[0,0]-X[0,0]}")

# ejercicio 5

A = np.array([[3,4,9], [6,8,6], [7,3,4]])
B = np.array([[1,6,7], [6,4,2], [4,1,5]])
print(f"La resta de A+B en 1,1: \n{A[0,0]-B[0,0]}")

# ejercicio 6

A = np.array([[1,2], [0,4], [-1,-1]])
B = np.array([[-1,-1], [4,1], [3,1]])
print(f"La resta de A+B en 1,1: \n{A[0,0]-B[0,0]}")

# ejercicio 7

# Las matrices [A] y [B] representan las ventas anuales, en millones de dólares, de los tres productos de una empresa en las cuatro regiones donde está disponible. De este modo (ai,j) y (bi,j) reflejan el monto de las ventas del producto i en la región j del primer y segundo año, respectivamente, desde que la empresa sale al mercado. 

A = np.array([[2.6, 4.8, 1.8, 0.9], [3.2, 4.4, 2.5, 2.8], [2.4, 3.6, 3.8, 2.5]])
B = np.array([[3.6, 2.5, 3.0, 2.5], [4.5, 5.0, 3.5, 3.8], [2.9, 3.0, 4.6, 4.0]])

# a) indique el orden de cada matriz
print(f"El orden de A es: {A.shape}")
print(f"El orden de B es: {B.shape}")

# b) Determine la matriz C = A + B, e interprete el elemento c2.4
C = A + B
print(f"El elemento c2.4 es: {C[1,3]}")

# c) Determine la matriz D = A - B, e interprete el elemento d3.1
D = A - B
print(f"El elemento d3.1 es: {D[2,0]}")

# ejercicio 8

#La matriz A muestra los pesos, en kilogramos, de cuatro hombres y cuatro mujeres antes de fiestas patrias, mientras que la matriz D muestra sus pesos después de dichas festividades 

#               1   2   3   4
A = np.array([[71, 80, 75, 90],    # hombre 
              [65, 58, 74, 82]])   # mujer

#               1   2   3   4
D = np.array([[75, 83, 80, 94],    # hombre
              [67, 60, 78, 82]])   # mujer

# a) la matriz V nos entrega las variaciones de peso para estas ocho personas.¿Que operacion entre las matrices A y D debemos realizar para obtener V?

print(f"La operacion para obtener V es restar A-D")

# b) calcule la matriz V

V = A - D
print(f"La matriz V es: \n{V}")

# c) ¿Cuanto fue el aumento de peso para la mujer 3 y el hombre 2? responda usando notacion matricial

print(f"El aumento de peso para la mujer 3 y el hombre 2 es: {V[1,2]} y {V[0,1]}")

# d) interprete los elementos a2.1 y d1.4 y v2.2

print(f"El elemento a2.1 es: {A[1,0]}")
print(f"El elemento d1.4 es: {D[0,3]}")
print(f"El elemento v2.2 es: {V[1,1]}")

# ejercicio 9

# encontrar la matriz (G)                 G= E + F

E = np.array([[8, 2, 1], [-5, 6, 7]])
F = np.array([[3, 4, 0], [4, -3, 9]])
G = E + F
print(f"La matriz G es: \n{G}")

# ejercicio 10

# encontrar la matriz (J)                 J= E - F

E = np.array([[8, 2, 1], [-5, 6, 7]])
F = np.array([[3, 4, 0], [4, -3, 9]])

J = E - F

print(f"La matriz J es: \n{J}")
