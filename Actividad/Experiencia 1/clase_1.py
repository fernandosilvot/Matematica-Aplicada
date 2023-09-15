
print("Bienvenido a la clase 1 de Matematica Aplicada")

print("Ejercicio 1\nsea la sucsion, definida por su termino general, Sn = 3n**2+7")
print("1) Calcular los 5 primeros terminos de la sucesion")
print("2) Calcular los 5 terminos que vienen inmediatamente despues de decimo quinto termino")
opcion = int(input("Ingrese la opcion\n>>> "))

if opcion == 1: # 1) Calcular los 5 primeros terminos de la sucesion
    lista_5_primeros_terminos = []
    for i in range(1,6):
        Sn = 3*i**2+7
        lista_5_primeros_terminos.append(Sn)
    print(f"Los {len(lista_5_primeros_terminos)} primeros terminos de la sucesion son: {lista_5_primeros_terminos}")

elif opcion == 2: # 2) Calcular los 5 terminos que vienen inmediatamente despues de decimo quinto termino
    lista_5_terminos_despues_del_15 = []
    for i in range(16,21):
        Sn = 3*i**2+7
        lista_5_terminos_despues_del_15.append(Sn)
    print(f"Los {len(lista_5_terminos_despues_del_15)} terminos que vienen inmediatamente despues de decimo quinto termino son: {lista_5_terminos_despues_del_15}")

else: # Opcion no valida
    print("Opcion no valida")