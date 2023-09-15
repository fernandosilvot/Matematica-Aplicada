# matriz transpuesta
import numpy as np

# Ejercicio 1

# [[7,-3],[4,1],[-2,0],[8,5]]^T

primera = np.array([[7,-3],[4,1],[-2,0],[8,5]])
primeraT = primera.T
print(f"la matriz primeraT es: \n{primeraT}\n")

# Ejercicio 2

# [[2,8,[0,1],[-5,-4]]^T

segunda = np.array([[2,8],[0,1],[-5,-4]])
segundaT = segunda.T
print(f"la matriz segundaT es: \n{segundaT}\n")

# Multiplicación de matrices

# Ejercicio 1

# G =[[55,39,68],[33,59,64],[72,63,62]] * [[550,500],[650,700],[450,400]]

G = np.array([[55,39,68],[33,59,64],[72,63,62]])
H = np.array([[550,500],[650,700],[450,400]])
GH = G.dot(H)
print(f"la matriz GH es: \n{GH}\n")


# Ejercicio 2

# M = [[2,8,3],[5,4,1]]
# N = [[4,1],[6,3],[2,4]]
# Sea P = M*N

M = np.array([[2,8,3],[5,4,1]])
N = np.array([[4,1],[6,3],[2,4]])
P = M.dot(N)
print(f"la matriz P es: \n{P}\n")

# Ejercicio 3

# Sea M= [[9,14],[4,5]]
# Sea Q= [[200,240,220],[175,210,215]]

# ademas se define las matrices I = M*Q y H = Q*M

M = np.array([[9,14],[4,5]])
Q = np.array([[200,240,220],[175,210,215]])
I = M.dot(Q)
print(f"la matriz I es: \n{I}\n")
print(f"la matriz H no se puede calcular\n")

# Ejercicio 4

# a = [[2,0,1],[3,0,0],[5,1,1]]
# b = [[1,0,1],[1,2,1],[1,1,0]]

A = np.array([[2,0,1],[3,0,0],[5,1,1]])
B = np.array([[1,0,1],[1,2,1],[1,1,0]])
AB = A.dot(B)
print(f"la matriz AB es: \n{AB}\n")

# Tarea #2

# dadas las Siguientes matrices

# A = [[4,3],[7,6]]
# B = [[1,0],[3,6],[5,8]]
# C = [[5,10,8],[7,3,4],[12,6,9]]
# D = [[11,12],[34,23]]
# E = [[2,3],[5,1]]
# F = [[3,5,7],[2,8,5]]
# G = [[-3,2,6],[9,0,12],[9,4,2]]
# H = [[51,10],[48,21]]
# I = [[0,0],[2,-1],[1,7]]
# J = [[12,10,21],[35,14,12],[9,4,2]]
# K = [[8,9],[17,13],[18,27]]
# L = [[8,15,21],[14,8,-10]]

# indique en cada operacion si es posible de realizar. En caso afirmativo,resuelva.

# 1. A*B

A = np.array([[4,3],[7,6]])
B = np.array([[1,0],[3,6],[5,8]])
#AB = A.dot(B)
print(f"la matriz AB no se puede calcular\n")

# 2. E*H

E = np.array([[2,3],[5,1]])
H = np.array([[51,10],[48,21]])
EH = E.dot(H)
print(f"la matriz EH es: \n{EH}\n")

# 3. J*G

J = np.array([[12,10,21],[35,14,12],[9,4,2]])
G = np.array([[-3,2,6],[9,0,12],[9,4,2]])
JG = J.dot(G)
print(f"la matriz JG es: \n{JG}\n")

# 4. B*C

B = np.array([[1,0],[3,6],[5,8]])
C = np.array([[5,10,8],[7,3,4],[12,6,9]])
#BC = B.dot(C)
print(f"la matriz BC no se puede calcular\n")



