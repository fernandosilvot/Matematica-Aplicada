print("Ejercicios Clase\n")
# Sea la sucesion (Kn) definida por su termino general (-1)**n
# determine los primeros 20 terminos

lista_terminos = []
for i in range(1,21):
    kn = (-1)**i
    lista_terminos.append(kn)
print(f"Los primeros 20 terminos de la sucesion son: {lista_terminos}")

#¿que se puede afirmar de los terminos de la sucesion?
print("Los terminos de la sucesion son alternantes, ya que cambian de signo")

#¿cual es el termino que ocupa la posicion 2020?
lista_terminos = []
for i in range(1,2021):
    kn = (-1)**i
    lista_terminos.append(kn)
print(f"El termino que ocupa la posicion 2020 es: {lista_terminos[2019]}")


#cual es el septimo termino de la sucesion?
#Qn = 4+(7-1)*12
lista_terminos = []
for i in range(1,8):
    qn = 4+(i-1)*12
    lista_terminos.append(qn)
print(f"El septimo termino de la sucesion es: {lista_terminos[6]}")

# como puedo comprobar si 76 es el spetimo termino de la sucesion?
#formula = 76 = 4+(n-1)*12
# ((76-4)/12) +1 =n

n = ((lista_terminos[6]-4)/12) +1
print(f"76 es el septimo termino de la sucesion: {n == 7}")

# considere la sucesion aritmetica: 25,72;26,93;28,14;... determine 
# la diferencia aritmetica 
d1 = 28.14-26.93
d2 = 26.93-25.72
print(f"La diferencia aritmetica es {d1}: {d1 == d2}")

#la expresion del termino de lugar "n"
print("Qn = Q1 + (n-1)*d")

# el termino del lugar 50 
q50 = 25.72 + (50-1)*d1
print(f"El termino del lugar 50 es: {q50}")

#¿ que lugar  ocupa en esta sucesion el termino "411.71"?
n = ((411.71-25.72)/d1) +1
print(f"El termino 411.71 ocupa el lugar: {n}")
qn = 25.72 + (n-1)*d1
print(f"El termino {n} ocupa el lugar: {qn}")


# en una sucesion aritmetica, la diferencia entre un termino y el anterior es 4 y el decimo termino es -20 determine 
# el primer termino
# Q10 = Q1 + (10-1)*d
n = 10
qn = -20
d = 4
q1 = qn - (n-1)*d
print(f"El primer termino es: {q1}")

# la expresion del termino de lugar "n"
print("Qn = Q1 + (n-1)*d")

#el termino del lugar 100
q100 = q1 + (100-1)*d
print(f"El termino del lugar 100 es: {q100}")

#¿que lugar ocupa en esta sucesion el termino "1680"?
n = ((1680-q1)/d) +1
print(f"El termino 1680 ocupa el lugar: {n}")

#Una casa se arrienda por 2 años, considerando que este periodo el arriendo se incrementara todos los meses en una cantidad constante. Si el quinto mes de arriendo se pagara 204000 y el decimo tercer mes 252000,¿cual sera el valor  del arriendo en el primer mes y ultimo mes?
q5 = 204000
q13 = 252000
dx = 13-5
d = q13-q5
d8 = (d/dx)
q1 = q5 - (5-1)*d8
q12 = q5 + (24-5)*d8
print(f"El valor del arriendo en el primer mes es: {q1}")
print(f"El valor del arriendo en el ultimo mes es: {q12}")

print("Ejercicio tipo prueba\n")

# segun estadisticas de un hospital, en promedio los recien nacidos miden 48 cm y por cada mes, hasta que cumplen un año, su altura se incrementa uniformemente en 0.7 cm. considere que An representa la  altura promedio de los bebes al cabo de n meses
# indicar que tipo de sucesion modela la altura promedio de los bebes
print("Es una sucesion aritmetica, por que la altura se incrementa uniformemente")

# escriba la expresion del termino "An"
print("An = 48 + (n-1)*0.7")

# ¿cuanto miden en promedio los bebes al cabo de 7 meses de haber nacido?
n = 7
an = 48 + (n-1)*0.7
print(f"Los bebes miden en promedio {an} cm al cabo de 7 meses de haber nacido")

#¿cuantos meses de vida deben tener un bebe para medir, en promedio 54.3 cm?
an = 54.3
n = ((an-48)/0.7) +1
print(f"Los bebes deben tener {n} meses de vida para medir, en promedio 54.3 cm")

#en una sucesion aritmetica , el cuarto termino es 64 y el termino lugar 54 es -61. determine el vigesimo tercer  termino
d = -125/50
q1 = 64 - (4-1)*d
q23 = q1 + (23-1)*d
print(f"El vigesimo tercer termino es: {q23}")

print("Tarea solo para valientes\n ")

#en una colonia de abejas, en el primer dia de investigacion los alumnos de ingenieria 

#Agricola contabilizaron 3 abejas, el segundo el segundo día contabilizaron 9 y el tercero 15. Si la cantidad de abejas se fue incrementando de manera constante, se pide

# Indicar que tipo de sucesión modela la cantidad de abejas.

print("Es una sucesion aritmetica, por que la cantidad de abejas se incrementa de manera constante")

# Escribir la expresión del término de lugar "n".

print("An = 3 + (n-1)*6")

# Determinar cuántas abejas habian el vigesimo dia

n = 20
an = 3 + (n-1)*6
print(f"El vigesimo dia habian {an} abejas")

# Determinar cuantas abejas habia a los 30 dias 

n = 30
an = 3 + (n-1)*6
print(f"A los 30 dias habian {an} abejas")

# ¿Cuantos dias deben transcurrir para que se puedan contabilizar 333 abejas?

an = 333
n = ((an-3)/6) +1
print(f"Deben transcurrir {n} dias para que se puedan contabilizar 333 abejas")
