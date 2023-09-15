import math # importa la libreria math para poder usar la funcion logaritmo

#considere la sucesion geometrica: 4,6,9,... determine

#la razon geometrica

q1 = 4
q2 = 6
r = q2/q1
print(f"La razon geometrica es: {r}")

# la expresion del termino de lugar "n"
print(f"Qn = {q1} * {r}**(n-1)")

# el termino del lugar 60
q60 = q1 * r**(60-1)
print(f"El termino del lugar 60 es: {q60}")


#¿ que lugar  ocupa en esta sucesion el termino "68.34375"?

n = math.log(68.34375/q1, r) +1
print(f"El termino 68.34375 ocupa el lugar: {n:.2f}") # el :.2f es para que solo muestre 2 decimales

# El tercer termino de una sucesion geometrica es 5  y el sexto termino es de 40. determine

# la razon geometrica

q3 = 5
q6 = 40
r = q6/q3
r3= (q6/q3)**(1/3)
print(f"La razon geometrica es: {r3}")

#El primer termino

q1 = q3/r3**(3-1)
print(f"El primer termino es: {q1}")

#La expresion del termino de lugar "n"

print(f"Qn = {q1} * {r3}**(n-1)")

#El octavo termino. Calcule con la forma que estime conveniente

q8 = q1 * r3**(8-1)
print(f"El termino del lugar 8 es: {q8}")

#¿Que lugar ocupa en esta sucesion el termino "20480"? Use logaritmo.

n = math.log(20480/q1, r3) +1
print(f"El termino 20480 ocupa el lugar: {n:.2f}") # el :.2f es para que solo muestre 2 decimales


#Hector,padre de matias, decidio ahorrar dinero por cada cumpleaños de su hijo. si el primer año ahorro 100 pesos, el segundo año ahorro 210 pesos, el tercer año ahorro 441 pesos, y asi durante los demas cumpleaños.¿cuanto dinero habra ahorrado hector cuando matias cumpla 18 años?

q1 = 100
q2 = 210
r = q2/q1
print(f"La razon geometrica es: {r}")
print(f"Qn = {q1} * {r}**(n-1)")
q18 = q1 * r**(18-1)
print(f"El termino del lugar 18 es: {q18}")

#En un experimento de laboratorio, se coloca una bacteria en un ambiente propicio para su reproducción. Se sabe que cada hora la población de bacterias se duplica debido a las condiciones ideales. Inicialmente, había 10 bacterias.

#¿Cuál es el valor que se considera como r (Razón Constante)?

q1 = 10
q2 = 20
r = q2/q1
print(f"La razon geometrica es: {r}")

#Calcula cuántas bacterias habrá en 3 horas.

q3 = q1 * r**(3-1)
print(f"En 3 horas habra : {q3}")

#¿En cuántas horas la población de bacterias será de al menos 640?

n = math.log(640/q1, r) +1
print(f"En {n:.2f} horas la poblacion de bacterias sera de al menos 640") 

# La tasa de crecimiento aumenta en un 2% anual.

# ¿ Cuál es el valor que se considera como r (Razón constante)?

r = 1.02 # 2% = 0.02 osea si aumenta en 2% es 1.02
print(f"La razon geometrica es: {r}")