# Ponderacion de matrices

# Importamos la libreria numpy
import numpy as np

# Ejercicio 1

# dada B= [[-4,-2],[7,1]], encuentra -3B
B = np.array([[-4,-2],[7,1]])
B3 = -3*B
print(f"la matriz -3B 1.1 es: {B3[0,0]}")

# Ejercicio 2

# dada C= [[-42],[27],[-3]], encuentra  (1/3)C
C = np.array([[-42],[27],[-3]])
C3 = (1/3)*C
print(f"la matriz (1/3)C 1.1 es: {C3[0,0]}")

# Ejercicio 3

# dada -2 * [[0],[-1],[-2]]
D = np.array([[0],[-1],[-2]])
D2 = -2*D
print(f"la matriz -2D 1.1 es: {D2[0,0]}")

# Ejercicio 4

# dada -5 * [[-2,4,3],[2,-2,-2]]
E = np.array([[-2,4,3],[2,-2,-2]])
E5 = -5*E
print(f"la matriz -5E 1.1 es: {E5[0,0]}")

# Ejercicio 5

# dada 2 * [[-2,-2],[-1,0]]
F = np.array([[-2,-2],[-1,0]])
F2 = 2*F
print(f"la matriz 2F 1.1 es: {F2[0,0]}")

# Ejercicio 6

# dada -6 * [[0,3],[3,-1],[2,-2]]
G = np.array([[0,3],[3,-1],[2,-2]])
G6 = -6*G
print(f"la matriz -6G 1.1 es: {G6[0,0]}")

# Ejercicio 7

#a empresa BETA tiene en Chile dos plantas; y en cada una de ellas fabrica tres productos. El número de unidades del producto i fabricadas en la planta j en una semana, está representado en la matriz [C] mediante Cij.

#C = [[120,70],[150,110],[80,160]]

#La empresa BETA, se expande creando una filial en Ecuador. Esta filial también tiene dos plantas y en ellas fabrica los mismos tres productos. Y la producción semanal de dicha filial estará representada por una matriz [E]. 

#a) Si los volúmenes de producción semanal de la filial en Ecuador son un 20% menor que en Chile, determine la matriz [E].

C = np.array([[120,70],[150,110],[80,160]])
E = 0.8*C
print(f"la matriz E es: \n{E}\n")

#b) Si la matriz [T] representa la producción semanal total de la empresa BETA, considerando ambas filiales, determine la matriz [T].

T = C + E
print(f"la matriz T es: \n{T}\n")


# Ejercicio 8
#interprete B1.3

# Una empresa que fabrica zapatos tiene dos plantas, una en Valparaíso y la otra en Temuco. Ésta produce zapatos de color negro, blanco y café, tanto para niños, damas como caballeros. La capacidad actual de producción mensual (en miles de pares) para las plantas de Valparaíso y Temuco, respectivamente, están dadas por las matrices V y T. Para ambas matrices, según el orden en que se mencionan, las filas corresponden al color del calzado y las columnas al tipo de persona que utilizará el calzado.

# V = [[30,34,20],[45,20,16],[14,26,25]]

# T = [[35,30,26],[52,25,18],[23,24,32]]

# A) Si para el próximo año se estima que la producción en Valparaíso aumenta en un 30%, mientras que la de Temuco se reduce en un 10%, represente la nueva producción total en la matriz B. 

V = np.array([[30,34,20],[45,20,16],[14,26,25]])

T = np.array([[35,30,26],[52,25,18],[23,24,32]])

V = 0.7 * V

T = 0.9 * T

B = V + T

print(f"La matriz b1,3 {B[0,2]:.2f}")

# Ejercicio 9

# Formar la matriz F, LA CUAL ES EL 15% AUMENTADA LA MATRIZ c

C = np.array([[120,70],[150,110],[80,160]])

F = 1.15 * C

print(f"La matriz F es: \n{F}\n")

# Ejercicio 10

#Formar la matriz B, LA CUAL ES EL 10% disminuida LA MATRIZ A

A = np.array([[65,64,46],[97,45,34],[37,50,57]])

B = 0.9 * A

print(f"La matriz B es: \n{B}\n")
