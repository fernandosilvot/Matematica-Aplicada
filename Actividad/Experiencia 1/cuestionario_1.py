# ejercicio 1

#Considere la siguiente sucesión:

#2045; 2086, 5; 2128; 2169,5; …

#¿A qué tipo de sucesión corresponde?

print("a una sucesion aritmetica")

# ejercicio 2

#Considere la siguiente sucesión:

#32; 54,4; 92,48; 157,21; …

#¿A qué tipo de sucesión corresponde?

print("a una sucesion geometrica")

# ejercicio 3

#Considere la siguiente sucesión:

#-102; -66; -30; 6;…

#¿A qué tipo de sucesión corresponde?

print("a una sucesion aritmetica")

# ejercicio 4

#Pamela decide ahorrar durante 2 años para un viaje a Europa. Durante el primer mes ahorra 50 euros, el segundo mes 62 euros, el tercer mes 74 euros y así sucesivamente. En este caso se define ej como la cantidad de euros ahorrados durante el mes j. La expresión que calcula cada término de la sucesión ej es:

print("Ej = 50 + 12 * (j - 1)")

# ejercicio 5

#Dada la sucesión an = 88-3n2

#Calcule el término que ocupa la posición, n=4

an = 88 - 3 * 4**2

print(f"el termino que ocupa la posicion n=4 es {an}")

# ejercicio 6

# Considere la siguiente sucesión:

#0, 3, 8, 15, 24, …

#¿Cuál de las siguientes fórmulas de sumatoria nos permite calcular la suma de los 5 primeros términos de la sucesión?

# a) pila sumatorio i menos 1 con i igual 1 debajo y 5 encima

# b) pila sumatorio i al cuadrado menos 1 con i igual 1 debajo y 5 encima

# c) pila sumatorio 2 elevado a i menos 1 con i igual 1 debajo y 5 encima

# d) pila sumatorio i más 3 con i igual 1 debajo y 5 encima

print("la respuesta correcta es la B")

# ejercicio 7

# En una sucesión aritmética, la diferencia entre un término y el anterior es 7 y el término de lugar 6 es 169. Determine el primer término de dicha sucesión.

a_1 = 169 - 7 * (6 - 1)

print(f"el primer termino de la sucesion es {a_1:.2f}")

# ejercicio 8

# La tasa de crecimiento de la población de una ciudad es del 3% anual. Si la población actual es de 1751 habitantes, determinar cuantos habitantes aproximadamente tendrá dentro de 2 años. (En caso de ser necesario, considere dos cifras decimales en su respuesta).

poblacion = 1751

poblacion_2 = poblacion * (1.03**2)

print(f"la poblacion dentro de 2 años sera de {poblacion_2:.2f}")

# ejercicio 9

# Considera la sucesión 2.2n2-1. Determine el valor del término que ocupa la posición 22. (En caso de ser necesario, considere una cifra decimal en su respuesta). 

a_22 = 2.2 * 22**2 - 1

print(f"el valor del termino que ocupa la posicion 22 es {a_22:.2f}")

# ejercicio 10

# Considere la sucesión n3-5n. Determine el valor del término de lugar 7.

a_7 = (7**3) - (5 * 7)

print(f"el valor del termino de lugar 7 es {a_7:.2f}")

# ejercicio 11

# Considere la siguiente sucesión:

#0,034; 0,114; 0,194; 0,274; …

#Determine el término de lugar 11. (En caso de ser necesario, considere 3 cifras decimales en su respuesta).

a_11 = 0.034 + (11 - 1) * 0.08

print(f"el termino de lugar 11 es {a_11:.2f}")

# ejercicio 12

# Considere la siguiente sucesión:

#3,1; 6,2; 12,4; 24,8; …

#Determine el término de lugar 8. (En caso de ser necesario, considere una cifra decimal en su respuesta).

a_8 = 3.1 * 2**(8 - 1)

print(f"el termino de lugar 8 es {a_8:.2f}")

# ejercicio 13

# Un estudiante de la asignatura de matemática aplicada, quiere repasar los contenidos de la asignatura durante todos los días del mes de septiembre. Se propone que cada día, realizará dos ejercicios más que el día anterior. Si el primer día realiza 1 ejercicio ¿Cuántos ejercicios realizará el día 17 de estudio?

ejercicios = 1

for i in range(1, 17):
    ejercicios += 2

print(f"el dia 17 de estudio realizara {ejercicios} ejercicios")