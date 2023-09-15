# se resolvieron las tareas anteriormente planteadas en la clase 4
# pero se añade uno a la ultima 
import math
# Ejercicio pasados 
# Revisar tarea 
# 1) El tercer termino de una sucesion geometrica es 5  y el sexto termino es de 40. determine

#A) la razon geometrica
q3 = 5
q6 = 40
r = q6/q3
r3= (q6/q3)**(1/3)
print(f"La razon geometrica es: {r3}")

#B) El primer termino

q1 = q3/r3**(3-1)
print(f"El primer termino es: {q1}")

#C) La expresion del termino de lugar "n"

print(f"Qn = {q1} * {r3}**(n-1)")

#D) El octavo termino. Calcule con la forma que estime conveniente

q8 = q1 * r3**(5-1)
print(f"El termino del lugar 8 es: {q8}")

#E) ¿Que lugar ocupa en esta sucesion el termino "20480"? Use logaritmo.

n = math.log(20480/q1, r3) +1
print(f"El termino 20480 ocupa el lugar: {n:.2f}") # el :.2f es para que solo muestre 2 decimales

print("--------------------------------------------------")
"""
    2)En un experimento de laboratorio, se coloca una bacteria en un ambiente propicio para su reproducción. 
    Se sabe que cada hora la población de bacterias se duplica debido a las condiciones ideales. Inicialmente, había 10 bacterias.
"""
# A)¿Cuál es el valor que se considera como “r” (Razón Constante)?

q1 = 10
q2 = 20
r = q2/q1
print(f"La razon constante es: {r}")
# B) calcula cuantas bacterias habra en 3 horas

n = 3
q3 = q1 * r**(n-1)
print(f"En {n} horas habra {q3} bacterias")

#C) ¿En cuántas horas la población de bacterias será de al menos 640?

n = math.log(640/q1, r) +1
print(f"En {n:.2f} horas la poblacion de bacterias sera de al menos 640")

print("--------------------------------------------------")
#3) La tasa de crecimiento aumenta en un 2% anual.
#A) ¿Cuál es el valor que se considera como “r” (Razón Constante)?

r = 102/100
print(f"La razon constante es: {r}")

print("--------------------------------------------------")
#4) La tasa de la población disminuye en un 2% anual.
#A) ¿Cuál es el valor de la razon constante?

r = 98/100
print(f"La razon constante es: {r}")

print("--------------------------------------------------")
"""
    5) Rodrigo tiene 7 años y comenzó a ahorrar dinero en su alcancía. En el primer
    día depositó $50, y cada día posterior aumentó en $30 la cantidad que ahorraba.
"""
#A) ¿Cuánto dinero tiene al octavo día?

q1 = 50
r = 30
n = 8
q8 = q1 + r*(n-1)
print(f"Al octavo dia tiene {q8} pesos")

#B) ¿Cuántos días necesitará María para tener $500?

q1 = 50
r = 30
q500 = 500
n = (q500 - q1)/r +1
print(f"Rodrigo necesitara {n:.2f} dias para tener 500 pesos")

print("--------------------------------------------------")

"""
    6) Supongamos que tienes una inversión inicial de $10.000 en una cuenta de
    ahorros con una tasa de interés el cual aumenta del 10% mensual. 
"""
#¿Calcular cuánto dinero tienes en el sexto mes?.

q1 = 10000
r = 110/100
n = 6
q6 = q1 * r**(n-1)
print(f"En el sexto mes tendra {q6:.2f} pesos")

print("--------------------------------------------------")

"""
    7) Dado los siguientes tres términos de una sucesión numérica 3; 5.4; 9.72, 
"""
# determinar si es una progresión aritmética o geométrica

print(f"Es una progresion geometrica {5.4/3 == 9.72/5.4, r}")

# encuentra el vigésimo término.

q1 = 3
r = 5.4/3
n = 20
q20 = q1 * r**(n-1)
print(f"El vigesimo termino es: {q20:.2f}")