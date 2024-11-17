#Escribe un programa que lea un número entero y determine si es positivo, negativo o cero.

numero=int(input("Ingrese el numero entero: "))

if numero >0:
    print("El numero es positivo.")
elif numero <0:
    print("El numero es negativo.")
else:
    print("El numero es 0.")