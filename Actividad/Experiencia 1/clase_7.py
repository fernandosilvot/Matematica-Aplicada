# Ejemplo 1 
# calcular la sumatoria 250 ∑ i=1 (18.5 + 2.5i)

# Formula aritmetica n/2*(2*a1+(n-1)*d)

a = 18.5
d = 2.5
n = 250
print(f"250 ∑ i=1 (18.5 + 2.5i) = {n/2*(2*a+(n-1)*d)} o aproximado {n/2*(a+a+(n-1)*d):.0f}")

# Ejemplo 2
# Calcular la sumatoria 100 ∑ i=61 (61+7i)

# Formula aritmetica cuando no parte del 1 ((100 ∑ i=1 (61+7i))-(60 ∑ i=1 (61+7i))))

n = 100
a = 61
d = 7
formula1 = (n/2)*(2*a+(n-1)*d)
n = 60
formula2 = (n/2)*(2*a+(n-1)*d)

print(f"100 ∑ i=61 (61+7i) = {formula1 - formula2} o aproximado {(formula1-formula2):.0f}")

# Ejemplo 3
# Calcular la sumatoria 36 ∑ i=1 (5000*1.06i)

# Formula geometrica a1*(1-r**n)/(1-r)

a = 5000
r = 1.06
n = 36

print(f"36 ∑ i=1 (5000+1.06i) = {a*(1-r**n)/(1-r)} o truncado es {a*(1-r**n)/(1-r):.0f}")

# Ejemplo 4
# Calcular la sumatoria 80 ∑ i=55 (7500*0.97i)

# Formula geometrica cuando no parte del 1 ((80 ∑ i=1 (7500*0.97i))-(54 ∑ i=1 (7500*0.97i))))

a = 7500
r = 0.97
n = 80
formula1 = a*(1-r**n)/(1-r)

n = 54
formula2 = a*(1-r**n)/(1-r)

print(f"80 ∑ i=55 (7500*0.97i) = {formula1 - formula2} o truncado es {(formula1-formula2):.0f}")


# Ejemplo 5

# un nuevo canal de youtube registra 50 visitas la primera semana de funcionamiento, registra 66 visitas la segunda, 82 la tercera y asi sucesivamente. Representado por Vi la cantidad de visitas en la semana i,

# determine 40 ∑ i=1 Vi

# Formula aritmetica n/2*(2*a1+(n-1)*d)

a = 50
d = 16
n = 40
formula1 = n/2*(2*a+(n-1)*d)

print(f"40 ∑ i=1 Vi = {formula1} o truncado es {(formula1):.0f}")

# Ejemplo 6

# Diego decide ahorrar en dolares para un viaje durante dos años y medio. El primer mes ahorra 900 dolares, el segundo mes 810 dolares, el tercer mes 729 dolares, y asi sucesivamente. Represente por "Di" la cantidad de dolares que ahorra Diego en el mes "i".

# determine 12 ∑ i=1 Di

# Formula geometrica a1*(1-r**n)/(1-r)

a = 900
r = 0.9
n = 12
formula1 = a*(1-r**n)/(1-r)

print(f"12 ∑ i=1 Di = {formula1} o truncado es {(formula1):.0f}")
