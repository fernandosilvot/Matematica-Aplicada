import numpy as np
# Ejercicio 1

# A [[5, 12, 3], [3, 5, 5]]
# B [[235], [115], [105]]

A = np.array([[5, 12, 3], [3, 5, 5]])
B = np.array([[235], [115], [105]])

# A(2X3) * B(3X1) = C(2X1)

C = A.dot(B)
print(f"la matriz C es: \n{C}\n")

# Ejercicio 2

# Encontrar matriz G = E * F

E = np.array([[2, 3], [5, 1]])
F = np.array([[3, 5, 7], [2, 8, 5]])

# E(2X2) * F(2X3) = G(2X3)

G = E.dot(F)
print(f"la matriz G es: \n{G}\n")

# Ejercicio 3

# La matriz E expresa la producción, en kilogramos, de zanahorias, papas y tomates de tres productores, Juan (J), Alicia (A) y Sofía (S). Mientras que la matriz F, expresa el valor, en pesos, que les pagarán por kilogramo de zanahorias (Z), papas (P) y tomates (T) en el supermercado 1 (51) o en el supermercado 2 (S2). 

#     Z  P   T
# E [[66, 45, 68],J 
#    [70, 54, 56],A
#   [70, 49, 64]]S


#     S1  S2
# F [[480, 470],Z
#    [580, 640],P
#   [420, 370]]T

# se define la matriz G = E*F
# a ) determine la matriz G

E = np.array([[66, 45, 68], [70, 54, 56], [70, 49, 64]])
F = np.array([[480, 470], [580, 640], [420, 370]])

# E(3X3) * F(3X2) = G(3X2)

G = E.dot(F)
print(f"la matriz G es: \n{G}\n")
