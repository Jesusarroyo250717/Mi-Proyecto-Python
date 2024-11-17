#Escribe un programa que solicite al usuario un número entero y calcule si es divisible por 3 y por 5.

numero= int(input("Ingrese un numero entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"El numero {numero} es divisible por 3 y 5.")
else:
    print(f"El numero {numero} no es divisible por 3 y 5.")
    